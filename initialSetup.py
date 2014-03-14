#	Establish a connection with database and create table as defined in supplied sql file
#	Note: Formatting of sql file is at the moment a little strange, see a2_setup_noComments.sql 
#		for a good example of a working sql file

#	BUGS:	create table file must not have comments


#	Code: Chase McCarty

import sys
import cx_Oracle

def establishConnection():
	#connect to the database
	try:
		connection = cx_Oracle.connect('cmccarty/4cidm4n67@gwynne.cs.ualberta.ca:1521/CRS')
		curs1 = connection.cursor()
	except cx_Oracle.DatabaseError as exc:
		error, = exc.args
		print("Error connecting to database")
		print(sys.stderr, "Oracle code: ", error.code)
		print(sys.stderr, "Oracle Message ", error.message)
	
	
	#open table creation file and begin creation
	# NOTE must use a file with no comments, no empty lines, and no ';' after last statement. 
	# if unsure, check a2_setup_noComments.sql for formatting style
	inputFile = open('a2_setup_noComments.sql')
	createText = inputFile.read()
	createStatements = createText.split(';')

	# Invalid commands will be written to stderr, though other commands will continue to run 
	for command in createStatements:
		try:
			curs1.execute(command)
		except cx_Oracle.DatabaseError as exc:
			error, = exc.args
			print("Error in statement: ", command)
			print(sys.stderr, "Oracle code: ", error.code)
			print(sys.stderr, "Oracle message: ", error.message)	
	inputFile.close()
	curs1.close()
	connection.commit()

	
	# Populate table
	# for now unsure how to make more efficient with prepared statements without hard coded populate list
	inputFile = open('a2-data.sql')
	populationFile = inputFile.read().split(';')
	cursInsert = connection.cursor()

	for command in populationFile:
		try:
			cursInsert.execute(command)
		except cx_Oracle.DatabaseError as exc:
			error, = exc.args
			print("Error in statement: ", command)
			print(sys.stderr, "Oracle code: ", error.code)
			print(sys.stderr, "Oracle message: ", error.message)
	inputFile.close()
	cursInsert.close()
	connection.commit()

	connection.close()


if __name__ =="__main__":
	establishConnection()
