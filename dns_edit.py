import os
import sys

hash_char = "#"
new_line_char = "\n"

def is_title(line):
	return ("#" in line and "=" not in line)

def update_dnsmasq():
	os.system("sudo systemctl restart dnsmasq")

if sys.argv[1] == "-restart":
	update_dnsmasq()
	print("Dnsmasq updated! Make sure you flush DNS on the host to fully apply changes")

class help:
	def script():
		sys.exit("""
===================================================================================================
DNS_edit is a lightweight dns editting script for use alongside DNSMasq or any other DNS program
that stores IPs in the same manner

Functions:
Commenter (-c)     Comment either all (-a) or single entries (-s) of the dnsconfig
		   file, below are 2 examples of how to use the command, you always
		   need to include a file path (-f) and depending on the usage you
		   may need to include the title of the entry you want to comment out

		   Example of usage:
		   Comment all = python3 dns_edit.py -c -a -f dnsconfig.txt
	   	   Comment Single Entry = python3 dns_edit.py -c -s -f dnsconfig.txt -t BT

Uncommenter (-u)   Works similar to Commenter function, you can either Uncomment all (-a) 
		   or single entries (-s) of the dnsconfig file, below I have included
		   2 examples of how to use the Uncommneter function, Like-wise to the
		   commenter function, you always need to include a file path (-f) and 
		   depending on usage you may need to include the title of the entry you 
		   wish to uncomment

		   Example of usage:
		   Uncomment all = python3 dns_edit.py -u -a -f dnsconfig.txt
		   Uncomment Single Entry = python3 dns_edit.py -u -s -f dnsconfig.txt -t BT

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

Rem.Duplicate (-r) This function removes all duplicate entries in the file that holds the ips.
		   Below is an example of how the usage works:

		   Example of Usage:
		   Remove Duplicates = python3 dns_edit.py -r -f dnsconfig.txt

Restart (-restart) Restarts the DNSMasq service, meaning any changes made will be applied.
		   wll reply with "Done!" if the syntax is correct, else it will reply with a
		   suitable error message to inform the user of their incorrect syntax.
		   
		   Example of usage:
		   Restart DNSMasq = python3 dns_edit.py -restart
===================================================================================================
			""")

class commenter:

	def __init__(self,file):
		self.file = file

	def uncomment_single(self, title):
		file = self.file
		found = False
		with open(file, 'r') as f:
			lines = f.readlines()
		with open(file, 'w') as f:
			pass
		with open(file, 'a') as f:
			line_counter = 0
			if title.startswith("#"):
				title = title[1:]
			while line_counter < len(lines):
				line = lines[line_counter]
				if line.strip('\n') == str("#" + title): 
					found = True
					f.write(line)
					line_counter_2 = line_counter+1
					while "=" in lines[line_counter_2]:
						if lines[line_counter_2].startswith("#"):
							f.write(lines[line_counter_2][1:])
						else:
							f.write(lines[line_counter_2])
						line_counter_2 += 1
					f.write("\n")
					line_counter = line_counter_2
				else:
					f.write(line)
				line_counter += 1
			if found == False:
				print("Title " + title + " could not be found, please check the usage and try again")
			else:
				print("Done!")

	def uncomment_all(self):

		file = self.file
		with open(file, 'r') as f:
			lines = f.readlines()
		with open(file, 'w') as f:
			pass
		with open(file, 'a') as f:
			for line in lines:
				if not is_title(line):
					if line.startswith("#"):
						f.write(line[1:])
					else:
						f.write(line)
				else:
					f.write(line)
		print("Done!")

	def comment_single(self, title):
		file = self.file
		found = False
		with open(file, 'r') as f:
			lines = f.readlines()
		with open(file, 'w') as f:
			pass
		with open(file, 'a') as f:
			line_counter = 0
			while line_counter < len(lines):
				line = lines[line_counter]
				if line.strip('\n') == str("#" + title): 
					found = True
					f.write(line)
					line_counter_2 = line_counter+1
					while "=" in lines[line_counter_2]:
						if lines[line_counter_2].startswith("#"):
							f.write(lines[line_counter_2])
						else:
							f.write("#" + lines[line_counter_2])
						line_counter_2 += 1
					f.write("\n")
					line_counter = line_counter_2
				else:
					f.write(line)
				line_counter += 1
			if found == False:
				print("Title " + title + " could not be found, please check the usage and try again")
			else:
				print("Done!")

	def comment_all(self):
		file = self.file
		with open(file, 'r') as f:
			lines = f.readlines()
		with open(file, 'w') as f:
			pass
		with open(file, 'a') as f:
			for line in lines:
				if is_title(line):
					f.write(line)
				elif line.startswith("#"):
					f.write(line)
				elif line == "\n":
					f.write(line)
				else:
					f.write("#"+line)
		print("Done!")

class combine:

	def read_files(file1, file2):
		with open(file1, 'r') as f:
			file_string = f.read()
			line_array_1 = str(file_string).splitlines()
		with open(file2, 'r') as f:
			file_string2 = f.read()
			line_array_2 = str(file_string2).splitlines()
		return(line_array_1, line_array_2)

	def get_details(self, title, array):
		current_title = ""
		output = []
		for i in range(array.index(title), len(array) - 1):
			if is_title(array[i]) and array[i] != title:
				break
			elif array[i] != "":
				output.append(array[i])
		return output

	def make_dictionary(line_array_1):
		dictionary_of_entries = {}
		for line in line_array_1:
			if is_title(line):
				dictionary_of_entries[line] = combine.get_details(line, line_array_1)
		return dictionary_of_entries

	def write_array_to_main(entries_to_add, line_array_1, file):
		original_entries = combine.make_dictionary(line_array_1)
		for entries in entries_to_add:
			if entries in original_entries:
				original_entries[entries] = entries_to_add[entries] + original_entries[entries]
			else:
				original_entries[entries] = entries_to_add[entries]
		blockAll = False
		commented = False
		with open(file, 'w') as f:
			for name, entries in original_entries.items():
				if "block-all" in name:
					blockAll = True
					if entries[1].startswith("#"):
						commented = True
					pass
				else:
					f.write("\n" + name + "\n")
					for entry in entries:
						f.write(entry + "\n")
			f.write("\n")
			if blockAll:
				if commented:
					f.write("#block-all\n#address=127.0.0.1\n\n")
				else:
					f.write("#block-all\naddress=127.0.0.1\n\n")

	def merge(main_file, to_add):
		files = []
		files.append(main_file)
		files.append(to_add)
		line_array_1, line_array_2 = combine.read_files(files[0], files[1])
		dictionary_of_entries = combine.make_dictionary(line_array_2)
		final = combine.write_array_to_main(dictionary_of_entries, line_array_1, main_file)

	def remove_duplicates(file):
		duplicate_found = False
		index_loop_1 = 0
		index_loop_2 = 0
		with open(file, 'r') as f:
			lines = f.readlines()
		for line in lines:
			index_loop_2 = 0
			if line == "\n":
				pass
			else:	
				for line_to_check in lines:
					if line_to_check == "\n":
						pass
					elif index_loop_1 == index_loop_2:
						pass
					else:
						if line in line_to_check or "#" + line in line_to_check:
							duplicate_found = True
							if index_loop_2 > index_loop_1:
								lines.pop(index_loop_2)
							else:
								lines.pop(index_loop_1)
							index_loop_2 -= 1
					index_loop_2 += 1
			index_loop_1 += 1
		if duplicate_found == False:
			print("Duplicate not found, check entries and try again")
		with open(file, "w+") as f:
			f.writelines(lines)
		print("Done!")

class add:

	def __init__(self,file):
		self.file = file

	def presence_check(self, str_to_check):
		file = self.file
		temp_array = add.make_array(self)
		if str_to_check in temp_array:
			sys.exit("title already exists, when adding to an entry that already exists use add.ip")

	def make_array(self):
		file = self.file
		with open(file, 'r') as f:
			file_string = f.read()
			return str(file_string).splitlines()

	def full_add(self, title, server, address):
		file = self.file
		if not hash_char in title:
			title = hash_char + title
		
		address = address
		server = server
		array_of_entries = add.make_array(self)
		array_to_add = []
		array_to_add.append(server)
		array_to_add.append(address)
		array_to_add.append(title)
		new_entry = {
					title:array_to_add
		}
		combine.write_array_to_main(new_entry, array_of_entries, file)
		combine.remove_duplicates(file)


	def server_add(self, title, server):
		file = self.file
		title = hash_char + title
		array_of_entries = add.make_array(self)
		array_to_add = []
		array_to_add.append(title)
		array_to_add.append(server)
		new_entry = {
					title:array_to_add
		}
		combine.write_array_to_main(new_entry, array_of_entries, file)
		combine.remove_duplicates(file)

	def address_add(self, title, address):
		file = self.file
		array_of_entries = add.make_array(self)
		array_to_add = []
		array_to_add.append(address)
		array_to_add.append(title)
		new_entry = {
					title:array_to_add
		}
		combine.write_array_to_main(new_entry, array_of_entries, file)
		combine.remove_duplicates(file)
		pass

	def entry_adding(self, title, address, server):
		file = self.file
		if not title.startswith("#"):
			title = "#" + title
		add.presence_check(self, title)
		if server != "" and address != "":
			add.full_add(self, title, address, server)
		elif address != "":
			add.address_add(title, address)
			pass	
		elif server != "":
			add.server_add(title, server)
			pass
		else:
			print("Error, please check usage and try again")
			
	def ip_adding(self, title, ip):
		file = self.file
		if not title.startswith("#"):
			title = "#" + title
		temp_array = add.make_array(self)
		if not title in temp_array:
			temp_array.append(title)
		add.address_add(self, title, ip)


#below controls all the arguments the user enters, different if statements for different classes and functions
	
#runs the help script if user enters "-h"
if ("-h") in sys.argv:
	help.script()

if len(sys.argv) < 3:
	sys.exit()

if sys.argv[1] == "-c" and sys.argv[2] == "-f" and sys.argv[3] != "" and sys.argv[4] == "-t" and sys.argv[5] != "":
	file = sys.argv[3]
	commenting = commenter(file)
	for i in range(5, len(sys.argv)):
		print(sys.argv[i])
		commenting.comment_single(sys.argv[i])
	print("Remember to use the restart command to apply changes")
	sys.exit()
	

if sys.argv[1] == "-u" and sys.argv[2] == "-f" and sys.argv[3] != "" and sys.argv[4] == "-t" and sys.argv[5] != "":
	file = sys.argv[3]
	commenting = commenter(file)
	for i in range(5, len(sys.argv)):
		print(sys.argv[i])
		commenting.uncomment_single(sys.argv[i])
	print("Remember to use the restart command to apply changes")
	sys.exit()








#If the user chooses either commenter or uncommenter ALL this if statement is ran
elif sys.argv[2] == "-a" and sys.argv[3] == "-f" and sys.argv[4] != "":
	file = sys.argv[4]
	commenting = commenter(file)
	if sys.argv[1] == "-c":
		commenting.comment_all()
		print("Remember to use the restart command to apply changes")
	elif sys.argv[1] == "-u":
		commenting.uncomment_all()
		print("Remember to use the restart command to apply changes")

#If the user chooses the merge file function this if statement is ran
elif sys.argv[1] == "-m" and sys.argv[2] == "-f1" and sys.argv[3] != "" and sys.argv[4] == "-f2" and sys.argv[5] != "":
	file1 = sys.argv[3]
	file2 = sys.argv[5]
	combine.merge(file1, file2)
	combine.remove_duplicates(file1)
	print("Remember to use the restart command to apply changes")

#If the user chooses to add entries to the file this statement is ran
elif sys.argv[1] == "-a" and sys.argv[2] == "-f" and sys.argv[3] != "":
	file = sys.argv[3]
	adding_object = add(file)
	if len(sys.argv) == 8:
		if sys.argv[4] == "-t" and sys.argv[5] != "" and sys.argv[6] != "" and sys.argv[7] != "":
			adding_object.ip_adding(sys.argv[5], sys.argv[7])
			print("Remember to use the restart command to apply changes")
	else:
		pass
	if len(sys.argv) == 10:
		if sys.argv[4] == "-t" and sys.argv[5] != "" and sys.argv[6] == "-s" and sys.argv[7] != "" and sys.argv[8] == "-a" and sys.argv[9] != "":
			adding_object.full_add(sys.argv[5], sys.argv[7], sys.argv[9])
			print("Remember to use the restart command to apply changes")
	else:
		pass
	
elif sys.argv[1] == "-r" and sys.argv[2] == "-f" and sys.argv[3] != "":
	combine.remove_duplicates(sys.argv[3])
	print("Remember to use the restart command to apply changes")

#if they dont enter any arguments an error output is produced
elif sys.argv[0] == "":
	print("error, check usage in -h and try again")

#if the syntax is incorrect then this else statement is ran
else:
	print("error, check usage in -h and try again")


