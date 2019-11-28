
def comment(file, title):
	found = False
	with open(file, 'r') as f:
		lines = f.readlines()
	with open(file, 'w') as f:
		pass
	with open(file, 'a') as f:
		line_counter = 0
		while line_counter < len(lines):
			line = lines[line_counter]
			if line.strip('\n') == str("#" + title): 
				found = True
				f.write(line)
				line_counter_2 = line_counter+1
				while "=" in lines[line_counter_2]:
					if "#" in lines[line_counter_2]:
						f.write(lines[line_counter_2])
					else:
						f.write("#" + lines[line_counter_2])
					line_counter_2 += 1
				f.write("\n")
				line_counter = line_counter_2
			else:
				f.write(line)
			line_counter += 1
		if found == False:
			print("Title Couldnt be found, please check the usage and try again")