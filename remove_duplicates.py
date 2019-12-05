def remove_duplicates(file):
	''' A function that removes duplicate entries from file provided
	Parameters:
		file: the name of the file that will be searched for duplicates
	Errors:
		duplicate_found: If False then outputs message to inform user
	'''
	duplicate_found = False
	index_loop_1 = 0
	index_loop_2 = 0
	with open(file, 'r') as f:
		lines = f.readlines()
	for line in lines:
		index_loop_2 = 0
		if line == "\n":
			pass
		else:	
			for line_to_check in lines:
				if line_to_check == "\n":
					pass
				elif index_loop_1 == index_loop_2:
					pass
				else:
					if line in line_to_check or "#" + line in line_to_check:
						duplicate_found = True
						lines.pop(index_loop_2)
						index_loop_2 -= 1
				index_loop_2 += 1
		index_loop_1 += 1
	if duplicate_found == False:
		print("Duplicate not found, check entries and try again")
	with open(file, "w+") as f:
		f.writelines(lines)

