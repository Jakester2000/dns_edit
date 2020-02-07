import sys
import commenting
import merging
import delete
import helpscript
import adding
import backup
FORCE_ENABLED = False


'''below controls all the arguments the user enters, different if statements for different classes and functions'''

#HELP SCRIPT [In form: python3 dns_edit.py -h]
if ("-h") in sys.argv:
	helpscript.script()

#VALIDATION: if the entry is not long enough to run any commands
if len(sys.argv) < 3:
	sys.exit("Command Not Found, Please check usage and try again")

#MANUAL BACKUP [In form: python3 dns_edit.py -b -f whitelist_file -n "Backup"]
elif sys.argv[1] == "-b" and sys.argv[2] == "-f" and sys.argv[3] != "" and sys.argv[4] == "-n" and sys.argv[5] != "":
	backup_object = backup.backup(sys.argv[3])
	backup_object.manual_backup(sys.argv[5])
	sys.exit("Done!")

#COMMENT SINGLE [In form: python3 dns_edit.py -c -f whitelist_file -t Title (optional -force)]
elif sys.argv[1] == "-c" and sys.argv[2] == "-f" and sys.argv[3] != "" and sys.argv[4] == "-t" and sys.argv[5] != "":
	file = sys.argv[3]
	commenting = commenting.commenter(file)
	if "-force" in sys.argv:
		FORCE_ENABLED = True
		for i in range(5, len(sys.argv)-1):
			commenting.comment_single(sys.argv[i], FORCE_ENABLED)
	else:
		FORCE_ENABLED = False
		for i in range(5, len(sys.argv)):
			commenting.comment_single(sys.argv[i], FORCE_ENABLED)
	print("Remember to use the restart command to apply changes")
	sys.exit()

#COMMENT ALL [In form: python3 dns_edit.py -c -a -f whitelist_file (optional -force)]
elif sys.argv[1] == "-c" and sys.argv[2] == "-a" and sys.argv[3] == "-f" and sys.argv[4] != "":
	full_permisions = False
	if len(sys.argv) == 6:
		if sys.argv[5] == "-force":
			full_permisions = True
	file = sys.argv[4]
	commenting = commenting.commenter(file)
	commenting.comment_all(full_permisions)
	print("Remember to use the restart command to apply changes")

#UNCOMMENT SINGLE [In form: python3 dns_edit.py -u -f whitelist_file -t Title (optional -force)]
elif sys.argv[1] == "-u" and sys.argv[2] == "-f" and sys.argv[3] != "" and sys.argv[4] == "-t" and sys.argv[5] != "":
	file = sys.argv[3]
	commenting = commenting.commenter(file)
	if "-force" in sys.argv:
		FORCE_ENABLED = True
		for i in range(5, len(sys.argv)-1):
			commenting.uncomment_single(sys.argv[i], FORCE_ENABLED)
	else:
		FORCE_ENABLED = False
		for i in range(5, len(sys.argv)):
			commenting.uncomment_single(sys.argv[i], FORCE_ENABLED)
	print("Remember to use the restart command to apply changes")
	sys.exit()

#UNCOMMENT ALL [In form: python3 dns_edit.py -u -a -f whitelist_file (optional -force)]
elif sys.argv[1] == "-u" and sys.argv[2] == "-a" and sys.argv[3] == "-f" and sys.argv[4] != "":
	full_permisions = False
	if len(sys.argv) == 6:
		if sys.argv[5] == "-force":
			full_permisions = True
	file = sys.argv[4]
	commenting = commenting.commenter(file)
	commenting.uncomment_all(full_permisions)
	print("Remember to use the restart command to apply changes")

#MERGE FILES [In Form: python3 dns_edit.py -m -f1 File1 -f2 File2]
elif sys.argv[1] == "-m" and sys.argv[2] == "-f1" and sys.argv[3] != "" and sys.argv[4] == "-f2" and sys.argv[5] != "":
	file1 = sys.argv[3]
	file2 = sys.argv[5]
	combiner = merging.combine(file1, file2)
	string_file_1, string_file_2 = combiner.read_files()
	array_file_1, array_file_2 = combiner.make_array_from_string(string_file_1, string_file_2)
	dictionary_file_1, dictionary_file_2 = combiner.make_dictionary(array_file_1, array_file_2)
	combiner.merge(dictionary_file_1, dictionary_file_2)
	print("Remember to use the restart command to apply changes")

#ENTRY ADDING [In Form: python3 dns_edit.py -a -f whitelist_file -t Title -s Server (optional -a Address)]
elif sys.argv[1] == "-a" and sys.argv[2] == "-f" and sys.argv[3] != "":
	file = sys.argv[3]
	adding_object = adding.add(file)
	if len(sys.argv) == 8:
		if sys.argv[4] == "-t" and sys.argv[5] != "" and sys.argv[6] != "" and sys.argv[7] != "":
			adding_object.ip_adding(sys.argv[5], sys.argv[7])
			print("Remember to use the restart command to apply changes")
	else:
		pass
	if len(sys.argv) == 10:
		if sys.argv[4] == "-t" and sys.argv[5] != "" and sys.argv[6] == "-s" and sys.argv[7] != "" and sys.argv[8] == "-a" and sys.argv[9] != "":
			adding_object.full_add(sys.argv[5], sys.argv[7], sys.argv[9])
			print("Remember to use the restart command to apply changes")
		elif sys.argv[4] == "-t" and sys.argv[5] != "" and sys.argv[6] == "-a" and sys.argv[7] != "" and sys.argv[8] == "-s" and sys.argv[9] != "":
			adding_object.full_add(sys.argv[5], sys.argv[9], sys.argv[7])
			print("Remember to use the restart command to apply changes")
	else:
		pass

#REMOVING ENTRY [In Form: python3 dns_edit.py -r -f whitelist_file -t Title]
elif sys.argv[1] == "-r" and sys.argv[2] == "-f" and sys.argv[3] != "" and sys.argv[4] == "-t" and sys.argv[5] != "":
	deleting_object = delete.deleting(sys.argv[3])
	deleting_object.rem_title(sys.argv[5])

#REMOVING IP [In Form: python3 dns_edit.py -r -f whitelist_file -ip server=/google.com/8.8.8.8]	
elif sys.argv[1] == "-r" and sys.argv[2] == "-f" and sys.argv[3] != "" and sys.argv[4] == "-ip" and sys.argv[5] != "":
	deleting_object = delete.deleting(sys.argv[3])
	deleting_object.rem_single(sys.argv[5])

#REMOVING DUPLICATES [In Form: python3 dns_edit.py -rd -f whitelist_file]
elif sys.argv[1] == "-rd" and sys.argv[2] == "-f" and sys.argv[3] != "":
	file = sys.argv[3]
	combine.remove_duplicates(file)
	print("Remember to use the restart command to apply changes")

#if they dont enter any arguments an error output is produced
elif sys.argv[0] == "":
	sys.exit("error, check usage in -h and try again")

#if the syntax is incorrect then this else statement is ran
else:
	sys.exit("error, syntax incorrect, check usage in -h and try again")
