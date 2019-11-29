def write(file, index, to_write):
	''' A function that writes to a specified line
	Parameters:
		file: the name of the file that will be written to
		index: location to be written to
		to_write: string that is going to be added
	Errors:
		N/a
	'''
	with open(file, "r+") as f:
		contents = f.readlines()
	contents.insert(index, to_write)
	with open(file, "w+") as f:
		f.writelines(contents)
