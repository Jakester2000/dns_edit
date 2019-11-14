import commenter, uncommenter, writeToFile, helpScript, entryAdding
import sys

args = sys.argv



def main():
	if len(args) < 2:
		sys.exit("Too few arguments. Run '-h' for help")
	else:
		handleArguments()



def handleArguments():
	
	if "-h" in args:
		help()


	if "-f" in args and argumentGiven("-f"):
		file = getIndex("-f")


	if "-t" in args and argumentGiven("-t"):
		title = getIndex("-t")


	if "-a"  in args and argumentGiven("-a"):
		address = getIndex("-a")


	if "-s" in args and argumentGiven("-s"):
		server = getIndex("-s")



	if "-u" in args:
		uncommenter.uncomment(file, title)


	elif "-c" in args:
		commenter.comment(file, title)


	elif "-w" in args:
		if not address and not server:
			sys.exit("Server or address not specified.")
		else:
			writeToFile.write(file, title, server, address)


	elif "-e" in args:
		if not address and not server:
			sys.exit("Server or address not specified.")
		else:
			entryAdding.addEntry(file, title, server, address)
	



def getIndex(to_find):
	return args[args.index(to_find) + 1]



def argumentGiven(to_check):
	return True if args.index(to_check) != (len(args) - 1) else sys.exit("No argument given.")



def help():
	sys.exit('''=====================================================================================================
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
				=====================================================================================================''')


main()