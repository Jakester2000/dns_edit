import commenter, uncommenter, writeToFile, entryAdding, mergingFile, deletionOfEntrys
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
		file = getArgument("-f")


	if "-t" in args and argumentGiven("-t"):
		title = getArgument("-t")


	if "-a"  in args and argumentGiven("-a"):
		address = getArgument("-a")


	if "-s" in args and argumentGiven("-s"):
		server = getArgument("-s")


	if "-u" in args:
		uncommenter.uncomment(file, title)


	elif "-c" in args:
		commenter.comment(file, title)


	elif "-w" in args:
		address = ""
		server = ""
		if not address and not server:
			sys.exit("Server or address not specified.")
		else:
			writeToFile.write(file, title, server, address)


	elif "-e" in args:
		if not address and not server:
			sys.exit("Server or address not specified.")
		else:
			entryAdding.addEntry(file, title, server, address)


	elif "-m" in args:
		files = []
		for arg in range(args.index("-m") + 1, len(args)):
			files.append(args[arg])
			
		try: 
			linearray1, linearray2 = mergingFile.readFiles(files[0], files[1])
		except:
			sys.exit("Use -h to ")

		MAINFILE = files[0]
		output = mergingFile.compare(linearray1, linearray2)
		final = mergingFile.WriteArrayToMain(output, linearray1, MAINFILE)

	elif "-d" in args:
	
		try:
			index = int(getArgument("-i"))

		except:
			sys.exit("error, this is not a number")

		arrayOfEntries = deletionOfEntrys.readFile(file)
		deletionOfEntrys.deleteline(arrayOfEntries, index, file)


def getArgument(to_find):
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
-d delete = deletes a specific line of the users choice, use with -i

Options -
-f file input = this is the file path of the config file you want to be edited
-t title =  declare the title of the website the dns will be altering
-s server = used with the writeToFile and entryAdding scripts to add a server under a title- example - /google.com/8.8.8.8
-a address = /google.com/192.165.24.2
-i index = provides the number of the line to delete with -d, 

Examples of how the software works -
	command: python3 main.py -u -f dnsconfig.txt -t Reddit
	command: python3 main.py -c -f dnsconfig.txt -t Twitter
	command: python3 main.py -w -f dnsconfig.txt -t bbc.co.uk -s /bbc.co.uk/8.8.8.8 -a /bbc.co.uk/162.52.101.28
	command: python3 main.py -e -f dnsconfig.txt -t Reddit -s /reddit.com/8.8.8.8
	command: python3 main.py -d -f dnsconfig.txt -i 5
=====================================================================================================''')


main()