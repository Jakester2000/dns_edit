import sys

HASH_CHAR = "#"
COMMENT_CHAR = "*"
NEW_LINE_CHAR = "\n"
class combine:

	def __init__(self, file1, file2):
		"""
		This function is ran automatically whenever an instance of this class is created
		(Whenever an object is created)
		it sets the variable self.file1 to equal to the file1 path passed
		it sets the variable self.file2 to equal to the file2 path passed
		"""
		self.file1 = file1
		self.file2 = file2
		
	def clear_file(self):
		"""
		This function clears the file in the file1 path that was passed when the object was created
		"""
		file = self.file1
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

	def read_files(self):
		"""
		This function checks that both the files exist. If the files exist it then creates a string called file_string1 and file_string2
		Returns:
		array_file: if the file exists the contents are returned as an array of lines
		"""
		file1 = self.file1
		file2 = self.file2
		try:
			with open(file1, 'r') as f:
				file_string1 = f.read()
		except:
			sys.exit("File1 not found, please check the filepath and try again")
		try:
			with open(file2, 'r') as f:
				file_string2 = f.read()
		except:
			sys.exit("File2 not found, please check the filepath and try again")
		return file_string1, file_string2

	def make_array_from_string(self, string_file_1, string_file_2):
		"""
		takes two strings as arguments, and then uses the .splitlines function to create two arrays
		and returns these two arrays
		arguments:
		@string_file_1: The raw string provided from read_files(file1)
		@string_file_2: The raw string provided from read_files(file2)
		"""
		return str(string_file_1).splitlines(), str(string_file_2).splitlines()

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
				#print(line)
		if title_found == False:
			print("title at bottom of file")
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
		title_location = line_array.index(title)
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

		#return dictionary_of_entries_f1


	def make_dictionary(self, array_file_1, array_file_2):
		"""
		Loops through the whole file array until it finds a title
		It then passes that title to the function "get_details" which returns an array
		this array is turned into a dictionary
		Arguments:
		@array_file_1: array storing the information in file1
		@array_file_2: array storing the information in file2
		Returns:
		dictionary_of_entries_f1: dictionary with every entry in from file1
		dictionary_of_entries_f2: dictionary with every entry in from file2
		"""
		dictionary_of_entries_f1 = {}
		dictionary_of_entries_f2 = {}
		for line in array_file_1:
			if self.is_title(line):
				dictionary_of_entries_f1[line] = self.get_details(line, array_file_1)
		for line in array_file_2:
			if self.is_title(line):
				dictionary_of_entries_f2[line] = self.get_details(line, array_file_2)

		return dictionary_of_entries_f1, dictionary_of_entries_f2

	def write_dictionary_back_to_file(self, dictionary_of_entries):
		"""
		this function is passed a dictionary, clears file1, and then writes the dictionary
		with the correct formatting back to the original file
		arguments:
		@dictionary_of_entries: a dictionary that contains everything to be written back to the main file location
		"""
		file = self.file1
		self.clear_file()
		with open(file, 'a') as f:
			for entry in dictionary_of_entries:
				for line in dictionary_of_entries[entry]:
					f.write(line + NEW_LINE_CHAR)
				f.write(NEW_LINE_CHAR)

	def merge(self, dictionary_of_entries_f1, dictionary_of_entries_f2):
		"""
		this is function that compares the two dictionarys to see if the titles are shared in common
		between the two.
		If they are then the corrosponding IPs are added under the correct section in the dictionary
		Else if they are not, the whole entry is added as a block into the dictionary.
		After this it calls the function write_dictionary_back_to_main to write the final dicitionary back to the original file
		arguments:
		@dictionary_of_entries_f1: a dictionary that contains everything from file1
		@dictionary_of_entries_f2: a dictionary that contains everything from file2
		"""
		for title in dictionary_of_entries_f2:
			if title in dictionary_of_entries_f1.keys():
				for line in dictionary_of_entries_f2[title]:
					if line not in dictionary_of_entries_f1[title]:
						dictionary_of_entries_f1[title].append(line)
			else:
				dictionary_of_entries_f1[title] = []
				for line in dictionary_of_entries_f2[title]:
					dictionary_of_entries_f1[title].append(line)
		self.write_dictionary_back_to_file(dictionary_of_entries_f1)