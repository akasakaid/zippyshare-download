import os
import re
import sys
try:
	import click
	import requests
except ImportError:
	exit("# import error !")

#url = "https://www40.zippyshare.com/v/6gtKYEqj/file.html"
r = requests.Session()


# url jadi https://www40.zippyshare.com/d/6gtKYEqj/3693/lunar.php
def download(url):
	try:
		req = r.get(url)
		var_n = eval(re.search('var n = (.*?);',req.text).group(1))
		var_b = eval(re.search('var b = (.*?);',req.text).group(1))
		var_z = eval(re.search('var z = (.*?);',req.text).group(1))
		origin = re.search('https://(.*?)/',url).group(1)
		
		elemen = re.search('document.getElementById\(\'dlbutton\'\).href = \"(.*?)\" \+ \((.*?)\) \+ \"(.*?)\";',req.text)
		elemen = re.search('document.getElementById\(\'dlbutton\'\).href = "(.*?)"\+\((.*?)\)\+\"(.*?)\";',req.text)
		matematika = var_n + var_b + var_z - 3
		url_download = "https://" + origin + elemen.group(1) + str(matematika) + elemen.group(3)
		print("# redirect to browser !")
		click.launch(url_download)
		print(url_download)
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
