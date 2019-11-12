
def uncomment(file, application):
	# Copy contents of file into memory.

	with open(file, 'r') as f:
		lines = f.readlines()
	# Overwrite file ready to write in data.

	with open(file, 'w') as f:
		pass

	with open(file, 'a') as f:
		line_counter = 0

		while line_counter < len(lines):
			line = lines[line_counter]
			# Search for the given application name.

			if line.strip('\n') == str("#" + application): 
				f.write(line)
				# Once application name found, look for
				# all attributes associated with it.
				line_counter_2 = line_counter+1

				while "=" in lines[line_counter_2]:
					f.write(lines[line_counter_2].strip("#"))
					line_counter_2 += 1

				f.write("\n")
				line_counter = line_counter_2

			else:
				f.write(line)
			line_counter += 1