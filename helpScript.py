
def Help():

	print('''
=====================================================================================================
Commands -
	-u uncomment = uncomment certain elements of the dnsconfig
	-c comment = recomment certain elements of the dnsconfig
	-w writeToFile = append new entries to the end of the config
	-e entry adding = add an entry to an existing Title
	-h Help-page = The command used to open the help-page

	Options -
	-f file input = this is the file path of the config file you want to be edited
	-t title =  declare the title of the website the dns will be altering
	-s server = used with the writeToFile and entryAdding scripts to add a server under a title- example - /google.com/8.8.8.8
	-a address = /google.com/192.165.24.2

	Examples of how the software works -
		command: python3 main.py -u -f dnsconfig.txt -t Reddit
		command: python3 main.py -c -f dnsconfig.txt -t Twitter
		command: python3 main.py -w -f dnsconfig.txt -t bbc.co.uk -s /bbc.co.uk/8.8.8.8 -a /bbc.co.uk/162.52.101.28
		command: python3 main.py -e -f dnsconfig.txt -t Reddit -s /reddit.com/8.8.8.8
=====================================================================================================
		''')
