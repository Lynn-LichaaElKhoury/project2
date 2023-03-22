import re
import argparse
import requests

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

sub=open ("./inputsubdomains.bat","r")
output=open ("./outputs/outputsubdomains.bat","w")

with sub as l:
    sd=l.readline()
    while(l):
        http=re.match(r"https?:\/\/",sd.rstrip())
        temp=re.sub(r"https?:\/\/www\.","", sd)
        newURL= http+sd+"."+temp
        try:
            exist=requests.get(newURL)
            output.write(newURL+"\n")
        except:
            pass

        sd=l.readline()
        