def read_file(file):
	"""
	A function that takes the parameter 'file'
	it will take a file and read all of the text into a string
	it will then use pythons  splitlines command to make arrays
	each line in the text file is an index in the array
	"""
	# [CODE REVIEW]
	# Standardise, as before
	with open(file, 'r') as f:
		file_string = f.read()
		return str(file_string).splitlines()

def is_title(line):
	return ("#" in line and "=" not in line)


	


def Uncomment_all(file):
	with open(file, "w+") as f:

	with open(file, 'a') as f:
		all_lines = []
		all_lines = read_file(file)

		for line in all_lines:
			if is_title(line):

