#!/usr/bin/python
#Subd0mains_Finder v2.1 - by @moradorex
#Python Subdomain searcher based of virustotal.com API

import requests
import sys
import getopt
import json

#DATA
domain = ''
api = ''
version = '2.1'

#OPTIONS
recursive = False
hosts = False
output = False


def usage():
	print("usage:")
	print("  Subd0mains_Finder.py [options] <domain>")
	print("\n  options:")
	print("    -t, --hosts \t\tShow in hosts file format, 127.0.0.1 <subdomain>")
	print("    -o <file>, --output <file> \tSave to file")
	print("    -v, --version \t\tShow version")
	print("    -h, --help \t\t\tShow this screen")
	print("\nPut your API key in the config.json file.")
	print("You can only enter one domain at a time. Get yours API key at:")
	print("  https://www.virustotal.com/gui/user/YOUR_USERNAME/apikey\n")
	sys.exit(2)


def getVirusTotal():
	params = {'apikey':api,'domain':domain}
	headers = {'User-Agent': 'Subd0mains_Finder/2.1'}
	response = requests.get('https://www.virustotal.com/vtapi/v2/domain/report', headers=headers, params=params)

	if(response.status_code == 400):
		print("Bad request. Your request was somehow incorrect. This can be caused by missing arguments or arguments with wrong values.")
		sys.exit(2)
	elif(response.status_code == 403):
		print("Forbidden. You don't have enough privileges to make the request. You may be doing a request without providing an API key or you may be making a request to a Private API without having the appropriate privileges.")
		sys.exit(2)
	elif(response.status_code == 201):
		print("Request rate limit exceeded. You are making more requests than allowed. You have exceeded one of your quotas (minute, daily or monthly). Daily quotas are reset every day at 00:00 UTC.")
		sys.exit(2)
	elif(response.json()['response_code']==0):
		print("Domain not found")
		sys.exit(2)

	return response.json()


def main():

	#DATA
	global api, domain

	#OPTIONS
	global recursive, hosts, output

	#GET API FROM CONFIG FILE
	#READ FILE
	Fconfig = open('config.json', 'r')
	data=Fconfig.read()

	#PARSE FILE
	obj = json.loads(data)
	api = str(obj['api'])

	if(api=="API_KEY" or api==""):
		print("\nAPI NOT FOUND")
		usage()

	#OPTIONS AND ARGUMENTS
	try:
		opts, args = getopt.getopt(sys.argv[1:], 'td:o:vh', ['hosts', 'domain=', 'output=', 'version', 'help'])
	except getopt.GetoptError:
		usage()

	## GET OPTIONS
	for opt, arg in opts:
		if opt in ('-t', '--hosts'):
			hosts = True

		elif opt in ('-o', '--output'):
			output = arg

		elif opt in ('-v', '--version'):
			print(version)
			sys.exit(2)

		elif opt in ('-h', '--help'):
			usage()

		else:
			usage()

	## GET DOMAIN
	try:
		domain = args[0]
	except Exception:
		usage()

	## ERROR IF NO API
	if(api == ''):
		usage()

	## OPEN FILE IF OUTPUT SELECTED
	if(output != False):
		file = open(output, 'w')

	## MAKE REQUEST
	req = getVirusTotal()
	for subdomain in req['subdomains']:
		if(hosts):
			if(output != False):
				file.write("127.0.0.1 " + subdomain + "\n")
				print("127.0.0.1 " + subdomain)

			else:
				print("127.0.0.1 " + subdomain)

		else:
			if(output != False):
				file.write(subdomain + "\n")
				print(subdomain)

			else:
				print(subdomain)

	## CLOSE FILE WHEN FINISHED
	if(output != False):
		print("\nSaved to file " + output)
		file.close()


if __name__ == "__main__":
    main()
