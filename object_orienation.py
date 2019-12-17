import os
import sys

def is_title(line):
	return ("#" in line and "=" not in line)

def update_dnsmasq():
	os.system("sudo systemctl restart dnsmasq")

class help:
	def script():
		sys.exit("""
===================================================================================================
This is the help message for my dns_edit script, this help function will show you
the correct sytnax to use the program.

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
		   will contain all the IPs at the end. The secondary dnsconfig file will not
		   change.

		   Example of usage:
		   Merge two files = python3 dns_edit.py -m -f1 main.txt -f2 combine.txt


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
			while line_counter < len(lines):
				line = lines[line_counter]
				if line.strip('\n') == str("#" + title): 
					found = True
					f.write(line)
					line_counter_2 = line_counter+1
					while "=" in lines[line_counter_2]:
						f.write(lines[line_counter_2].strip("#"))
						line_counter_2 += 1
					f.write("\n")
					line_counter = line_counter_2
				else:
					f.write(line)
				line_counter += 1
			if found == False:
				print("error, title not found, please check the input and try again")
			pass

	def uncomment_all(self):

		file = self.file
		with open(file, 'r') as f:
			lines = f.readlines()
		with open(file, 'w') as f:
			pass
		with open(file, 'a') as f:
			for line in lines:
				if not is_title(line):
					f.write(line.strip("#"))
				else:
					f.write(line)

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
						if "#" in lines[line_counter_2]:
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
				print("Title Couldn't be found, please check the usage and try again")

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
				elif "#" in line:
					f.write(line)
				elif line == "\n":
					f.write(line)
				else:
					f.write("#"+line)

class combine:

	def read_files(file1, file2):
		with open(file1, 'r') as f:
			file_string = f.read()
			line_array_1 = str(file_string).splitlines()
		with open(file2, 'r') as f:
			file_string2 = f.read()
			line_array_2 = str(file_string2).splitlines()
		return(line_array_1, line_array_2)

	def get_details(title, array):
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
		with open(file, 'w') as f:
			for name, entries in original_entries.items():
				f.write("\n" + name + "\n")
				for entry in entries:
					f.write(entry + "\n")
			f.write("\n")

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

	def full_add(self, title, address, server):
		file = self.file
		array_of_entries = add.make_array(self)
		array_to_add = []
		array_to_add.append(title)
		array_to_add.append(server)
		array_to_add.append(address)
		new_entry = {
					title:array_to_add
		}
		print(new_entry)
		combine.write_array_to_main(new_entry, array_of_entries, file)
		combine.remove_duplicates(file)

	def server_add(self, title, server):
		file = self.file
		array_of_entries = add.make_array()
		array_to_add = []
		array_to_add.append(title)
		array_to_add.append(server)
		new_entry = {
					title:array_to_add
		}
		print(new_entry)
		combine.write_array_to_main(new_entry, array_of_entries, file)
		combine.remove_duplicates(file)

	def address_add(self, title, address):
		file = self.file
		array_of_entries = add.make_array(self)
		array_to_add = []
		array_to_add.append(title)
		array_to_add.append(address)
		new_entry = {
					title:array_to_add
		}
		print(new_entry)
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
			sys.exit("title doesnt exist, when adding an entry that doesnt exist you should use entry adding")
		add.address_add(self, title, ip)
	
if ("-h") in sys.argv:
	help.script()

if sys.argv[2] == "-s" and sys.argv[3] == "-f" and sys.argv[4] != "" and sys.argv[5] == "-t" and sys.argv[6] != "":
	file = sys.argv[4]
	title = sys.argv[6]
	commenting = commenter(file)
	if sys.argv[1] == "-c":
		commenting.comment_single(title) 
	elif sys.argv[1] == "-u":
		commenting.uncomment_single(title)
	else:
		sys.exit("Incorrect Usage, please read the help document (-h) and try again")

elif sys.argv[2] == "-a" and sys.argv[3] == "-f" and sys.argv[4] != "":
	file = sys.argv[4]
	commenting = commenter(file)
	if sys.argv[1] == "-c":
		commenting.comment_all()
	elif sys.argv[1] == "-u":
		commenting.uncomment_all()

elif sys.argv[1] == "-m" and sys.argv[2] == "-f1" and sys.argv[3] != "" and sys.argv[4] == "-f2" and sys.argv[5] != "":
	file1 = sys.argv[3]
	file2 = sys.argv[5]
	combine.merge(file1, file2)
	combine.remove_duplicates(file1)

else:
	print("error")

