import sys
import datetime
import cx_Oracle
import time
import random
import string
from random import randint

def vinInDB(VIN):
	## Returns true if the given VIN is on the database
	## Returns false for now...
	VIN = VIN.upper()

	curs = connection.cursor()
	statement = "select v.serial_no from vehicle v where v.serial_no = '" + str(VIN) + "'"
	curs.execute(statement)
	rows = curs.fetchall()

	if len(rows) > 0:
		curs.close()
		return True
	curs.close()
	return False
	

def printVTypes():
	## Take a list of vehicle types from the DB and print them
	## Print misc list for now...
	listOfVtypes = list()

	curs = connection.cursor()
	statement = "select v.type from vehicle_type v"
	try:
		curs.execute(statement)
	except cx_Oracle.DatabaseError as exc:
		error, = exc.args
		print(sys.stderr, "Error Creating Vehicle statement: ", statement)
		print(sys.stderr, "Oracle code: ", error.code)
		print(sys.stderr, "Oracle message: ", error.message)

	rows = curs.fetchall()
	curs.close()

	for row in rows:
		listOfVtypes.append(row[0].strip())

	for i in range(len(listOfVtypes)):
		print("%d. %s" % (i+1,listOfVtypes[i]))

	return listOfVtypes
	

def isVType(vType):
	## Check to see if vType is in the list of vehicle types on the DB
	## Return true for now...
	return True

def createVehicle(serialNum, make, model, year, color, vType):
	#statement = "INSERT INTO vehicle VALUES ('" + str(serialNum) + "', '" + str(make) + "', '" + str(model) + "', " + str(year) + ", '" + str(color) + "', " + str(vType) + ")" 
	serialNum = serialNum.upper()
	make = make.upper()
	model = model.upper()
	color = color.upper()

	statement = "INSERT INTO vehicle VALUES ('%s', '%s', '%s', %s, '%s', %s)" % (serialNum, make, model, year, color, vType)	
	curs = connection.cursor()

	print("Creating vehicle now")

	try:
		curs.execute(statement)	
	except cx_Oracle.DatabaseError as exc:
		error, = exc.args
		print(sys.stderr, "Error Creating Vehicle statement: ", statement)
		print(sys.stderr, "Oracle code: ", error.code)
		print(sys.stderr, "Oracle message: ", error.message)

	connection.commit()
	curs.close()

def sinExists(SIN):
	## Checks to see if a SIN exists on the DB
	## Returns True for now..
	SIN = SIN.upper()

	curs = connection.cursor()
	statement = "select p.sin from people p where p.sin = '" + str(SIN) + "'"
	curs.execute(statement)
	rows = curs.fetchall()

	if len(rows) > 0:
		curs.close()
		return True
	curs.close()
	return False

def licenceExists(SIN):
	# Check to see if someone with sin SIN already has a license
	SIN = SIN.upper()

	curs = connection.cursor()
	statement = "select l.sin from drive_licence l where l.sin = '%s'" % (SIN)
	curs.execute(statement)
	rows = curs.fetchall()
	curs.close()

	if len(rows) > 0:
		return True
	return False

def removeLicence(SIN):
	# Remove licence owned by person with sin SIN
	SIN = SIN.upper()

	curs = connection.cursor()
	statement = "delete from drive_licence l where l.sin = '%s'" % SIN
	try:
		curs.execute(statement)
	except cx_Oracle.DatabaseError as exc:
		error, = exc.args
		print(sys.stderr, "Error removing license from Database")
		print(sys.stderr, "Oracle code: ", error.code)
		print(sys.stderr, "Oracle Message ", error.message)

	connection.commit()
	curs.close()


def DBgetPersonName(SIN):
	## Returns person at SIN's name
	SIN = SIN.upper()

	curs = connection.cursor()
	statement = "select p.name from people p where p.sin = '%s'" % (SIN)
	curs.execute(statement)
	rows = curs.fetchall()

	curs.close()
	return rows[0][0]

def DBgetPersonHeight(SIN):
	## Returns person at SIN's height
	SIN = SIN.upper()

	curs = connection.cursor()
	statement = "select p.height from people p where p.sin = '%s'" % (SIN)
	curs.execute(statement)
	rows = curs.fetchall()

	curs.close()
	return rows[0][0]

def DBgetPersonWeight(SIN):
	## Returns person at SIN's weight
	SIN = SIN.upper()

	curs = connection.cursor()
	statement = "select p.weight from people p where p.sin = '%s'" % (SIN)
	curs.execute(statement)
	rows = curs.fetchall()

	curs.close()
	return rows[0][0]

def DBgetPersonEyeColour(SIN):
	## Returns person at SIN's eye colour
	SIN = SIN.upper()

	curs = connection.cursor()
	statement = "select p.eyecolor from people p where p.sin = '%s'" % (SIN)
	curs.execute(statement)
	rows = curs.fetchall()

	curs.close()
	return rows[0][0]

def DBgetPersonHairColour(SIN):
	## Returns person at SIN's hair colour
	SIN = SIN.upper()

	curs = connection.cursor()
	statement = "select p.haircolor from people p where p.sin = '%s'" % (SIN)
	curs.execute(statement)
	rows = curs.fetchall()

	curs.close()
	return rows[0][0]

def DBgetPersonAddress(SIN):
	## Returns person at SIN's address
	SIN = SIN.upper()

	curs = connection.cursor()
	statement = "select p.addr from people p where p.sin = '%s'" % (SIN)
	curs.execute(statement)
	rows = curs.fetchall()

	curs.close()
	return rows[0][0]

def DBgetGender(SIN):
	## Returns person at SIN's gender
	SIN = SIN.upper()

	curs = connection.cursor()
	statement = "select p.gender from people p where p.sin = '%s'" % (SIN)
	curs.execute(statement)
	rows = curs.fetchall()

	curs.close()
	return rows[0][0]

def DBgetBirthday(SIN):
	## Returns person at SIN's birthday
	SIN = SIN.upper()

	curs = connection.cursor()
	statement = "select p.birthday from people p where p.sin = '%s'" % (SIN)
	curs.execute(statement)
	rows = curs.fetchall()

	curs.close()
	return rows[0][0]

def registerOwner(VIN, SIN):
	## Registers the owner with the VIN on the database
	# Add row to owners table with values (SIN, VIN, y/n)
	SIN = SIN.upper()
	VIN = VIN.upper()

	curs = connection.cursor()
	statement = ("INSERT INTO owner VALUES('%s', '%s', 'y')" % (SIN, VIN))
	try:
		curs.execute(statement)
	except cx_Oracle.DatabaseError as exc:
		error, = exc.args
		print(sys.stderr, "Error Regostering owner: ", statement)
		print(sys.stderr, "Oracle code: ", error.code)
		print(sys.stderr, "Oracle message: ", error.message)

	connection.commit()
	curs.close()

def registerSecondary(VIN, SIN):
	SIN = SIN.upper()
	VIN = VIN.upper()

	curs = connection.cursor()
	statement = ("INSERT INTO owner VALUES('%s', '%s', 'n')" % (SIN, VIN))
	try:
		curs.execute(statement)
	except cx_Oracle.DatabaseError as exc:
		error, = exc.args
		print(sys.stderr, "Error Regostering seconday owner: ", statement)
		print(sys.stderr, "Oracle code: ", error.code)
		print(sys.stderr, "Oracle message: ", error.message)

	connection.commit()
	curs.close()


	return True

def createPerson(SIN, name, height, weight, eyeColour, hairColour, addr, gender, birthday):
	## Creates a person on the database
	SIN = SIN.upper()
	name = name.upper()
	eyeColour = eyeColour.upper()
	hairColour = hairColour.upper()
	addr = addr.upper()

	curs = connection.cursor()
	statement = ("INSERT INTO people VALUES('" + str(SIN) + "', '" + str(name) + "', " + str(height)+ ", " + str(weight)+ ", '" + str(eyeColour) + "', '" + str(hairColour) + "', '" + str(addr) + "', '" + str(gender) + "', '" + str(birthday) + "')")
	try:
		curs.execute(statement)
	except cx_Oracle.DatabaseError as exc:
		error, = exc.args
		print(sys.stderr, "Error Creating Person: ", statement)
		print(sys.stderr, "Oracle code: ", error.code)
		print(sys.stderr, "Oracle message: ", error.message)

	connection.commit()
	curs.close()
	
	


def tryRegisterPrimary(VIN):

	# Get SIN 
	while(True):
		SIN = input("Please enter Primary Owner SIN: ")
		print ("is %s correct? " % SIN)
		ans = getYN()
		if ans == 'n':
			continue
		# Check if SIN is in DB
		#if SIN doesnt exist, prompt to create new person
		if sinExists(SIN) == False:
			print("A person with that SIN doesn't exist, would you like to create one?")
			ans = getYN()
			if ans == 'n':
				continue
			#create new person
			while (True):
				name = input("Person's name: ")
				height = input("Person's height: ")
				weight = input("Person's weight: ")
				eyeColour = input("Person's eye colour: ")
				hairColour = input("Person's hair colour: ")
				addr = input("Person's address: ")
				while (True):
					gender = input("Person's gender [m/f]: ")
					gender = gender.lower()
					if (gender == "m" or gender == "f"):
						break
					else:
						print ("Sorry, that's not a valid option!")
						print ("Please select from either 'm' or 'f'")
				birthday = input("Person's birthday [DD-MON-YY]: ")
						
				print ("\nName: %s\nHeight: %s\nWeight: %s\nHair Colour: %s\nHair Colour: %s\nAddress: %s\nGender: %s\nBirthday: %s" % (str(name), str(height), str(weight), str(eyeColour), str(hairColour), str(addr), str(gender), str(birthday)))
				print ("Is this information correct?")
				ans = getYN()
				if ans == 'n':
					continue
				createPerson(SIN, name.lower(), height, weight, eyeColour.lower(), hairColour.lower(), addr.lower(), gender, birthday)
				break
		else:
			name = DBgetPersonName(SIN)
			height = DBgetPersonHeight(SIN)
			weight = DBgetPersonWeight(SIN)
			eyeColour = DBgetPersonEyeColour(SIN)
			hairColour = DBgetPersonHairColour(SIN)
			addr = DBgetPersonAddress(SIN)
			gender = DBgetGender(SIN)
			birthday = DBgetBirthday(SIN)

			print ("\nName: %s\nHeight: %s\nWeight: %s\nHair Colour: %s\nHair Colour: %s\nAddress: %s\nGender: %s\nBirthday: %s" % (str(name), str(height), str(weight), str(eyeColour), str(hairColour), str(addr), str(gender), str(birthday.strftime('%d-%b-%y'))))
			print ("Is this the person you're looking for?")
			ans = getYN()
			if ans == 'n':
				continue

		# Person definitely exists now
		# So time to finish off registration
		print ("Registering Vehicle VIN: %s with Primary Owner: %s" % (VIN, SIN))
		registerOwner(VIN, SIN)
		break

def tryRegisterSecondary(VIN):
	# Get SIN 
	while(True):
		SIN = input("Please enter Secondary Owner SIN: ")
		print ("is %s correct? " % SIN)
		ans = getYN()
		if ans == 'n':
			continue
		# Check if SIN is in DB
		#if SIN doesnt exist, prompt to create new person
		if sinExists(SIN) == False:
			print("A person with that SIN doesn't exist, would you like to create one?")
			ans = getYN()
			if ans == 'n':
				continue
			#create new person
			while (True):
				name = input("Person's name: ")
				height = input("Person's height: ")
				weight = input("Person's weight: ")
				eyeColour = input("Person's eye colour: ")
				hairColour = input("Person's hair colour: ")
				addr = input("Person's address: ")
				while (True):
					gender = input("Person's gender [m/f]: ")
					gender = gender.lower()
					if (gender == "m" or gender == "f"):
						break
					else:
						print ("Sorry, that's not a valid option!")
						print ("Please select from either 'm' or 'f'")
				birthday = input("Person's birthday [DD-MON-YY]: ")
						
				print ("\nName: %s\nHeight: %s\nWeight: %s\nHair Colour: %s\nHair Colour: %s\nAddress: %s\nGender: %s\nBirthday: %s" % (str(name), str(height), str(weight), str(eyeColour), str(hairColour), str(addr), str(gender), str(birthday)))
				print ("Is this information correct?")
				ans = getYN()
				if ans == 'n':
					continue
				createPerson(SIN, name.lower(), height, weight, eyeColour.lower(), hairColour.lower(), addr.lower(), gender, birthday)
				break
		else:
			name = DBgetPersonName(SIN)
			height = DBgetPersonHeight(SIN)
			weight = DBgetPersonWeight(SIN)
			eyeColour = DBgetPersonEyeColour(SIN)
			hairColour = DBgetPersonHairColour(SIN)
			addr = DBgetPersonAddress(SIN)
			gender = DBgetGender(SIN)
			birthday = DBgetBirthday(SIN)

			print ("\nName: %s\nHeight: %s\nWeight: %s\nHair Colour: %s\nHair Colour: %s\nAddress: %s\nGender: %s\nBirthday: %s" % (str(name), str(height), str(weight), str(eyeColour), str(hairColour), str(addr), str(gender), str(birthday.strftime('%d-%b-%y'))))
			print ("Is this the person you're looking for?")
			ans = getYN()
			if ans == 'n':
				continue

		# Person definitely exists now
		# So time to finish off registration
		print ("Registering Vehicle VIN: %s with Secondary Owner: %s" % (VIN, SIN))
		registerSecondary
		break



## On Main Menu Selection 1
def startNVR():
	print ("New Vehicle Registration Selected")
	
	while (True):
		#removed int typecast, as VIN can have letters in it
		VIN = input("Please enter the new vehicle's serial number: ")
		
		# Check if VIN in DB. If VIN in DB and dont want to try again, quit to main
		if (vinInDB(VIN)):
			print ("Sorry, that VIN already exists in the database. Would you like to try again?")
			ans = getYN()
			if ans == 'y':
				continue
			else:
				break


		print ("Let's fill in the vehicle's details...")
		serialNum = VIN
		make = input("Vehicle make: ")
		model = input("Vehicle model: ")
		year = input("Vehicle year: ") ## Check this to make sure it's a valid year
		color = input("Vehicle colour: ")
	
		while (True):
			listOfTypes = printVTypes()
			vType = input("Select a vehicle type from the list: ")
			
			try:
				vType = int(vType)
			except:
				print("Please enter an integer")
				continue


			if (vType) > len(listOfTypes):
				print("That is not a valid option")
				continue
			vNum = vType
			vType = listOfTypes[vType - 1]
			break

		# Output entered info for final check
		print("")
		print("Serial: %s\nMake: %s\nModel: %s\nYear: %s\nColour: %s\nType: %s\n" % (str(serialNum), str(make), str(model), str(year), str(color), str(vType)))
		print("Is this information correct?")
		ans = getYN()
		if ans == 'n':
			continue
		createVehicle(serialNum, make, model, year, color, vNum)
		# Register the primary owner	
		tryRegisterPrimary(VIN)		
		print ("\nThank you for registering this vehicle.")

		while(True):
			print("Would you like to add a secondary owner? ")
			ans = getYN()
			if ans == 'n':
				print("Exiting to main menu...")
				break
			if ans == 'y':
				tryRegisterSecondary(VIN)
		break		
		
		
			
	

def startAT():
	print ("Auto Transaction Selected")
	while (True):

		VIN = input("Please enter the vehicle's serial number: ")
			
		if (vinInDB(VIN) == False):
			print ("Sorry, that VIN doesn't exist. Would you like to sell a different vehicle?")
			ans = getYN()
			if ans == 'n':
				break
			else:
				continue				

		while(True):
			sellerSIN = input("Please enter the seller's SIN: ")
		
			if (sinExists(sellerSIN) == False):
				print("Sorry, that SIN doesn't exist... would you like to enter a different seller?")
				ans = getYN()
				if ans == 'n':
					break
				else:
					continue

			## GET PERSON'S DATA FROM DB
			else:
				sellerName = DBgetPersonName(sellerSIN)
				sellerHeight = DBgetPersonHeight(sellerSIN)
				sellerWeight = DBgetPersonWeight(sellerSIN)
				sellerEyeColour = DBgetPersonEyeColour(sellerSIN)
				sellerHairColour = DBgetPersonHairColour(sellerSIN)
				sellerAddr = DBgetPersonAddress(sellerSIN)
				sellerGender = DBgetGender(sellerSIN)
				sellerBirthday = DBgetBirthday(sellerSIN)
			
				print ("\nName: %s\nHeight: %s\nWeight: %s\nHair Colour: %s\nHair Colour: %s\nAddress: %s\nGender: %s\nBirthday: %s" % (sellerName, sellerHeight, sellerWeight, sellerEyeColour, sellerHairColour, sellerAddr, sellerGender, str(sellerBirthday.strftime('%d-%b-%y'))))
				print ("Is this the person you're looking for?")
				ans = getYN()
				if ans == 'n':
					continue


			break
		## Check to see if the selected sellerSIN owns the VIN
		if (checkSellerOwnsVehicle(sellerSIN, VIN) == False):
			print("Sorry, that person doesn't own this vehicle. \nwould you like to try a different vehicle?")
			ans = getYN()
			if ans == 'y':
				continue
			else:
				break

		## Get the buyer's information...
		buyerBool = True
		while(buyerBool == True):
			## COPIED DIRECTLY FROM ABOVE CODE...
			buyerSIN = input("Please enter the buyer's SIN: ")
		
			## CREATE A PERSON IN THE DB
			if (sinExists(buyerSIN) == False):
				print("Sorry, that SIN doesn't exist...")
				ans = True
				while (ans == True):
					print ("Would you like to create a new instance in the system?")
					answer = input("[Y/N]: ")
					answer = answer.lower()
					if (answer == "y" or answer == ""):
						while (True):
							name = input("Person's name: ")
							i = True
							height = input("Person's height: ")
							
							weight = input("Person's weight: ")

							eyeColour = input("Person's eye colour: ")
							hairColour = input("Person's hair colour: ")
							addr = input("Person's address: ")
							while (True):
								gender = input("Person's gender [m/f]: ")
								gender = gender.lower()
								if (gender == "m" or gender == "f"):
									break
								else:
									print ("Sorry, that's not a valid option!")
									print ("Please select from either 'm' or 'f'")
							birthday = input("Person's birthday [DD-MON-YY]: ")
						
							print ("\nName: %s\nHeight: %s\nWeight: %s\nHair Colour: %s\nHair Colour: %s\nAddress: %s\nGender: %s\nBirthday: %s" % (name, height, weight, eyeColour, hairColour, addr, gender, birthday))
							print ("Is this information correct?")
			
							answer = input("[Y/N] (q to quit): ")
							answer = answer.lower()
							if (answer == "y" or answer == ""):
								createPerson(buyerSIN, name.lower(), height, weight, eyeColour.lower(), hairColour.lower(), addr.lower(), gender, birthday)
								ans = False
								buyerBool = False
								break
							elif (answer == "n"):
								print ("Please re-enter the information:\n")
								continue
							elif (answer == "q"):
								main()
							else:
								print ("Sorry, that's not a valid option!")

					elif (answer == "n"):
						break
					else:
						print ("Sorry, that's not a valid option!")

				if (buyerBool):
					continue
			

			## GET PERSON'S DATA FROM DB
			else:
				buyerName = DBgetPersonName(buyerSIN)
				buyerHeight = DBgetPersonHeight(buyerSIN)
				buyerWeight = DBgetPersonWeight(buyerSIN)
				buyerEyeColour = DBgetPersonEyeColour(buyerSIN)
				buyerHairColour = DBgetPersonHairColour(buyerSIN)
				buyerAddr = DBgetPersonAddress(buyerSIN)
				buyerGender = DBgetGender(buyerSIN)
				buyerBirthday = DBgetBirthday(buyerSIN)
			
				while(True):
					print ("\nName: %s\nHeight: %s\nWeight: %s\nHair Colour: %s\nHair Colour: %s\nAddress: %s\nGender: %s\nBirthday: %s" % (buyerName, buyerHeight, buyerWeight, buyerEyeColour, buyerHairColour, buyerAddr, buyerGender, str(buyerBirthday.strftime('%d-%b-%y'))))
					print ("Is this the person you're looking for?")
					answer = input("[Y/N]: ")
					answer = answer.lower()

					if (answer == "y" or answer == ""):
						buyerBool = False
						break
					elif (answer == "n"):
						buyerBool = True
						break
					else:
						print ("Sorry, that's not a valid option!")
			
			if (buyerBool):
				continue
			else:
				break
	
		## Ask for the vehicle price
		vehPrice = input("What is the selling price of this vehicle? ")

		dateOfSale = input("Please enter the date of sale in format [DD-MON-YY]: ")
		removeVehicleOwners(VIN)
		addOwner(VIN, buyerSIN)
		transactionID = generateID()
		createAutoSale(transactionID, VIN, sellerSIN, buyerSIN, vehPrice, dateOfSale)
		print("Thank you for reporting this sale!")
		print("Returning to the main menu...\n\n")
		break
		

def DBgetVehicleMake(VIN):
	## Returns the make of vehicle at VIN
	VIN = VIN.upper()
	curs = connection.cursor()
	statement = "SELECT v.maker from vehicle v where v.serial_no = '%s'" % (VIN)
	curs.execute(statement)
	rows = curs.fetchall()

	curs.close()
	return rows[0][0]

def DBgetVehicleModel(VIN):
	## Returns the model of vehicle at VIN
	VIN = VIN.upper()	
	curs = connection.cursor()
	statement = "SELECT v.model from vehicle v where v.serial_no = '%s'" % (VIN)
	curs.execute(statement)
	rows = curs.fetchall()

	curs.close()
	return rows[0][0]

def DBgetVehicleYear(VIN):
	## Returns the year of the vehicle at VIN
	VIN = VIN.upper()
	curs = connection.cursor()
	statement = "SELECT v.year from vehicle v where v.serial_no = '%s'" % (VIN)
	curs.execute(statement)
	rows = curs.fetchall()

	curs.close()
	return rows[0][0]

def DBgetVehicleColor(VIN):
	## Returns the color of the vehicle at VIN
	VIN = VIN.upper()
	curs = connection.cursor()
	statement = "SELECT v.color from vehicle v where v.serial_no = '%s'" % (VIN)
	curs.execute(statement)
	rows = curs.fetchall()

	curs.close()
	return rows[0][0]

def createAutoSale(transactionID, VIN, sellerSIN, buyerSIN, vehPrice, dateOfSale):
	## Creates a row in the auto_sale table with all the values above
	## The current date will be put in for the s_date variable
	transactionID = transactionID.upper()
	VIN = VIN.upper()
	sellerSIN = sellerSIN.upper()
	buyerSIN = buyerSIN.upper()
	vehPrice = vehPrice.upper()


	curs = connection.cursor()
	statement = "INSERT INTO auto_sale VALUES(%s, '%s', '%s', '%s', '%s', %s)" % (transactionID, sellerSIN, buyerSIN, VIN, dateOfSale, vehPrice)
	try:
		curs.execute(statement)
	except cx_Oracle.DatabaseError as exc:
		error, = exc.args
		print(sys.stderr, "Error adding new auto sale to database")
		print(sys.stderr, "Oracle code: ", error.code)
		print(sys.stderr, "Oracle Message ", error.message)
	
	connection.commit()
	curs.close()	


	print ("Auto sale created...")

def generateID():
	##Creates a random number to be used for auto sale transaction 
	idNum = ''.join(random.choice(string.digits) for i in range(6))
	idNum = idNum.upper()
	while transIDinDB(idNum):
		licenceNum = ''.join(random.choice(string.digits) for i in range(6))	
	return idNum

def transIDinDB(idNum):
	#Checks if a transaction id already exists
	idNum = idNum.upper()
	curs = connection.cursor()
	statement = "select a.transaction_id from auto_sale a where a.transaction_id = '%s'" % idNum
	curs.execute(statement)
	rows = curs.fetchall()

	curs.close()
	if len(rows) > 0:
		return True
	return False

def licenceNumInDB(NUM):
	# Checks if licence number is already in DB
	NUM = NUM.upper()
	curs = connection.cursor()
	statement = "select l.licence_no from drive_licence l where l.licence_no = '%s'" % NUM
	curs.execute(statement)
	rows = curs.fetchall()

	curs.close()
	if len(rows) > 0:
		return True
	return False

	
def addOwner(VIN, buyerSIN):
	## Adds an owner to the vehicle at VIN as a primary owner...
	VIN = VIN.upper()
	buyerSIN = buyerSIN.upper()


	curs = connection.cursor()
	statement = "INSERT INTO owner VALUES ('%s', '%s', 'y')" % (buyerSIN, VIN)

	try:
		curs.execute(statement)
	except cx_Oracle.DatabaseError as exc:
		error, = exc.args
		print(sys.stderr, "Error adding new owner to database")
		print(sys.stderr, "Oracle code: ", error.code)
		print(sys.stderr, "Oracle Message ", error.message)
	
	connection.commit()
	curs.close()	

def removeVehicleOwners(VIN):
	## Removes all owners associated with the vehicle at the VIN, even if there are none available
	## Returns nothing
	VIN = VIN.upper()

	curs = connection.cursor()
	statement = "delete from owner o where o.vehicle_id = '%s'" % VIN 

	try:
		curs.execute(statement)
	except cx_Oracle.DatabaseError as exc:
		error, = exc.args
		print(sys.stderr, "Error removing owners from database")
		print(sys.stderr, "Oracle code: ", error.code)
		print(sys.stderr, "Oracle Message ", error.message)

	connection.commit()
	curs.close()

def checkSellerOwnsVehicle(sellerSIN, VIN):
	## Checks to see if anyone other than sellerSIN is associated with the VIN
	## Returns True if seller or nobody owns; False if someone else is the primary owner
	sellerSIN = sellerSIN.upper()
	VIN = VIN.upper()

	curs = connection.cursor()
	statement = "SELECT * from owner o where o.vehicle_id = '%s'" % (VIN)
	curs.execute(statement)
	rows = curs.fetchall()

	sellable = False
	for row in rows:
		if row[0].strip() == sellerSIN and row[2] == 'y':
			sellable = True
	
	curs.close()
	if sellable:
		return True
	return False 
			

def startDLR():
	print ("Driver License Registration Selected")
	
	# acquire the SIN of the person being registered. 
	# If that sin is not yet in the DB then create new person to go along with it
	while(True):
		#prompt user for SIN, check if SIN is already in DB
		SIN = input("Please enter the SIN of the person you wish to register: ")
		if (sinExists(SIN) == True):
			print("Is this the person you were looking for?: ")
			#print info of person SIN
			Name = DBgetPersonName(SIN)
			Height = DBgetPersonHeight(SIN)
			Weight = DBgetPersonWeight(SIN)
			EyeColour = DBgetPersonEyeColour(SIN)
			HairColour = DBgetPersonHairColour(SIN)
			Addr = DBgetPersonAddress(SIN)
			Gender = DBgetGender(SIN)
			Birthday = DBgetBirthday(SIN)

			print ("\nName: %s\nHeight: %s\nWeight: %s\nHair Colour: %s\nHair Colour: %s\nAddress: %s\nGender: %s\nBirthday: %s" % (Name, Height, Weight, EyeColour, HairColour, Addr, Gender, Birthday))
			ans = getYN()
			if (ans == 'n'):
				continue
			else:
				break
		else:
			print("That Person does not exist, would you like to add them?: ")
			ans = getYN()
			if ans == 'n':
				continue
			else:
				#add person to DB
				while (True):
					name = input("Person's name: ")
					height = input("Person's height: ")
					weight = input("Person's weight: ")
					eyeColour = input("Person's eye colour: ")
					hairColour = input("Person's hair colour: ")
					addr = input("Person's address: ")
					while (True):
						gender = input("Person's gender [m/f]: ")
						gender = gender.lower()
						if (gender == "m" or gender == "f"):
							break
						else:
							print ("Sorry, that's not a valid option!")
							print ("Please select from either 'm' or 'f'")
				
					birthday = input("Person's birthday [DD-MON-YY]: ")
					print ("\nName: %s\nHeight: %s\nWeight: %s\nHair Colour: %s\nHair Colour: %s\nAddress: %s\nGender: %s\nBirthday: %s" % (name, height, weight, eyeColour, hairColour, addr, gender, birthday))
					print ("Is this information correct?")
					ans = getYN()

					if (ans == 'y'):
						print ("Adding person to DB")
						createPerson(SIN, name.lower(), height, weight, eyeColour.lower(), hairColour.lower(), addr.lower(), gender, birthday)
						break
					else:
						continue
				break			

	# SIN of person to be added is in SIN, and person definitely exists
	# Check if person already has a license
	if licenceExists(SIN):
		print("That person already has a license,\nwould you like to remove their old license?")
		ans = getYN()
		if ans == 'y':
			removeLicence(SIN)
		else:
			print("License will not be altered\nExiting...")
			return 



	# Create License
	drivingClass = input("Please enter a driving class: ")

	issueDate = input("Please enter an issue date [DD-MON-YY], or 'n' for today's date: ")
	if issueDate == 'n':
		issueDate = time.strftime("%d-%b-%y")

	while(True):
		try:
			yearsValid = int(input("please enter number of years license will be valid: "))
		except:
			print("Make sure entry is an integer")
			continue
		break

	expireDate = issueDate[:]
	newYear = int(expireDate[len(expireDate)-2 :])
	newYear += yearsValid

	expireDate = expireDate[:len(expireDate)-2]
	expireDate += str(newYear)

	while(True):
		photo = 'NULL'
		pathToPhoto = input("Please Provide an absolute path to the photo: ")
		try:
			image = open(pathToPhoto, 'rb')
			photo = image.read()
		except:
			print("Error opening image.")
			continue
		break

	photo = 'NULL'


	licenceNum = ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(15))
	while licenceNumInDB(licenceNum):
		licenceNum = ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(15))


	createLicence(licenceNum, SIN, drivingClass, photo, issueDate, expireDate)
	print("Created licence for: %s" % DBgetPersonName(SIN))


def displayPossibleViolations():
	## Prints unique violations as they exist in the table "ticket_type"
	## For the user's reference

	return True


def checkViolationExists(violationType):
	## Checks to see if the violationType argument exists in the "ticket_type"
	## Returns True for now...
	return True

def stringToDate(dateString):
	## Turns a string to a date
	return True

def createViolation(ticketNumber, violatorSIN, vehicleID, violationType, issueDate, place, descriptions):
	## Creates a violation row in the ticket table
	return True

def generateTicketNumber():
	## Generates a random number
	return randint(4000,90000)

def startVR():
	print ("Violation Record Selected")


	while(True):

		# Ask to enter badge number
		officerID = input("Please enter the issuing officer's SIN: ")
		if (sinExists(officerID) == False): ## CHANGE TO TRUE

			# Ask for violator's SIN
			while(True):
				violatorSIN = input("Please enter the violator's SIN: ")
				if (sinExists(violatorSIN) == False): ## CHANGE TO TRUE
					
					# Ask for the vehicle VIN
					while(True):
						vehicleVIN = input("Please enter the vehicle VIN: ")
						if(vinInDB(vehicleVIN) == False):
							
							# Ask for the type of offense
							print("Please select a violation from the list below: \n")
							displayPossibleViolations()

							while (True):
								violationType = input("\nTicket violation: ")
								violationCheck = checkViolationExists(violationType)
					
								if (violationCheck):

									# Ask for the date of the ticket
									issueDate = input("Please enter the date for which the ticket will be issued [DD-MON-YY] or type 'today' for today's date: ")

									if (issueDate == "today"):
										issueDate = time.strftime("%d-%b-%y")
									else:
										issueDate = stringToDate(issueDate)
									# Ask for a place
									place = input("Please enter the place of the violation: ")

									# Ask for additional descriptions
									while (True):
										descriptions = input("Please input any extra descriptions: ")	
										if(len(descriptions) < 1024):
									
											# Allow the user to review before submitting
											print("Please review this information:\n")
				
											#officerName = DBgetPersonName(officerID)
											#violatorName = DBgetPersonName(violatorSIN)
											officerName = "Bob"
											violatorName = "Jimbo"

											print("Issuing officer name: %s\nViolator name: %s\nVIN: %s\nViolation type: %s\nViolation date: %s\nPlace: %s\nDescriptions: %s\n" % (officerName, violatorName, vehicleVIN, violationType, issueDate, place, descriptions))
											print ("Is this information correct?: ")
											ans = getYN()
											if (ans == 'y'):
												ticketNumber = generateTicketNumber()
												createViolation(ticketNumber, violatorSIN, vehicleVIN, violationType, issueDate, place, descriptions)
												print("Thank you for submitting this ticket.\nReturning to the main menu.")
												main()
										
											else:
												print("Please try the process again.")
												startVR()

											# Generate random ticket_no
										else:
											print("Sorry, that description is too long. Please try again \n")
											break
								else:
									print ("Sorry, that ticket violation does not exist. Please try again.")
									break

								## END
						else:
							print("That VIN does not exist in the database. Please enter a valid one.")
							continue

				else:
					print("Sorry, there is nobody listed under that SIN. \n")
					print("Would you like to try again?")
					ans = getYN()
					if (ans == 'y'):
						continue
					else:
						print("Would you like to enter a new officer?")
						ans = getYN()
						if (ans == 'y'):
							startVR()
						else:
							main()


		else:
			print("Sorry, there is nobody listed under that SIN. \n")
			print("Would you like to try again?")
			ans = getYN()
			if (ans == 'y'):
				continue
			else:
				main()

	

def startSE():
	print ("Search Engine Selected")

	while (True):
		userInput = input("""PLEASE CHOOSE A SEARCH OPTION:
	1. Licence Number
	2. Name 
Select [1/2]: """)
		if userInput == '1' or userInput == '2':
			break
		else:
			print("Please enter a valid input")
	
	if userInput == '1':
		# Search by licence Number
		licence = input("Please enter a licence number to search by: ")
		results = searchLicence(licence)
		print("== Results =========")

		for row in results:
			name = row[0].strip()
			licence_no = row[1].strip()
			addr = row[2].strip()
			birthday = row[3]
			dClass = row[4].strip()
			dCondition = row[5].strip()
			expDate = row[6]

			print("Name: %s\nLicence Number: %s\nAddress: %s\nBirthday: %s\nDriving Class: %s\nDriving Condition: %s\nExpiration Date: %s\n") % (name, licence_no, addr, birthday, dClass, dCondition, expDate)

	if userInput == '2':
		# Search by Name
		name = input("Please enter a name to search by: ")
		results = searchName(name)
		print("== Results =========")

		for row in results:
			name = row[0].strip()
			licence_no = row[1].strip()
			addr = row[2].strip()
			birthday = row[3]
			dClass = row[4].strip()
			dCondition = row[5].strip()
			expDate = row[6]

			print("Name: %s\nLicence Number: %s\nAddress: %s\nBirthday: %s\nDriving Class: %s\nDriving Condition: %s\nExpiration Date: %s\n") % (name, licence_no, addr, birthday, dClass, dCondition, expDate)


def searchLicence(licence):
	#returns search results from licence 
	# Need to Add Joins for people without restrictions and such
	licencse = licencse.upper()
	curs = connection.cursor()
	statement = "select p.name, l.licence_no, p.addr, p.birthday, l.class, dc.description, l.expiring_date from people p, drive_licence l, driving_condition dc, restriction r where p.sin = l.sin and l.licence_no = r.licence_no and dc.c_id = r.r_id and l.licence_no = '%s'" % licence
	curs.execute(statement)
	rows = curs.fetchall()
	curs.close()
	
	return rows

def searchName(name):
	#returns search results from name
	# Need to Add Joins for people without restrictions and such
	name = name.upper()
	curs = connection.cursor()
	statement = "select p.name, l.licence_no, p.addr, p.birthday, l.class, dc.description, l.expiring_date from people p, drive_licence l, driving_condition dc, restriction r where p.sin = l.sin and l.licence_no = r.licence_no and dc.c_id = r.r_id and p.name = '%s'" % name
	curs.execute(statement)
	rows = curs.fetchall()
	curs.close()
	
	return rows

def main():
	while(True):
		print ("""PLEASE SELECT FROM THE FOLLOWING OPTIONS:
	      1. New Vehicle Registration
	      2. Auto Transaction
	      3. Driver License Registration
	      4. Violation Record
	      5. Search Engine
	      6. Exit""")

		var = 0
		var = input("Select [1/2/3/4/5/6]: ")
		if (var == "1"):
			startNVR()
	
		elif (var == "2"):
			startAT()
	
		elif (var == "3"):
			startDLR()
	
		elif (var == "4"):
			startVR()
	
		elif (var == "5"):
			startSE()
	
		elif (var == "6"):
			print ("Exiting...")
			break

		else:
			print ("Sorry, that's not a valid option!")
	
	connection.close()
	sys.exit()
###################################################################################################
#
#                                                                                  ,---.,---.,---.    
# ,-----.,--.                           ,--.           ,-----.          ,--.       |   ||   ||   |    
#'  .--./|  ,---.  ,--,--. ,---.  ,---. |  |,---.     '  .--./ ,---.  ,-|  | ,---. |  .'|  .'|  .'    
#|  |    |  .-.  |' ,-.  |(  .-' | .-. :`-'(  .-'     |  |    | .-. |' .-. || .-. :|  | |  | |  |     
#'  '--'\|  | |  |\ '-'  |.-'  `)\   --.   .-'  `)    '  '--'\' '-' '\ `-' |\   --.`--' `--' `--'     
# `-----'`--' `--' `--`--'`----'  `----'   `----'      `-----' `---'  `---'  `----'.--. .--. .--.     
#                                                                                  '--' '--' '--'     
##################################################################################################

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

def getYN():
	while (True):
		answer = input("[Y/N]: ")
		answer = answer.lower()
		if answer == 'y' or answer == '':
			return 'y'
		elif answer == 'n':
			return 'n'
		else:
			continue

def createLicence(licenceNum, SIN, drivingClass, photo, issueDate, expireDate):
	# Creates a new licence with specifications
	licenceNum = licenceNum.upper()
	SIN = SIN.upper()
	drivingClass = drivingClass.upper()

	curs = connection.cursor()
	curs.setinputsizes(photo=cx_Oracle.BLOB)
	statement = "INSERT INTO drive_licence VALUES('%s', '%s', '%s', %s, '%s', '%s')" % (licenceNum, SIN, drivingClass, photo, issueDate, expireDate)
	try:
		curs.execute(statement)
	except cx_Oracle.DatabaseError as exc:
		error, = exc.args
		print(sys.stderr, "Error Adding new licence: ", statement)
		print(sys.stderr, "Oracle code: ", error.code)
		print(sys.stderr, "Oracle message: ", error.message)

	connection.commit()
	curs.close()

#!# a little clusterd right now, maybe consider a delegation function to clean up main
if __name__ =="__main__":
	connection = establishConnection('cmccarty', '4cidm4n67')
	#createTables("a2_setup_new.sql")
	#populateTables("a2-data.sql")

	# this will be merged with mainMenu later
	#createVehicle("1e37y6", "Lamborghini", "Hurican", 2014, "blue", "0001")
	#!# Run the main code here, like it says above this should all be refactored for prettiness anyway
	main()
	connection.close()



