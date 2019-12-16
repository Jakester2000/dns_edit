import os
import sys

def is_title(line):
	return ("#" in line and "=" not in line)

def update_dnsmasq():
	os.system("sudo systemctl restart dnsmasq")

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
		temp_array = add.make_array(file)
		if str_to_check in temp_array:
			sys.exit("title already exists, when adding to an entry that already exists use add.ip")

	def make_array(self):
		file = self.file
		with open(file, 'r') as f:
			file_string = f.read()
			return str(file_string).splitlines()

	def full_add(self, title, address, server):
		file = self.file
		array_of_entries = add.make_array(file)
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
		array_of_entries = add.make_array(file)
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
		array_of_entries = add.make_array(file)
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
		add.presence_check(file, title)
		if server != "" and address != "":
			add.full_add(file, title, address, server)
		elif address != "":
			add.address_add(file, title, address)
			pass	
		elif server != "":
			add.server_add(file, title, server)
			pass
		else:
			print("Error, please check usage and try again")
			
	def ip_adding(self, title, ip):
		file = self.file
		if not title.startswith("#"):
			title = "#" + title
		temp_array = add.make_array(file)
		if not title in temp_array:
			sys.exit("title doesnt exist, when adding an entry that doesnt exist you should use entry adding")
		print("test")
	

commenting = commenter("test")
commenting.uncomment_all()



	
#add.ip_adding("test", "youtube", "asdasd")

#combine.merge("test", "compare")

#combine.remove_duplicates("test")

#update_dnsmasq()

# class Car():
# 	def __init__(self,color,doors,gears,speed):
# 		self.color = color
# 		self.doors = doors
# 		self.gears = gears
# 		self.speed = speed
# 	def crash(self):
# 		print("BANG"*self.speed)
# 	def changeSpeed(self,speed):
# 		self.speed = speed

# jakesCar = Car("black",5,5,120)

# jakesCar.crash()