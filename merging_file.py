def is_title(line):
	''' A function checks whether a given string meets the criteria to be a title'''
	return ("#" in line and "=" not in line)
def read_files(file1, file2):
	''' A function reads two files into two seperate arrays
	Parameters: 
		file1: used to locate 1st file
		file2: used to locate 2nd file
	Returns: 
		line_array: array that contains all the text from the dns file
		line_array2:array that contains all the text from the 2nd dns file
	'''
	with open(file1, 'r') as f:
		file_string = f.read()
		line_array = str(file_string).splitlines()
	with open(file2, 'r') as f:
		file_string2 = f.read()
		line_array2 = str(file_string2).splitlines()

	return(line_array, line_array2)
def get_details(title, array):

	current_title = ""
	output = []
	
	for i in range(array.index(title), len(array) - 1):
		if is_title(array[i]) and array[i] != title:
			break
		elif array[i] != "":
			output.append(array[i])
		
	return output
def make_dictionary(line_array):
	
	dictionary_of_entries = {}
	for line in line_array:
		if is_title(line):
			dictionary_of_entries[line] = get_details(line, line_array)

	return dictionary_of_entries
def write_array_to_main(entries_to_add, line_array1, file):
	original_entries = make_dictionary(line_array1)

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
		

