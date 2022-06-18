import os
import re
import sys
try:
    import click
    import requests
except ImportError:
    exit("# import error !")

r = requests.Session()

def download(url):
	try:
		req = r.get(url)
		origin = re.search('https://(.*?)/',url).group(1)
		elemen = re.search('document.getElementById\(\'dlbutton\'\).href = \"(.*?)\" \+ \((.*?)\) \+ \"(.*?)\";',req.text)
		url_download = "https://" + origin + elemen.group(1) + str(eval(elemen.group(2))) + elemen.group(3)
		print("- redirect to browser !")
		click.launch(url_download)
	except ValueError:
		sys.exit(f"- failed download from {url}")
	except AttributeError:
		sys.exit("- failed download file not found !")

def main():
	if len(sys.argv) < 2:
		print()
		print("- input url zippyshare !")
		url_download = input('- url : ')
	else:
		url_download = sys.argv[2]
	download(url_download)

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		sys.exit()
