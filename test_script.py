import re
import argparse
import requests
from urllib.request import urlopen

args = argparse.ArgumentParser()
args.add_argument("domainName", help="'domain name")
domain=getattr(args.parse_args(), "domainName")


if not re.match(r"^https?:\/\/", domain):
    secure = input("protocol secure ? (yes or no)")
    if secure.lower() == "yes" :
        domain = "https://"+domain
    elif secure.lower() == "no":
        domain = "http://"+domain
    
exits=requests.get(domain)

try:
    exists=requests.get(domain)
except:
    print("enter a domain that exists:")
    exit()

sub=open ("./subdomains_dictionary.bat","r")
output=open ("./outputs/outputsubdomains.bat","w")

trailing_spaces = r'^\s+|\s+$|[^a-zA-Z0-9\s]'

with sub as l:
    sd=l.readline()
    while(l):
        nospaces = re.sub(trailing_spaces, "", sd)
        http=re.match(r"https?:\/\/",nospaces)
        temp=re.sub(r"https?:\/\/www\.","", nospaces)
        newURL= http+nospaces+"."+temp
        try:
            exist=requests.get(newURL)
            output.write(newURL+"\n")
        except:
            pass

        sd=l.readline()
        

dir=open("./dirs_disctionary.bat","r")
outputd=open("./outputs/outputdirectories","w")

with dir as l:
    d= l.readline()
    while (d):
        nspaces=re.sub(trailing_spaces,"",d)
        http=re.match(r"https?:\/\/",nospaces)
        temp=re.sub(r"https?:\/\/www\.","", nospaces)
        newURL= http+nospaces+"."+temp
        try:
            exist = requests.get(newURL)
            outputd.write(newURL+"\n")
        except:
            pass
        d = l.readline()
    
try:
    html = urlopen(domain).read().decode()
    f_output = open("./Output/files_output.bat", "w")

    link = r'<a\s+(?:[^>]*?\s+)?href="([^"]*)"'
    matches = re.findall(link, html)
    for link in list(matches):
        f_output.write(link)
except:
    print("Forbidden access")
