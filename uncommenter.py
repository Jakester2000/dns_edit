
def uncomment(file, title):
	"""
	A function that takes the parameters 'file' and 'title'
	it will uncomment all the entries underneath the provided title
	if the entries are already uncommented no changes will be made
	if the title doesnt exist it will output a corrosponding error message
	"""
	# [CODE REVIEW]
	# Make more succinct. Use standards as written in 'main.py' 
	# 	when talking about params, etc
	found = False
	with open(file, 'r') as f:
		lines = f.readlines()
	#read the file into an array called lines stored in memory 
	# ^^ [CODE REVIEW] Remove, pointless
	with open(file, 'w') as f:
		pass
	# Overwrite file ready to write in data.
	with open(file, 'a') as f:
		line_counter = 0
		while line_counter < len(lines):
			#While the script is not at the end of the file
			# ^^ [CODE REVIEW] Remove, pointless
			line = lines[line_counter]
			if line.strip('\n') == str("#" + title): 
				found = True
				f.write(line)
				line_counter_2 = line_counter+1
				while "=" in lines[line_counter_2]:
					f.write(lines[line_counter_2].strip("#"))
					line_counter_2 += 1
				f.write("\n")
				line_counter = line_counter_2
			else:
				f.write(line)
			line_counter += 1
		if found == False:
			print("error, title not found, please check the input and try again")
