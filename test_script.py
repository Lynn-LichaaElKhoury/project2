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
    

