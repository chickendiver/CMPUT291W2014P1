#	Establish a connection with database and create table as defined in supplied sql file
#	Note: Formatting of sql file is at the moment a little strange, see a2_setup_noComments.sql 
#		for a good example of a working sql file

#	BUGS:	running initial drop statements crash if table to be dropped does not exist
#	Proposed FIX: Filter exceptions appropriately


#	Code: Chase McCarty

import sys
import cx_Oracle

def establishConnection():
	#connect to the database
	try:
		connection = cx_Oracle.connect('cmccarty/4cidm4n67@gwynne.cs.ualberta.ca:1521/CRS')
		curs1 = connection.cursor()

		#open table creation file and begin creation
		# NOTE must use a file with no comments, no empty lines, and no ';' after last statement. 
		# if unsure, check a2_setup_noComments.sql for formatting style
		inputFile = open('a2_setup_noComments.sql')
		createText = inputFile.read()
		createStatements = createText.split(';')

		## BUG ## Drop tables cause crash if table does not exist
		for command in createStatements:
			sys.stdout.write(command)
			curs1.execute(command)
		
		

		inputFile.close()
		connection.commit()

		curs1.close()
		connection.close()

	#if connection fails:
	except cx_Oracle.DatabaseError as exc:
		error, = exc.args
		print(sys.stderr, "Oracle code: ", error.code)
		print(sys.stderr, "Oracle Message: ", error.message)

if __name__ =="__main__":
	establishConnection()
