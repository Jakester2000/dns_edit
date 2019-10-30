#set this to the path where the file with the server information is kept
FilePath = input("whats the file called? >>>  ")
UserInput = input("What line you want \"#\" to be removed? >>>  ")
def write(file, to_write):
	with open(file, 'a+') as f:
		f.write(f'{to_write}\n')


def delete(file, to_delete):
	with open(file, 'r') as f:
		lines = f.readlines()

	with open(file, 'w') as f:
		for line in lines:
			if line.strip('\n') != to_delete:
				f.write(line)
			else:
				f.write(line.strip('#'))



for i in range(0, 50):
	write(FilePath, "#line number" + str(i))

delete(FilePath, UserInput)