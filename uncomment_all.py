def uncomment_all(file, title):
	with open(file, 'r') as f:
		lines = f.readlines()
	with open(file, 'w') as f:
		pass
	with open(file, 'a') as f:
		for line in lines:
			if not is_title(line):
				f.write(line.strip("#"))
			else:
				f.write(line)

def is_title(line):
	return ("#" in line and "=" not in line)

uncomment_all("test", "line12")