import writeToFile


def addEntry(file, title, server, address):

	if not title.startswith("#"):
		title = "#" + title
	
	if address != "":
		addAddress(file, title, address)

	if server != "":
		addServer(file, title, server)



def makeArray(file):
	with open(file, 'r') as f:
		filestring = f.read()
		return str(filestring).splitlines()



def addAddress(file, title, address):
	linearray = makeArray(file)

	if title in linearray:
		counter = getIndex(linearray, title) + 1

		while counter < (len(linearray)):
			if "address=" in linearray[counter] or "server=" in linearray[counter]:
				counter += 1
			else:
				writeToFile.write(file, counter, f"address={address}\n")
				return

	else:
		writeToFile.write(file, len(linearray), f"\n{title}\naddress={address}\n\n")



def addServer(file, title, server):
	linearray = makeArray(file)

	if title in linearray:
		counter = getIndex(linearray, title) + 1

		while counter < (len(linearray) - 1):
			if "server=" in linearray[counter]:
				counter += 1
			else:
				writeToFile.write(file, counter, f"server={server}\n")
				return

	else:
		writeToFile.write(file, len(linearray), f"\n{title}\nserver={server}\n\n")



def getIndex(array, to_find):
	return array.index(to_find)
