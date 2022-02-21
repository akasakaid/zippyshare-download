import os
import re
import sys
try:
	import click
	import requests
except ImportError:
	exit("# import error !")

#url = "https://www48.zippyshare.com/v/8wuhRqsI/file.html"
r = requests.Session()


# url jadi https://www40.zippyshare.com/d/6gtKYEqj/3693/lunar.php
def download(url):
	try:
		req = r.get(url)
		open("hasil.html","wb").write(req.content)
		origin = re.search('https://(.*?)/',url).group(1)
		
		elemen = re.search('document.getElementById\(\'dlbutton\'\).href = \"(.*?)\" \+ \((.*?)\) \+ \"(.*?)\";',req.text)
		url_download = "https://" + origin + elemen.group(1) + str(eval(elemen.group(2))) + elemen.group(3)
		print("# redirect to browser !")
		click.launch(url_download)
	except ValueError:
		exit(f"# failed download from {url}")

def main():
	if len(sys.argv) < 2:
		exit("# how to use : python {} zippyshare_url".format(sys.argv[0]))
	download(sys.argv[1])

try:
	main()
except KeyboardInterrupt:
	exit()
