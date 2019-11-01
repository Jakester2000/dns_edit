#set this to the path where the file with the server information is kept
FilePath = input("whats the file called? >>>  ")
UserInput = input("What line you want \"#\" to be removed? >>>  ")

def checkTitle(file, to_check):
	found = False
	with open(file, 'r') as f:
		lines = f.readlines()
			

	with open(file, 'w') as f:
	
		while not found:
			for line in lines:
				if line.strip('\n') == str("#" + to_check):
					print("Found")
					found = True
					f.write(line.strip("#"))

				else:

					f.write(line)
			


checkTitle(FilePath, UserInput)

	



# delete(FilePath, UserInput)