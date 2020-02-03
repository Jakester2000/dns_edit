import write_to_file


def add_entry(file, title, server, address):

	if not title.startswith("#"):
		title = "#" + title
	
	if address != "":
		add_address(file, title, address)

	if server != "":
		add_server(file, title, server)



def make_array(file):
	with open(file, 'r') as f:
		file_string = f.read()
		return str(file_string).splitlines()



def add_address(file, title, address):
	print(title)
	line_array = make_array(file)

	if title in line_array:
		counter = get_index(line_array, title) + 1

		while counter < (len(line_array)):
			if "address=" in line_array[counter] or "server=" in line_array[counter]:
				counter += 1
			else:
				write_to_file.write(file, counter, f"address={address}\n")
				return

	else:
		write_to_file.write(file, len(line_array), f"\n{title}\naddress={address}\n\n")



def add_server(file, title, server):
	line_array = make_array(file)

	if title in line_array:
		counter = get_index(line_array, title) + 1

		while counter < (len(line_array) - 1):
			if "server=" in line_array[counter]:
				counter += 1
			else:
				write_to_file.write(file, counter, f"server={server}\n")
				return

	else:
		write_to_file.write(file, len(line_array), f"\n{title}\nserver={server}\n\n")



def get_index(array, to_find):
	return array.index(to_find)
