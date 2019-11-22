def readFile(file):
	with open(file, 'r') as f:
		filestring = f.read()
		return str(filestring).splitlines()


def deleteline(arrayOfEntries, indexToRemove, file):
	with open(file, "w+") as f:
		for line in range(0, len(arrayOfEntries) - 1):
		
			if line == indexToRemove:
			
				pass
			else:
				f.write(arrayOfEntries[line] + "\n")
		f.write("\n")

