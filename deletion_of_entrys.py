def read_file(file):
	''' A function that copys the text from a file into an array

	Parameters:
		file: the name of the file that will be put into an array
	
	Errors:
		N/a
	'''
	with open(file, 'r') as f:
		file_string = f.read()
		return str(file_string).splitlines()

def delete_line(array_of_entries, index_to_remove, file):
	''' A function that removes any line the user inputs

	Parameters:
		array_of_entries: the array of text that is inside the text file
		index_to_remove: an integer that represents the line to remove
		file: the name of the file that will have the line removed
	
	Errors:
		N/a
	'''
	with open(file, "w+") as f:
		for line in range(0, len(array_of_entries) - 1):
			if line == index_to_remove:
				pass
			else:
				f.write(array_of_entries[line] + "\n")
		f.write("\n")

