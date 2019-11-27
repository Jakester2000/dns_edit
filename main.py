import commenter, uncommenter, write_to_file, entry_adding, merging_file, deletion_of_entrys
import sys

server = ""
address = ""
args = sys.argv

def main():
	if len(args) < 2:
		sys.exit("Too few arguments. Run '-h' for help")
	else:
		handle_arguments(server, address)

def handle_arguments(server, address):
	''' [CODE REVIEW] Comment Title/Brief Description

	More description if needed

	Params:
		server: ...
		address: ...
	Returns:
	    (if application)
	Errors:
		Try/Catch exceptions noted here
	'''
	
	if "-h" in args:
		help()
	# [CODE REVIEW] 
	# There is another way to do this, may need to be more readable,
	# 	i.e. with --file
	if "-f" in args and argument_given("-f"):
		file = get_argument("-f")

	if "-t" in args and argument_given("-t"):
		title = get_argument("-t")

	if "-a"  in args and argument_given("-a"):
		address = get_argument("-a")

	if "-s" in args and argument_given("-s"):
		server = get_argument("-s")

	if "-u" in args:
		try:
			uncommenter.uncomment(file, title)
		except:
			sys.exit("No argument given.")

	elif "-c" in args:
		commenter.comment(file, title)

	elif "-w" in args:
	
		if not address and not server:
			sys.exit("Server or address not specified.")
		else:
			write_to_file.write(file, server, address)

	elif "-e" in args:
		if not address and not server:
			sys.exit("Server or address not specified.")
		else:
			entry_adding.add_entry(file, title, server, address)

	elif "-m" in args:
		files = []
		for arg in range(args.index("-m") + 1, len(args)):
			files.append(args[arg])
			
		try:
			line_array_1, line_array_2 = merging_file.read_files(files[0], files[1])
		except:
		 	sys.exit("Use -h to ") #[CODE REVIEW] ...to what?

		main_file = files[0]
		output = merging_file.compare(line_array_1, line_array_2)
		final = merging_file.write_array_to_main(output, line_array_1, main_file)

	elif "-d" in args:
		# [CODE REVIEW] Remove pointless whitespace like this
		try:
			index = int(get_argument("-i"))

		except:
			sys.exit("error, this is not a number")

		array_of_entries = deletion_of_entrys.read_file(file)
		deletion_of_entrys.delete_line(array_of_entries, index, file)

# [CODE REVIEW] These don't need comments, so don't worry
def get_argument(to_find):
	return args[args.index(to_find) + 1]

def argument_given(to_check):
	return True if args.index(to_check) != (len(args) - 1) else sys.exit("No argument given.")

def help():
	sys.exit('''=====================================================================================================
Commands -
-u uncomment = uncomment certain elements of the dnsconfig
-c comment = recomment certain elements of the dnsconfig
-w write_to_file = append new entries to the end of the config
-e entry adding = add an entry to an existing Title
-h Help-page = The command used to open the help-page
-d delete = deletes a specific line of the users choice, use with -i

Options -
-f file input = this is the file path of the config file you want to be edited
-t title =  declare the title of the website the dns will be altering
-s server = used with the write_to_file and entry_adding scripts to add a server under a title- example - /google.com/8.8.8.8
-a address = /google.com/192.165.24.2
-i index = provides the number of the line to delete with -d, 

Examples of how the software works -
	command: python3 main.py -u -f dnsconfig.txt -t Reddit
	command: python3 main.py -c -f dnsconfig.txt -t Twitter
	command: python3 main.py -w -f dnsconfig.txt -t bbc.co.uk -s /bbc.co.uk/8.8.8.8 -a /bbc.co.uk/162.52.101.28
	command: python3 main.py -e -f dnsconfig.txt -t Reddit -s /reddit.com/8.8.8.8
	command: python3 main.py -d -f dnsconfig.txt -i 5
=====================================================================================================''')



if __name__ == '__main__':
	main()

