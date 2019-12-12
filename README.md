# Subd0mains_Finder
Python Subdomain finder based of virustotal.com API

Subd0mains_Finder is a scripts that uses the virustotal.com API, runs querys of domains and returns a subdomain list.
Querys return a maximun of a 100 subdomains and virustotal.com API has requests rates depending on the account type.
For the use of this script an API key is needed, if u don´t have a VirusTotal.com account create one, its free! 

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

Tested in Python3.7

### Dependencies
Install `requests` using pip:
```
$ pip install requests
```
Using the requirements.txt:
```
$ pip install -r requirements.txt
````

### Installation
Clone the repository
```
$ git clone https://github.com/moradorex/Subd0mains_Finder.git
```
Navigate to the repository
```
$ cd Subd0mains_Finder
```
Execute the script
```
$ python Subd0mains_Finder.py --help
```

## Usage

```
$ python Subd0mains_Finder.py --help

Usage:
Subd0mains_Finder.py  [options]  -a <your_api_key> <domain>
Subd0mains_Finder.py  [options]  --api <your_api_key> <domain>
  
Options:
-t --hosts			Show in hosts file format - 127.0.0.1	<subdomainsdomain>
-o --output <file_name>		Output to file
-v --version			Show version
-h --help			Show this screen
```
  
## Authors

* **moradorex** - *Initial work* - [moradorex](https://github.com/moradorex)
