import sys
import cx_Oracle

#this is a comment
def establishConnection():

	#setup create table string
	createStr = ("create table TOFFEES "
            "(T_NAME VARCHAR(32), SUP_ID INTEGER, PRICE FLOAT, SALES INTEGER, TOTAL INTEGER)")

	#try connecting to database
	#initializing a cursur for command entry
	#drop the table we are about to create incase it already exists
	#and creating our table with our string 
	try:
		connection = cx_Oracle.connect('cmccarty/nothing@gwynne.cs.ualberta.ca:1521/CRS')
		curs = connection.cursor()
		curs.execute("drop table TOFFEES")
		curs.execute(createStr)

		#initilize 3 rows of data to be added in an array
		#get a new command cursor, and set input based on our data
		#execute all 3 adds 
		#and commit
		data = [('Quadbury', 101, 7.99, 0, 0),('Almond roca', 102, 8.99, 0, 0),('Golden Key', 103, 3.99, 0, 0)]
		cursInsert = connection.cursor()
		cursInsert.bindarraysize = 3
		cursInsert.setinputsizes(32,int,float,int,int)
		cursInsert.executemany("INSERT INTO TOFFEES (T_NAME, SUP_ID, PRICE, SALES, TOTAL)" "VALUES(:1,:2,:3,:4,:5)", data)
		connection.commit()

		#execute a select statement using first cursor
		#fetch the result into rows
		#and print output line by line
		curs.execute("SELECT * from TOFFEES")
		rows = curs.fetchall()
		for row in rows:
			print(row)
			
		#close our cursors, and close our connections
		curs.close()
		cursInsert.close()
		connection.close()

	#if connection fails, through exception
	except cx_Oracle.DatabaseError as exc:
		error = exc.args
		print(sys.stderr, "Oracle code: ", error.code)
		print(sys.stderr, "Oracle Message: ", error.message)


if __name__=="__main__":
	establishConnection()
