def write(file, index, to_write):

	with open(file, "r+") as f:
		contents = f.readlines()
	contents.insert(index, to_write)

	with open(file, "w+") as f:
		f.writelines(contents)
