import sys
def script():
	sys.exit("""
===================================================================================================
DNS_edit is a lightweight dns editting script for use alongside DNSMasq or any other DNS program
that stores IPs in the same manner

Functions:
Commenter (-c)     Comment either all (-a) or single entries of the dnsconfig
		   file, below are 2 examples of how to use the command, you always
		   need to include a file path (-f) and depending on the usage you
		   may need to include the title of the entry you want to comment out

		   Example of usage:
		   Comment all = python3 dns_edit.py -c -a -f dnsconfig.txt
	   	   Comment Single Entry = python3 dns_edit.py -c -f dnsconfig.txt -t BT

Uncommenter (-u)   Works similar to Commenter function, you can either Uncomment all (-a) 
		   or single entries of the dnsconfig file, below I have included
		   2 examples of how to use the Uncommneter function, Like-wise to the
		   commenter function, you always need to include a file path (-f) and 
		   depending on usage you may need to include the title of the entry you 
		   wish to uncomment

		   Example of usage:
		   Uncomment all = python3 dns_edit.py -u -a -f dnsconfig.txt
		   Uncomment Single Entry = python3 dns_edit.py -u -f dnsconfig.txt -t BT

Merge Files (-m)   The Merge function allows for 2 dnsconfig files to be combined into
		   one main file, the file you list first is the "main" file, the one which
		   will contain all the IPs at the end. The secondary dnsconfig file will
		   not change.

		   Example of usage:
		   Merge two files = python3 dns_edit.py -m -f1 main.txt -f2 combine.txt

Entry Adding (-a)  This function allows the user to add entries to the dnsmasq config file.
		   These entries must have a title but can either have a server, address or 
		   both. Below are examples of how to use this function.

		   Example of usage
		   full add = python3 dns_edit.py -a -f dnsconfig.txt -t title -s server -a address
		   server add = python3 dns_edit.py -a -f dnsconfig.txt -t title -s server
		   address add = python3 dns_edit.py -a -f dnsconfig.txt -t title -a address

Entry Remove (-r)  The entry removing function can be used to either remove a whole block of
		   Entries or alternatively remove select ips (either servers or addresses)
		   from an already existing entry inside the dnsmasq whitelist file.

		   Examples of usage:
		   Remove Entries: python3 dns_edit.py -r -f dnsconfig.txt -t Title
		   Remove IP: python3 dns_edit.py -r -f dnsconfig.txt -ip server=/bt.com/8.8.8.8

Rem.Duplicate (-rd)This function removes all duplicate entries in the file that holds the ips.
		   Below is an example of how the usage works:

		   Example of usage:
		   Remove Duplicates = python3 dns_edit.py -rd -f dnsconfig.txt

Restart (-restart) Restarts the DNSMasq service, meaning any changes made will be applied.
		   wll reply with "Done!" if the syntax is correct, else it will reply with a
		   suitable error message to inform the user of their incorrect syntax.
		   
		   Example of usage:
		   Restart DNSMasq = python3 dns_edit.py -restart
===================================================================================================
			""")