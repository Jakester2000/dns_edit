
def isTitle(line):
	return ("#" in line and "=" not in line)


def readFiles(file1, file2):
	with open(file1, 'r') as f:
		filestring = f.read()
		linearray = str(filestring).splitlines()

	with open(file2, 'r') as f:
		filestring2 = f.read()
		linearray2 = str(filestring2).splitlines()

	return(linearray, linearray2)


def getDetails(title, array):
	index = 0
	output = []

	while index < len(array)-1:
		index += 1

		if title in array[index]:

			if index < len(array)-1:
				index += 1
			
			output.append(title)

			while index < len(array)+1 and "=" in array[index]:
				output.append(array[index])
				index += 1
	return output


def compare(linearray1, linearray2):
	output = []

	for line in linearray2:
		if isTitle(line):
			output.append(getDetails(line, linearray2))
	return output

def WriteArrayToMain(ListofLists, linearray1, file):

	with open(file, "r+") as f:
		contents = f.readlines()

		
	for singlelist in ListofLists:
		for item in singlelist:
			if isTitle(item):
				if item in linearray1:
					
					#we wanna write the single line list into the area under the
					#title but without the first index of the single line list
					nextline = linearray1.index(item) +1

					with open(file, "r+") as f:
						contents = f.readlines()

					contents.insert(nextline, "\n".join(singlelist[1:]) + "\n")

					with open(file, "w+") as f:
						f.writelines(contents)

				else:
					with open(file, "w+") as f:
						f.writelines(contents)
						f.writelines("\n".join(singlelist)+ "\n\n")



