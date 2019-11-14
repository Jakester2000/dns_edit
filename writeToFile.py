
def write(file, title, server, address):
	with open(file, 'a+') as f:
		f.write(f'#{title}\nserver={server}\naddress={address}\n\n')