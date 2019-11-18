

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


def combine(positionOfTitleInArray1, positionOfTitleInArray2, linearray1, linearray2):
	
	for i in linearray1:

		if not isTitle(linearray[positionOfTitleInArray1 + i]):
			finalarray[i] = linearray1[positionOfTitleInArray1]
			print(finalarray[i])
			end = True
		i += 1
		if i == len(linearray1)-1:
			end = True
		if positionOfTitleInArray1 == len(linearray1)-1:
			end = True


def titleInArray(title, array):
	for line in array:
		if title in line:
			return True
	return False


def getDetails(title, array):
	index = 0
	output = []

	while index < len(array)-1:
		index += 1

		if title in array[index]:

			if isTitle(array[index]) and index < len(array)+1:
				index += 1
			
			output.append(title)

			while index < len(array)+1 and "=" in array[index]:
				output.append(array[index].split("=")[1])
				index += 1

	return output


def compare(linearray1, linearray2):
	temp = ""
	flag = True
	positionOfTitleInArray1 = 0
	positionOfTitleInArray2 = 0

	out = []

	for line in linearray2:
		if isTitle(line) and titleInArray(line, linearray2):
			out.append(getDetails(line, linearray2))

	return out
