# project2

Subdomain and Directory Scanner: 
This script takes a domain name as input, checks if it is a valid URL and prompts for a secure protocol if one is not provided. It then performs a series of HTTP GET requests to a list of subdomains and directories using a provided dictionary. The results of each request are written to separate output files in the "outputs" directory.


Usage: 
To run this script, execute the following command:
python3 test_script.py http://www.example.com

Arguments:
domainName: The name of the domain to scan.
Dependencies


This script requires the following Python packages:
argparse
re
requests


This script writes the results of each HTTP GET request to separate output files:
outputsubdomains.bat: Contains the URLs of any discovered subdomains.
outputdirectories.bat: Contains the URLs of any discovered directories.
Dictionary Files


This script requires two dictionary files, located in the root directory of the project:
subdomains_dictionary.bat: A list of subdomains to check.
dirs_dictionary.bat: A list of directories to check.


These files can be modified to include your own lists of subdomains and directories.