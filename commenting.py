import sys
HASH_CHAR = "#"
NEW_LINE_CHAR = "\n"
COMMENT_CHAR = "*"
FORCE_CHAR = "~"

def is_force(line):
	"""
	This function checks if the chosen title declares that the entry is of importance
	Importance can be assumed if the title includes the force character ("~")

	Arguments:
	@line: a string that is checked if it matches the criteria for being a title AND being of imporance
	
	Returns:
	True: if string is a title AND is of importance
	False: if string is either not a title or not of importance or both
	"""
	return (is_title(line) and FORCE_CHAR in line)

def is_title(line):
	"""
	This function checks if the line passed meets the criteria to be a title,
	the criteria it checks for is if a line starts with a Hash ("#") and that it
	doesnt include an equals sign ("="). This distinguishes between an IP and a Title

	Arguments:
	@line: a string that is checked if it matches the criteria for being a title
	
	Returns:
	True: if string is a title
	False: if string is not a title
	"""
	return (line.startswith(HASH_CHAR) and "=" not in line and COMMENT_CHAR not in line)

def is_comment(line):
	"""
	This function checks if the line passed meets the criteria to be a comment,
	the criteria it checks for is if a line starts with a hash and if the line contains
	the comment character ("#")
	Arguments:
	@line: a string that is checked if it matches the criteria for being a comment
	
	Returns:
	True: if string is a comment
	False: if string is not a comment
	"""
	return (line.startswith(HASH_CHAR) and COMMENT_CHAR in line)

def is_address(line):
	"""
	This function checks if the line passed meets the criteria to be an address,
	the criteria it checks for is if the line contains and equals ("=") and a dot (".")
	Arguments:
	@line: a string that is checked if it matches the criteria for being an address
	
	Returns:
	True: if string is an address
	False: if string is not an address
	"""
	return ("=" in line and "." in line)

class commenter:
	#Creates a class called commenter

	def __init__(self, file):
		"""
		This function is ran automatically whenever an instance of this class is created
		(Whenever an object is created)
		it sets the variable self.file to equal to the file path passed
		"""
		self.file = file

	def file_exists(self):
		"""
		This function checks that the file exists. If the file does exist it then creates a string called lines
		Returns:
		lines: if the file exists the contents are returned as a string
		"""
		file = self.file
		try:
			with open(file, 'r') as f:
				lines = f.readlines()
			return(lines)
		except:
			sys.exit("File not found, please check the filepath and try again")
            
	def starts_with_hash(self, string_to_check):
		"""
		This function checks if the passed string starts with a hash
		Returns:
		@True: if line does start with a hash
		@False: if line does not start with a hash
		"""
		return(string_to_check.startswith(HASH_CHAR))

	def clear_file(self):
		"""
		This function clears the file in the file-path that was passed when the object was created
		"""
		file = self.file
		with open(file, 'w') as f:
			pass

	def rewrite_original(self, lines):
		"""
		This function will rewrite the array lines back into the original file path
		Arguments:
		@lines: an array of the original contents from the file
		"""
		file = self.file
		with open(file, 'a') as f:
			f.writelines(lines)

	def uncomment_single(self, title, force_enabled):
		"""
		this function is called when the user wants to uncomment a single entry in the whitelist file
		it works by finding the location of the title, the location of the next title below the title given
		a for loop is iterated starting from the location of the title in the array, and ends when the next title
		is found or when it reaches the bottom of the file.
		it doesnt however uncomment titles, or comments as these are meant to stay commented
		if a title is found but is of importance (i.e has a ~) then it checks the force_enabled variable to see
		whether the uncomment is authorised
		Arguments:
		@title: A string that implies which entry needs to be uncommented
		@force_enabled: A boolean variable that shows whether the user has granted force permissions
		"""
		file = self.file
		title_found = False
		next_title_found = False
		position_of_title = 0
		lines = self.file_exists()
		if self.starts_with_hash(title):
			title = title[1:]
		self.clear_file()
		
		with open(file, 'a') as f:
			for line in lines:
				temp_line = line.strip(NEW_LINE_CHAR).strip(HASH_CHAR)
				if title_found:
					break
				if temp_line == title + FORCE_CHAR:
					if force_enabled == False:
						f.close()
						self.clear_file()
						self.rewrite_original(lines)
						sys.exit("Title found but is of importance, therefore -force needed to elevate command")
					else:
						f.write(line)
						force_enabled = False
						title_found = True
						position_of_title = lines.index(line)
						break

				if temp_line == title:
					f.write(line)
					title_found = True
					position_of_title = lines.index(line)
				else:
					f.write(line)
					
			if not title_found:
				sys.exit("Title couldnt be found, please check the title entry and try again")

			# This is the bit that uncomments the servers
			for linecounter in range(position_of_title + 1, len(lines)):
				if next_title_found:
					break
				if is_comment(lines[linecounter].strip(NEW_LINE_CHAR)):
					f.write(lines[linecounter])
				elif is_title(lines[linecounter]):
					next_title_found = True
					next_title_location = linecounter
				else:
					f.write(lines[linecounter].strip(HASH_CHAR))

			if not next_title_found:
				sys.exit("removed hashes correctly, title was at the bottom of the conf file")
				
			for linecounter in range(next_title_location, len(lines)):
				f.write(lines[linecounter])
			sys.exit(title + " has been uncommented successfully")

	def uncomment_all(self, full_permisions):
		"""
		This function is called when the user wants to uncomment all entries in the whitelist file,
		Firstly, uses the function file_exists() to create an array called "lines"
		It then uses iteration to loop through the array of text from the file, and if the line is not a 
		comment or a title then it removes the hash from the beggining of the line
		The function needs to be passed a boolean value to represent whether full permisions have been
		granted.
		Arguments:
		@full_permisions: True if all permissions have been granted
						  False if all permissions have not been granted
		"""
		file = self.file
		force_flag = False
		lines = self.file_exists()
		if not full_permisions:
			self.clear_file()
			with open(file, 'a') as f:
				for line in lines:
					if force_flag:
						f.write(line)
						if is_title(line):
							force_flag = False
							pass
			
					elif not is_title(line) and not is_comment(line):
						if line.startswith(HASH_CHAR):
							f.write(line[1:])
						else:
							f.write(line)
					else:
						if is_force(line):
							print("found force: " + line)
							force_flag = True
							f.write(line)
						else:
							f.write(line)
			print("Done!")
		else:
			with open(file, 'w') as f:
				pass
			with open(file, 'a') as f:
				for line in lines:
					if not is_title(line) and not is_comment(line):
						if line.startswith(HASH_CHAR):
							f.write(line[1:])
						else:
							f.write(line)
					else:
						f.write(line)
			print("Done!")

	def comment_single(self, title, force_enabled):
		"""
		this function is called when the user wants to comment a single entry in the whitelist file
		it works by finding the location of the title, the location of the next title below the title given
		a for loop is iterated starting from the location of the title in the array, and ends when the next title
		is found or when it reaches the bottom of the file.
		it doesnt however comment titles, or comments as these are already commented
		if a title is found but is of importance (i.e has a "~") then it checks the force_enabled variable to see
		whether the comment process is authorised
		Arguments:
		@title: A string that implies which entry needs to be commented
		@force_enabled: A boolean variable that shows whether the user has granted force permissions
		"""
		print("this far")
		file = self.file
		title_found = False
		next_title_found = False
		position_of_title = 0
		lines = self.file_exists()
		if self.starts_with_hash(title):
			title = title[1:]
		self.clear_file()
		
		with open(file, 'a') as f:
			for line in lines:
				temp_line = line.strip(NEW_LINE_CHAR).strip(HASH_CHAR)
				if title_found:
					break
				if temp_line == title + FORCE_CHAR:
					if force_enabled == False:
						f.close()
						self.clear_file()
						self.rewrite_original(lines)
						sys.exit("Title found but is of importance, therefore -force needed to elevate command")
					else:
						f.write(line)
						force_enabled = False
						title_found = True
						position_of_title = lines.index(line)
						break

				if temp_line == title:
					f.write(line)
					title_found = True
					position_of_title = lines.index(line)
				else:
					f.write(line)
					
			if not title_found:
				sys.exit("Title couldnt be found, please check the title entry and try again")

			# This is the bit that comments the servers
			for linecounter in range(position_of_title + 1, len(lines)):
				if next_title_found:
					break
				if is_comment(lines[linecounter].strip(NEW_LINE_CHAR)):
					f.write(lines[linecounter])
				elif is_title(lines[linecounter]):
					next_title_found = True
					next_title_location = linecounter
				else:
					if lines[linecounter] == NEW_LINE_CHAR:
						f.write(NEW_LINE_CHAR)
					elif not lines[linecounter].startswith(HASH_CHAR):
						f.write(HASH_CHAR + lines[linecounter])
					else:
						f.write(lines[linecounter])

			if not next_title_found:
				sys.exit("added hashes correctly, title was at the bottom of the conf file")
				
			for linecounter in range(next_title_location, len(lines)):
				f.write(lines[linecounter])
			sys.exit(title + " has been commented successfully")
				
	def comment_all(self, full_permisions):
		"""
		This function is called when the user wants to comment all entries in the whitelist file,
		Firstly, uses the function file_exists() to create an array called "lines"
		It then uses iteration to loop through the array of text from the file, and if the line is not a 
		comment or a title then it adds the hash from the beggining of the line, but first ensuring it doesnt already start with a hash
		The function needs to be passed a boolean value to represent whether full permisions have been
		granted.
		Arguments:
		@full_permisions: True if all permissions have been granted
						  False if all permissions have not been granted
		"""
		file = self.file
		force_flag = False
		lines = self.file_exists()
		if not full_permisions:
			self.clear_file()
			with open(file, 'a') as f:
				for line in lines:
					if force_flag:
						f.write(line)
						if is_title(line):
							force_flag = False
							pass
			
					elif not is_title(line) and not is_comment(line):
						if line == NEW_LINE_CHAR:
							f.write(NEW_LINE_CHAR)
						elif not line.startswith(HASH_CHAR):
							f.write(HASH_CHAR + line)
						else:
							f.write(line)
					else:
						if is_force(line):
							print("found force: " + line)
							force_flag = True
							f.write(line)
						else:
							f.write(line)
			print("Done!")
		else:
			with open(file, 'w') as f:
				pass
			with open(file, 'a') as f:
				for line in lines:
					if not is_title(line) and not is_comment(line) and line != NEW_LINE_CHAR:
						if not self.starts_with_hash(line):
							f.write(HASH_CHAR + line)
						else:
							f.write(line)
					else:
						f.write(line)
			print("Done!")
