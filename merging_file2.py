def is_title(line):
	return ("#" in line and "=" not in line)

def read_files(file1, file2):
	with open(file1, 'r') as f:
		file_string = f.read()
		line_array = str(file_string).splitlines()
	with open(file2, 'r') as f:
		file_string2 = f.read()
		line_array2 = str(file_string2).splitlines()
	return(line_array, line_array2)

def merge(file1, file2):
	index1 = 0
	index2 = 0
	array1, array2 = read_files(file1, file2)
	for line2 in array2:
		index2 += 1
		if is_title(line2):
			for line1 in array1:
				index1 += 1
				if line1 == line2:
					print(index1, index2)
			index1 = 0		

		else:
			pass
merge("test", "compare")


