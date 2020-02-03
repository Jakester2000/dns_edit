
def comment(file, title):
	found = False
	# [CODE REVIEW]
	# Almost all comments here are unneccessary. Remove them, so code is more readable. 
	# 	Change variable names to make easier to understand, if you need to.
	
	#creates a function called comment that runs when passed a file and a title
	with open(file, 'r') as f:
		#Opens the file and stores the contents into an array
		lines = f.readlines()

	with open(file, 'w') as f:
		# Overwrite file ready to write in data.
		pass

	with open(file, 'a') as f:
		#append everything inside the with statement onto the end of the dnsconfig
		line_counter = 0
		#create a variable and set it to 0
		while line_counter < len(lines):
			#While the script is not at the end of the file
			line = lines[line_counter]
			#Update the variable line to temporaily store the current line
			if line.strip('\n') == str("#" + title): 
				#Search for the given title name
				found = True
				f.write(line)

				# Once title name found, look for
				# all attributes associated with it.
				line_counter_2 = line_counter+1
				#create a second line counter and make it equal to the next line
				while "=" in lines[line_counter_2]:
					if "#" in lines[line_counter_2]:
						#if line already commented 
						f.write(lines[line_counter_2])
						#write line as normal
					else:
						f.write("#" + lines[line_counter_2])
						#write the server or address but with a hash at the beginning
					line_counter_2 += 1
					#increment line2 counter

				f.write("\n")
				#write a new line character
				line_counter = line_counter_2
				#set line1 counter to equal line2 counter

			else:
			#if the line isnt the title
				f.write(line)
				#write the line back into the file

			line_counter += 1
			#increment the line counter

		if found == False:
		#if the title couldnt be found then output an error message
			print("Title Couldnt be found, please check the usage and try again")