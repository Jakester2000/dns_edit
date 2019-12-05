def comment_all(file, title):
	with open(file, 'r') as f:
		lines = f.readlines()
	with open(file, 'w') as f:
		pass
	with open(file, 'a') as f:
		for line in lines:
			if is_title(line):
				f.write(line)
			elif "#" in line:
				f.write(line)
			elif line == "\n":
				f.write(line)
			else:
				f.write("#"+line)


def is_title(line):
	return ("#" in line and "=" not in line)

comment_all("test", "line12")