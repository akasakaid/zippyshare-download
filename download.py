import os
import re
import argparse
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
		origin = re.search('https://(.*?)/',url).group(1)
		elemen = re.search('document.getElementById\(\'dlbutton\'\).href = \"(.*?)\" \+ \((.*?)\) \+ \"(.*?)\";',req.text)
		matematika = eval(elemen.group(2))
		url_download = "https://" + origin + elemen.group(1) + str(matematika) + elemen.group(3)
		print("# redirect to browser !")
		click.launch(url_download)
	except ValueError:
		exit(f"# failed download from {url}")

def main():
	parser = argparse.ArgumentParser(description="Zippyshare Downloader")
	parser.add_argument("--url",dest="url",help="url for download",required=True)
	args = parser.parse_args()
	download(args.url)

try:
	main()
except KeyboardInterrupt:
	exit()