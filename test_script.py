import re
import argparse
import requests

args = argparse.ArgumentParser()
args.add_argument("domainName", help="'domain name")
domain=getattr(args.parse_args(), "domainName")