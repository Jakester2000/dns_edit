def remove_duplicates():
	index_loop_1 = 0
	index_loop_2 = 0
	file = "test"
	with open(file, 'r') as f:
		lines = f.readlines()
	#read the file into an array called lines stored in memory 
	# ^^ [CODE REVIEW] Useless comment. Add one at the beginning
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
						print(line)
						print(index_loop_1)
						print(index_loop_2)
						lines.pop(index_loop_2)
						index_loop_2 -= 1
				index_loop_2 += 1

		index_loop_1 += 1

	with open(file, "w+") as f:
		f.writelines(lines)



remove_duplicates()