def read_file(file):
	"""
	A function that takes the parameter 'file'
	it will take a file and read all of the text into a string
	it will then use pythons  splitlines command to make arrays
	each line in the text file is an index in the array
	"""
	with open(file, 'r') as f:
		file_string = f.read()
		return str(file_string).splitlines()


def delete_line(array_of_entries, index_to_remove, file):
	"""
	A function that takes the parameters "array_of_entries", 
	"index_to_remove" and "file"
	it will take an array and loop through each line
	once the line index equals the line we want to remove it doesnt write
	the line
	"""
	with open(file, "w+") as f:
		for line in range(0, len(array_of_entries) - 1):
			if line == index_to_remove:
				pass
			else:
				f.write(array_of_entries[line] + "\n")
		f.write("\n")
# [CODE REVIEW]
# This file is better. Standardise commenting
