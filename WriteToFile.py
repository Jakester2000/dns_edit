import sys

if "-h" in sys.argv:
	print("This script can be used to add an entry to the server config file")
	sys.exit("Usage: [File] [Title] [Server] [Address] \nHere's an Example:\n[File] = dns-entrys.txt\n[Title] = Google\n[Server] = /google.com/8.8.8.8\n[Address] = /google.com/162.52.26.42")

if len(sys.argv) < 5:
	sys.exit("Too few arguments. Usage: [File] [Title] [Server] [Address] \nHere's an Example:\n[File] = dns-entrys.txt\n[Title] = Google\n[Server] = /google.com/8.8.8.8\n[Address] = /google.com/162.52.26.42")
file = sys.argv[1]
title = sys.argv[2]
server = sys.argv[3]
address = sys.argv[4]

with open(file, 'a') as f:
	f.write("#" + title + "\n")
	f.write("server=" + server + "\n")
	f.write("address=" + address + "\n")
	f.write("\n")
	