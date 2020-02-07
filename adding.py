import sys
HASH_CHAR = "#"
COMMENT_CHAR = "*"
NEW_LINE_CHAR = "\n"
class add:
	#creates a class called add

	def __init__(self,file):
		"""
		This function is ran automatically whenever an instance of this class is created
		(Whenever an object is created)
		it sets the variable self.file to equal to the file path passed
		"""
		self.file = file
	
	def clear_file(self):
		"""
		This function clears the file in the file-path that was passed when the object was created
		"""
		file = self.file
		with open(file, 'w') as f:
			pass

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

	def title_formating(self, title):
		"""
		This function makes sure the string passed (title)
		starts with a hash, if it doesnt start with a hash("#") then it adds one at the
		beginning of the string
		Arguments:
		@title: a string that is checked if it starts with a hash, and if it doesn't then one is added
		Returns:
		title: a string that always starts with a hash
		"""
		if not HASH_CHAR in title:
			title = HASH_CHAR + title
		return title

	def read_file(self):
		"""
		This function checks that the file exists. If the file does exist it then creates a string called file_string
		it then splits this string up into an array of lines
		Returns:
		array_file: if the file exists the contents are returned as an array of lines
		"""
		file = self.file
		try:
			with open(file, 'r') as f:
				file_string = f.read()
		except:
			sys.exit("Error, title not found")
		array_file = file_string.splitlines()
		return array_file

	def find_next_title(self, title, line_array, title_location):
		"""
		This function finds the location of the next title, to later be used as an upper bound in a for loop
		If there is no next title (I.E the title passed was at the bottom of the file) a boolean variable (bottom_of_file)
		is set to true
		Arguments:
		@title: a string which is an existing title in the file
		@line_array: an array of the text in the file, split up by new line characters
		@title_location: the location of the title passed
		Returns:
		next_title_location: the location of the next title, 0 If there is no next title (indicated by title_found boolean)
		title_found: set to true if there is a title below the one passed, else set to false if the title passed is at the bottom of the file
		"""
		title_found = False
		bottom_of_file = False
		for counter in range(title_location + 1, len(line_array)-1):
			line = line_array[counter]
			if self.is_title(line):
				next_title_location = counter
				title_found = True
				break
			else:
				pass

		if title_found == False:
			bottom_of_file = True
			return 0, bottom_of_file
		return next_title_location, bottom_of_file

	def get_details(self, title, line_array):
		"""
		This function gets the details relevent from the given title,
		for example, if the title BT was passed, all the relevent IPs below that title in the whitelist file
		will be returned in an array
		Arguments:
		@title: a string which is an existing title in the file
		@line_array: an array of the text in the file, split up by new line characters
		@title_location: the location of the title passed
		@next_title_location: the location of the next title in the array, 0 if next title is not found
		@bottom_of_file: boolean variable set to true if there is no next title
		Returns:
		array_of_entry: an array of all the details from a given title, for example [#bt, server=/bt.com/8.8.8.8, address=/bt.com/175.51.25.62]
		"""
		array_of_entry = []
		try:
			title_location = line_array.index(title)
		except:
			sys.exit("title not in file")
		next_title_location, bottom_of_file = self.find_next_title(title, line_array, title_location)
		if bottom_of_file == False:
			for i in range (title_location, next_title_location):
				if line_array[i] != "":
					array_of_entry.append(line_array[i])
		else:
			for i in range(title_location, len(line_array)):
				if line_array[i] != "":
					array_of_entry.append(line_array[i])
		return array_of_entry

	def make_dictionary(self, array_of_whole_file):
		"""
		Loops through the whole file array until it finds a title
		It then passes that title to the function "get_details" which returns an array
		this array is turned into a dictionary
		Arguments:
		@array_of_whole_file: all the text from the file, split into an array of lines
		@dictionary_of_entries: a dictionary that is created empty and then gets entries added to it
		Returns:
		dictionary_of_entries: once the dictionary contains each entry in the original file
		"""
		dictionary_of_entries = {}
		for line in array_of_whole_file:
			if self.is_title(line):
				dictionary_of_entries[line] = self.get_details(line, array_of_whole_file)
		return dictionary_of_entries

	def write_dictionary_back_to_file(self, dictionary_of_entries):
		"""
		this function is passed a dictionary, clears the original file, and then writes the dictionary
		with the correct formatting back to the original file
		arguments:
		@dictionary_of_entries: a dictionary that contains everything in the original file, but formatted in a dealable way
		"""
		file = self.file
		self.clear_file()
		with open(file, 'a') as f:
			f.write(NEW_LINE_CHAR)
			for entry in dictionary_of_entries:
				for line in dictionary_of_entries[entry]:
					f.write(line + NEW_LINE_CHAR)
				f.write(NEW_LINE_CHAR)
	
	def full_add(self, title, address, server):
		"""
		the function that runs the other functions in the correct order to ensure the full add
		is completed successfully
		>starts by reading the file
		>>it then ensures that the title is formatted correctly
		>>>it then gets the details about the title it got passed
		>>>>it then appends the address and server to the bottom of the array
		>>>>>it creates a dictionary of the main file
		>>>>>>it then loops through the dictionary titles, and adds it to a final dictionary
		>>>>>>>it then finally writes the dictionary back to the file 
		"""
		final_dictionary = {}
		initial_array = self.read_file()
		title = self.title_formating(title)
		array_of_entry = self.get_details(title, initial_array)
		array_of_entry.append(address)
		array_of_entry.append(server)
		original_dictionary = self.make_dictionary(initial_array)
		for title in original_dictionary:
			if not title in final_dictionary.keys():
				final_dictionary[title] = []
				for line in original_dictionary[title]:
					if not line in final_dictionary[title]:
						final_dictionary[title].append(line)
		if array_of_entry[0] in final_dictionary.keys():
			temp_title = array_of_entry[0]
			for i in range(1, len(array_of_entry)):
				if not array_of_entry[i] in final_dictionary[temp_title]:
					final_dictionary[temp_title].append(array_of_entry[i])
		self.write_dictionary_back_to_file(final_dictionary)
