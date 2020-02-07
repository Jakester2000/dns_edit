import sys
NEW_LINE_CHAR = "\n"
HASH_CHAR = "#"
COMMENT_CHAR = "*"

class deleting:
	#creates a class called deleting
	def __init__(self, file):
		"""
		This function is ran automatically whenever an instance of this class is created
		(Whenever an object is created)
		it sets the variable self.file to equal to the file path passed
		"""
		self.file = file

	def is_title(self, line):
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

	def rem_title(self, title):
		"""
		This function removes the title passed from the whitelist file, along with all the ips
		and comments associated with the title.
		Arguments:
		@title: a string that corrosponds to the title to be removed from the whitelist file
		"""
		file = self.file
		try:
			with open(file, 'r') as f:
				lines = f.readlines()
		except:
			sys.exit("File not found, please check the filepath and try again")
		top_title_found = False
		bottom_title_found = False

		for line in lines:
			if line.strip(NEW_LINE_CHAR) == HASH_CHAR + title:
				top_pointer = lines.index(line)
				top_title_found = True

			elif top_title_found and self.is_title(line) and not bottom_title_found:
				bottom_pointer = lines.index(line)
				bottom_title_found = True

			elif top_title_found and bottom_title_found:
				pass
		
		if top_title_found and not bottom_title_found:
			print("Title was at bottom of conf file")
			with open(file, "w+") as f:
				for counter in range(0, top_pointer):
					f.write(lines[counter])

		elif top_title_found and bottom_title_found:
			print("Title was not at bottom of conf file")
			with open(file, "w+") as f:
				for counter in range(0, top_pointer):
					f.write(lines[counter])
				counter = 0

				for counter in range(bottom_pointer, len(lines)):
					f.write(lines[counter])
					
		elif not top_title_found:
			sys.exit("Title couldnt be found, please try again")
		
	def rem_single(self, rem_string):
		"""
		This function removes a single IP from the whitelist file declared when an instance of the class
		was created
		The rem_string has to match a line in the whitelist file, else it will return an error message and stop the
		execution of the rest of the code to prevent any breakages
		Arguments:
		@rem_string: The string passed by the user to get removed
		"""
		file = self.file
		try:
			with open(file, 'r') as f:
				lines = f.readlines()
		except:
			sys.exit("File not found, please check the filepath and try again")
		string_found = False
		with open(file, "w+") as f:
			for line in lines:
				temp_line = line.strip(NEW_LINE_CHAR)
				if temp_line == rem_string or temp_line[1:] == rem_string:
					string_found = True
					pass
				else:
					f.write(line)
			if string_found:
				print("String successfully found and removed")
			else:
				sys.exit("Error, string not found, check the input and try again")