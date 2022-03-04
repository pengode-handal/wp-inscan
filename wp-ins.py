from colorama import Fore
b = '\033[1m'+Fore.LIGHTBLUE_EX
red = '\033[1m'+Fore.LIGHTRED_EX
g = '\033[1m'+Fore.LIGHTGREEN_EX
c = '\033[1m'+Fore.LIGHTCYAN_EX
w = '\033[1m'+Fore.LIGHTWHITE_EX
import requests, argparse
from bs4 import BeautifulSoup

def getUrl(url):
    urls = []
    with open(url, "r") as ufile:
        allurl = ufile.readlines()
        for i in range(len(allurl)):
            urls.append(allurl[i].strip('\n'))
        return urls

parse = argparse.ArgumentParser()
parse.add_argument('-u', '--url', help='Input site(with http/https)')
parse.add_argument('-f', '--file', help='scanning hash in the file')
args = parse.parse_args()

def inscan(url):
    try:
        r =requests.get(url+'/wp-admin/install.php')
        if 'Already Installed' in r.text:
            return w+url+red+' Not Vuln'
        elif r.status_code == 404:
            return red+'Not Found(check if site have path or site use wordpress)'
        else:
            return w+url+g+' Vuln'
    except:
        print(w+url+red+'Error')

if args.url:
    print(inscan(args.url))
elif args.file:
    url = getUrl(args.file)
    for i in url:
        print('======================')
        print(inscan(i))
else:
    print('Input argument')