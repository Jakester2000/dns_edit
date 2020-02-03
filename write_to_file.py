def write(file, index, to_write):
	#creates a function that takes file, index to write to and what to write
	# ^^ [CODE REVIEW] Standardise all comments at the beginnings of functions
	# [CODE REVIEW] Comments below are mainly pointless. 
	# 	Remove pointless white space, too
	with open(file, "r+") as f:
		#open the file and store the contents into an array called contents
		contents = f.readlines()

	contents.insert(index, to_write)
	#inserts the to_write variable into the array

	with open(file, "w+") as f:
		f.writelines(contents)
		#rewrites the array after the to_write has been added