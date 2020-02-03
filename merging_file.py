
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


def get_details(title, array):
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


def compare(line_array1, line_array2):
	output = []

	for line in line_array2:
		if is_title(line):
			output.append(get_details(line, line_array2))
	return output

def write_array_to_main(list_of_lists, line_array1, file):

	with open(file, "r+") as f:
		contents = f.readlines()

		
	for single_list in list_of_lists:
		for item in single_list:
			if is_title(item):
				if item in line_array1:
					
					#we wanna write the single line list into the area under the
					#title but without the first index of the single line list
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



