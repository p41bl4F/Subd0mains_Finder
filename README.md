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
Or using the [requirements.txt](requirements.txt):
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

Configure the API key in the [config.json](config.json) file.


```
$ python Subd0mains_Finder.py --help

Usage:
Subd0mains_Finder.py  [options] <domain>
  
Options:
-t --hosts			Show in hosts file format, 127.0.0.1 <subdomain>
-o --output <file_name>		Output to file
-v --version			Show version
-h --help			Show this screen

Put your API key in the config.json file.
You can only enter one domain at a time. Get yours API key at:
  https://www.virustotal.com/gui/user/YOUR_USERNAME/apikey
```

## Example

Example using -o to export to a file
```
$ python Subd0mains_Finder.py -o output.txt google.com
clients3.google.com
mts1.google.com
ampcid.google.com
script.google.com
docs.google.com
surveys.google.com
shopping.google.com
plus.google.com
passwords.google.com
play.google.com
.
. (Some omitted for the example)
.
alt4-mtalk.google.com
mail.google.com
clients5.google.com
actions.google.com
dl-ssl.google.com
inbox.google.com
edu.google.com
smartlock.google.com
payments.google.com
fcmatch.google.com

Saved to file output.txt
```

Example using --hosts to print subdomains as hosts file format
```
$ python Subd0mains_Finder.py --hosts github.com

127.0.0.1	malsup.github.com
127.0.0.1	ppareit.github.com
127.0.0.1	central.github.com
127.0.0.1	api.github.com
127.0.0.1	help.github.com
127.0.0.1	www.github.com
127.0.0.1	yfujely.github.com
127.0.0.1	codeload.github.com
127.0.0.1	assets-cdn.github.com
127.0.0.1	noraesae.github.com
.
. (Some omitted for the example)
.
127.0.0.1	used.github.com
127.0.0.1	a-creative.github.com
127.0.0.1	here.github.com
127.0.0.1	2fraw.github.com
127.0.0.1	twbs.github.com
127.0.0.1	github.github.com
127.0.0.1	visualstudio.github.com
127.0.0.1	hawser.github.com
127.0.0.1	almeida.github.com
127.0.0.1	tsvensen.github.com
```
## Relevant Information
For info on the VirusTotal.com API go to:
* https://developers.virustotal.com/reference
* https://support.virustotal.com/hc/en-us/articles/115002100149-API

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

As this script uses virustotal.com API you also must respect VirusTotal's [Terms of Service](https://support.virustotal.com/hc/en-us/articles/115002145529-Terms-of-Service) and [Privacy Policy](https://support.virustotal.com/hc/en-us/articles/115002168385-Privacy-Policy)
  
## Authors

* **moradorex** - *Initial work* - [moradorex](https://github.com/moradorex)
