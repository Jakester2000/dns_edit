def read_file(file):
	with open(file, 'r') as f:
		file_string = f.read()
		return str(file_string).splitlines()

def delete_line(array_of_entries, index_to_remove, file):
	with open(file, "w+") as f:
		for line in range(0, len(array_of_entries) - 1):
			if line == index_to_remove:
				pass
			else:
				f.write(array_of_entries[line] + "\n")
		f.write("\n")

