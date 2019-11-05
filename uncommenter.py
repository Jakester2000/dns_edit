import sys

if "-h" in sys.argv:
	print("This script can be used to uncomment server entries in the config file")
	sys.exit("Usage: [file] [application_name]")

if len(sys.argv) < 3:
	sys.exit("Too few arguments. Usage: [file] [application_name]")

file = sys.argv[1]
to_check = sys.argv[2:]

def uncomment(application):
	# Copy contents of file into memory.
	with open(file, 'r') as f:
		lines = f.readlines()

	# Overwrite file ready to write in data.
	with open(file, 'w') as f:
		pass

	with open(file, 'a') as f:
		line_counter = 0

		while line_counter < len(lines):
			line = lines[line_counter]

			# Search for the given application name.
			if line.strip('\n') == str("#" + application): 
				f.write(line)

				# Once application name found, look for
				# all attributes associated with it.
				line_counter_2 = line_counter+1
				while "=" in lines[line_counter_2]:
					f.write(lines[line_counter_2].strip("#"))
					line_counter_2 += 1

				f.write("\n")
				line_counter = line_counter_2

			else:
				f.write(line)

			line_counter += 1


for title in to_check:
	uncomment(title)