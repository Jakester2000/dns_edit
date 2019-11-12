def addentry(file, title, server, address):
	# with open(file, 'r') as f:
	# 	lines = f.readlines()

	# with open(file, 'w') as f:
	# 	pass

	# with open(file, 'a') as f:
	# 	line_counter = 0
	# 	flag = False

	# 	while line_counter < len(lines):
	# 		print("test")
	# 		line = lines[line_counter]
	# 		# Search for the given application name.

	# 		if line.strip('\n') == str("#" + title): 
	# 			f.write(line)
	# 			#
	# 			line_counter_2 = line_counter+1
	# 			flag = True
	# 		else:
	# 			f.write(line)
	# 			line_counter += 1
	# 		if server != "":
	# 			if "server" in lines[line_counter]:
	# 				if flag == True:
	# 					f.write(line)
	# 					flag = False
	# 		line_counter += 1

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

			if line.strip('\n') == str("#" + title): 
				f.write(line)
				# Once application name found, look for
				# all attributes associated with it.
				line_counter_2 = line_counter+1

				while "server=" in lines[line_counter_2]:
					f.write(lines[line_counter_2])
					line_counter_2 += 1

				f.write(f"server={server}\n")

				while "address=" in lines[line_counter_2]:
					f.write(lines[line_counter_2])
					line_counter_2 += 1

				f.write("\n")

				line_counter = line_counter_2

			else:
				f.write(line)
			line_counter += 1
