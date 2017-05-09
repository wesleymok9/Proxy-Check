"""
http://docs.python-requests.org/en/master/user/advanced/
must do a pip install requests
and pip install BeautifulSoup4
for the imports to work

this program works the same as
curl -x 168.159.213.211:80 --insecure https://google.com
"""
import requests
from bs4 import BeautifulSoup

#this import is just to disable a Warning because SSL cert is not being checked
#this is fine because we just need the status codes
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


"""will be using array instead of proxies=proxies to loop easier
proxies = {
  'http': 'http://127.0.0.1:80',
  'https': 'http://127.0.0.1:80',
}"""

#enter all proxies that want to be checked
proxy = ['http://127.0.0.1:80',]

try:
	#the site you want to check must show http or https in front of it
	check_site = 'https://www.facebook.com/'
	verify_proxy = 'http://www.ipchicken.com/'
	for item in proxy:
		#will get page using allow_redirects=False,verify=False to disable the SSL cert issue
		verify_proxy_url = requests.get(verify_proxy, proxies={'http': item, 'https': item,}, allow_redirects=False,verify=False)
		verify_proxy_page = BeautifulSoup(verify_proxy_url.text, "html.parser")
		proxy_ip = verify_proxy_page.find("b").text.split("\n")[1]
		#print(verify_proxy_page.find("b").text.split("\n")[1])
		
		check_site_get = requests.get(check_site, proxies={'http': item, 'https': item,}, allow_redirects=False,verify=False)
		check_site_code = check_site_get.status_code
		
		print("The site \"{}\" give status code of {} on the proxy {}".format(check_site, check_site_code, proxy_ip))
		
except requests.exceptions.ProxyError as e:
	print("Proxy Error")