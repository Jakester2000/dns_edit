import datetime
import sys
BACKUP_DIR = "backups/"

class backup:
    #creates a class called backup
    def __init__(self, existing_file):
        """
		This function is ran automatically whenever an instance of this class is created
		(Whenever an object is created)
		it sets the variable self.file to equal to the file path passed
		"""
        self.file = existing_file

    def manual_backup(self, backup_name):
        """
		This function creates manual backups when called
        It uses the datetime package to include the date and time in the title of the renamed file
        there is reformating to make the file name easier to understand
        Arguments:
        @backup_name: A string passed into the function that will be in the final backup name
		"""
        existing_file = self.file
        with open(existing_file, 'r') as f:
            date_time_string = str(datetime.datetime.now())
            date_time_string = "[" + date_time_string[8:10] + "." + date_time_string[5:7] + "." + date_time_string[0:4] + "]" + "[" + date_time_string[11:19] + "]"
            final_backup_name = date_time_string + backup_name
            try:
                print(str('cp ' + existing_file + ' ' + backup_dir + final_backup_name))
            except:
                sys.exit("Error, not on linux")

    #def auto_backup(self, existing_file)
    #function to implement after code review^
