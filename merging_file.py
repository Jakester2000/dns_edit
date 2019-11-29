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
	''' A function that gets all the servers / addresses corrosponding to the title
	Parameters: 
		title: the title that will be used to find the information about
		array: all the text from the textfile that will be searched through
	Returns: 
		output: an array of all the details to be written back into the main file
	'''
	index = 0
	output = []
	while index < len(array)-1:
		index += 1
		if title in array[index]:
			if index < len(array)-1:
				index += 1
			output.append(title)
			while index < len(array)+1 and "=" in array[index]:
				output.append(array[index])
				index += 1
	return output
def compare(line_array2):
	''' A function that checks if a title exists and then concatonates it onto output
	Parameters:
		line_array2: the secondary file with the entries that are getting added
	Returns: 
		output: a list of entries to add to the main file
	'''
	output = []
	for line in line_array2:
		if is_title(line):
			output.append(get_details(line, line_array2))
	return output
def write_array_to_main(list_of_lists, line_array1, file):
	''' A function that writes the final array back into the file
	Parameters: 
		list_of_lists: each sub-list inside the list contains a block entry, including the title, server and address
		line_array1: the array that holds the final strings to be written back into the file
		file: the directory / name of the file
	Returns: 
		N/a
	'''
	with open(file, "r+") as f:
		contents = f.readlines()
	for single_list in list_of_lists:
		for item in single_list:
			if is_title(item):
				if item in line_array1:
					next_line = line_array1.index(item) +1
					with open(file, "r+") as f:
						contents = f.readlines()
					contents.insert(next_line, "\n".join(single_list[1:]) + "\n")

					with open(file, "w+") as f:
						f.writelines(contents)
				else:
					with open(file, "w+") as f:
						f.writelines(contents)
						f.writelines("\n".join(single_list)+ "\n\n")



