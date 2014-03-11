import sys
import cx_Oracle

def establishConnection():

	createStr = ("create table TOFFEES "
            "(T_NAME VARCHAR(32), SUP_ID INTEGER, PRICE FLOAT, SALES INTEGER, TOTAL INTEGER)")

	try:
		connection = cx_Oracle.connect('cmccarty/4cidm4n67@gwynne.cs.ualberta.ca:1521/CRS')
		curs = connection.cursor()
		curs.execute("drop table TOFFEES")
		curs.execute(createStr)

		data = [('Quadbury', 101, 7.99, 0, 0),('Almond roca', 102, 8.99, 0, 0),('Golden Key', 103, 3.99, 0, 0)]
		cursInsert = connection.cursor()
		cursInsert.bindarraysize = 3
		cursInsert.setinputsizes(32,int,float,int,int)
		cursInsert.executemany("INSERT INTO TOFFEES (T_NAME, SUP_ID, PRICE, SALES, TOTAL)" "VALUES(:1,:2,:3,:4,:5)", data)
		connection.commit()

		curs.execute("SELECT * from TOFFEES")
		rows = curs.fetchall()
		for row in rows:
			print(row)
			
		curs.close()
		cursInsert.close()
		connection.close()

	except cx_Oracle.DatabaseError as exc:
		error = exc.args
		print(sys.stderr, "Oracle code: ", error.code)
		print(sys.stderr, "Oracle Message: ", error.message)


if __name__=="__main__":
	establishConnection()