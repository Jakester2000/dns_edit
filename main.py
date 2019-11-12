import sys

import commenter
import uncommenter
import WriteToFile
import helpScript
import entryadding

if len(sys.argv) < 2:
	sys.exit("Too few arguments. Run '-h' for help")

if "-h" in sys.argv:
	helpScript.Help()

if "-f" in sys.argv:
	if sys.argv.index("-f") == len(sys.argv) - 1:
			sys.exit("No argument given.") 
	file = sys.argv[sys.argv.index("-f") + 1]
else:
	sys.exit("No file specified.")

if "-t" in sys.argv:
	if sys.argv.index("-t") == len(sys.argv) - 1:
		sys.exit("No argument given.")
	title = sys.argv[sys.argv.index("-t") + 1]
else:
	sys.exit("Please specify title.")


if "-u" in sys.argv:
	uncommenter.uncomment(file, title)


if "-c" in sys.argv:
	commenter.comment(file, title)


if "-w" in sys.argv:
	if "-a" not in sys.argv or "-s" not in sys.argv or sys.argv.index("-a") == len(sys.argv) - 1 or sys.argv.index("-s") == len(sys.argv) - 1:
		sys.exit("Server or address not specified.")
	else:
		server = sys.argv[sys.argv.index("-s") + 1]
		address = sys.argv[sys.argv.index("-a") + 1]
		WriteToFile.writeToFile(file, title, server, address)


if "-e" in sys.argv:
	file = "test"
	title = "facebook"
	server = "www.facebook.com/10.12.10.10"
	address = "www.facebook.com/125.75.63.26"
	entryadding.addentry(file, title, server, address)

