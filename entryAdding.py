
def addEntry(file, title, server, address):
	with open(file, 'r') as f:
		filestring = f.read()
		linearray = str(filestring).splitlines()
		if server != "":
			linearray = addserveroraddress(server, "server", title, linearray)
		elif address != "":
			linearray = addserveroraddress(address, "address", title, linearray)
	with open(file, 'w+') as f:
		for i in range(0, len(linearray)):
			f.write(linearray[i])
			if "\n" not in linearray[i]:
				f.write("\n")

def addServerOrAddress(entryType, name, title, linearray):	
	i = 0
	end = False
	flag = False
	while i < len(linearray) and end == False:
		line = linearray[i]
		i += 1
		if line.startswith("#" + title):
			print ("hello")
			flag = True
		if line.startswith(name) or line.startswith("#" + name):
			linearray[i] = linearray[i]+ '\n' + name + "=" + entryType + "\n"
			flag = False
			end = True
			break
	return(linearray)