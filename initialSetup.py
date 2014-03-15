#	Establish a connection with database and create table as defined in supplied sql file
#	Note: Formatting of sql file is at the moment a little strange, see a2_setup_noComments.sql 
#		for a good example of a working sql file

#	Testing:	make sure create table and population works for all valid formats
#	Mods:		let user input database credentials, and input file names


#	Code: Chase McCarty

import sys
import cx_Oracle


# Returns a connection with the database
def establishConnection(username, password):
	connectionString = (str(username) + "/" + str(password) + "@gwynne.cs.ualberta.ca:1521/CRS")
	connection = None 
	try:
		connection = cx_Oracle.connect(connectionString)
		
	except cx_Oracle.DatabaseError as exc:
		error, = exc.args
		print(sys.stderr, "Error connecting to database")
		print(sys.stderr, "Oracle code: ", error.code)
		print(sys.stderr, "Oracle Message ", error.message)

	if connection:
		return connection
	else:
		print(sys.stderr, "Error establishing connection")
		return 0

# Create initial database tables from inputted .sql file
#!# any errors returned appear to be due to file input at this point and do not affect implemenation
def createTables(inputFile):
	inputFile = open(inputFile)
	createStatements = inputFile.read()
	createStatements = createStatements.split(';')

	curs = connection.cursor()

	for command in createStatements:
		try:
			curs.execute(command)
		except cx_Oracle.DatabaseError as exc:
			error, = exc.args
			if len(command) > 1:		#if command isnt just a newline character
				print(sys.stderr, "Error in statement: ", command)
				print(sys.stderr, "Oracle code: ", error.code)
				print(sys.stderr, "Oracle message: ", error.message)

	inputFile.close()
	curs.close()
	connection.commit()

# Populate created tables with inputted .sql file
#!# any errors returned appear to be due to file input at this point and do not affect implemenation
def populateTables(inputFile):
	inputFile = open(inputFile)
	populateStatements = inputFile.read()
	populateStatements = populateStatements.split(';')

	cursInsert = connection.cursor()

	for command in populateStatements:
		try:
			cursInsert.execute(command)
		except cx_Oracle.DatabaseError as exc:
			error, = exc.args
			if len(command) > 1:		#if command isnt just a newline character
				print(sys.stderr, "Error in statement: ", command)
				print(sys.stderr, "Oracle code: ", error.code)
				print(sys.stderr, "Oracle message: ", error.message)
	inputFile.close()
	cursInsert.close()
	connection.commit()


# Establishes a Connection to the database, creates and populates tables
#!# files and credentials are hard coded at the moment, this needs to be changed before release
def establishConnectionDeprecated(tableFile, populationFile, username, password):
	#connect to the database
	try:
		connection = cx_Oracle.connect('cmccarty/4cidm4n67@gwynne.cs.ualberta.ca:1521/CRS')
		curs1 = connection.cursor()
	except cx_Oracle.DatabaseError as exc:
		error, = exc.args
		print(sys.stderr, "Error connecting to database")
		print(sys.stderr, "Oracle code: ", error.code)
		print(sys.stderr, "Oracle message ", error.message)
	
	
	# open table creation file and begin creation
	# Files with comments appear to work but additional testing should be done
	inputFile = open('a2_setup_new.sql')
	createText = inputFile.read()
	createStatements = createText.split(';')

	# Invalid commands will be written to stderr, though other commands will continue to run 
	for command in createStatements:
		try:
			curs1.execute(command)
		except cx_Oracle.DatabaseError as exc:
			error, = exc.args
			print(sys.stderr, "Error in statement: ", command)
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
			print(sys.stderr, "Error in statement: ", command)
			print(sys.stderr, "Oracle code: ", error.code)
			print(sys.stderr, "Oracle message: ", error.message)
	inputFile.close()
	cursInsert.close()
	connection.commit()

	return connection

# Returns statements that Puts a vehicle in the database
#!# Does not perform checks for conflicting information already in database, or any checks for that matter (yet)
def createVehicle(serialNum, make, model, year, color, vType):
	statement = "INSERT INTO vehicle VALUES ('" + str(serialNum) + "', '" + str(make) + "', '" + str(model) + "', " + str(year) + ", '" + str(color) + "', " + str(vType) + ")" 
	return statement


if __name__ =="__main__":
	connection = establishConnection('cmccarty', '4cidm4n67')
	createTables("a2_setup_new.sql")
	populateTables("a2-data.sql")


	curs = connection.cursor()
	# this will be merged with mainMenu later
	statement = (createVehicle("1e37y6", "Lamborghini", "Egoista", 2014, "blue", "0001"))
	try:
		curs.execute(statement)	
	except cx_Oracle.DatabaseError as exc:
		error, = exc.args
		print(sys.stderr, "Error in statement: ", statement)
		print(sys.stderr, "Oracle code: ", error.code)
		print(sys.stderr, "Oracle message: ", error.message)

	curs.close()
	connection.commit()
	connection.close()

