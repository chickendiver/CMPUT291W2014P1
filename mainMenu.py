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
	curs = connection.cursor()
	statement = "select v.serial_no from vehicle v where v.serial_no = ('" + str(VIN) + "')"
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

	print("Searching for sin: %s" % SIN)

	curs = connection.cursor()
	statement = "select p.sin from people p where (p.sin) = ('" + str(SIN) + "')"
	curs.execute(statement)
	rows = curs.fetchall()

	if len(rows) > 0:
		curs.close()
		return True
	curs.close()
	return False

def licenceExists(SIN):
	# Check to see if someone with sin SIN already has a license
	curs = connection.cursor()
	statement = "select l.sin from drive_licence l where (l.sin) = ('%s')" % (SIN)
	curs.execute(statement)
	rows = curs.fetchall()
	curs.close()

	if len(rows) > 0:
		return True
	return False

def removeLicence(SIN):
	# Remove licence owned by person with sin SIN
	curs = connection.cursor()
	statement = "delete from drive_licence l where (l.sin) = ('%s')" % SIN
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

	curs = connection.cursor()
	statement = "select p.name from people p where (p.sin) = ('%s')" % (SIN)
	curs.execute(statement)
	rows = curs.fetchall()

	curs.close()
	return rows[0][0]

def DBgetPersonHeight(SIN):
	## Returns person at SIN's height

	curs = connection.cursor()
	statement = "select p.height from people p where (p.sin) = ('%s')" % (SIN)
	curs.execute(statement)
	rows = curs.fetchall()

	curs.close()
	return rows[0][0]

def DBgetPersonWeight(SIN):
	## Returns person at SIN's weight

	curs = connection.cursor()
	statement = "select p.weight from people p where (p.sin) = ('%s')" % (SIN)
	curs.execute(statement)
	rows = curs.fetchall()

	curs.close()
	return rows[0][0]

def DBgetPersonEyeColour(SIN):
	## Returns person at SIN's eye colour

	curs = connection.cursor()
	statement = "select p.eyecolor from people p where (p.sin) = ('%s')" % (SIN)
	curs.execute(statement)
	rows = curs.fetchall()

	curs.close()
	return rows[0][0]

def DBgetPersonHairColour(SIN):
	## Returns person at SIN's hair colour

	curs = connection.cursor()
	statement = "select p.haircolor from people p where (p.sin) = ('%s')" % (SIN)
	curs.execute(statement)
	rows = curs.fetchall()

	curs.close()
	return rows[0][0]

def DBgetPersonAddress(SIN):
	## Returns person at SIN's address

	curs = connection.cursor()
	statement = "select p.addr from people p where (p.sin) = ('%s')" % (SIN)
	curs.execute(statement)
	rows = curs.fetchall()

	curs.close()
	return rows[0][0]

def DBgetGender(SIN):
	## Returns person at SIN's gender

	curs = connection.cursor()
	statement = "select p.gender from people p where (p.sin) = ('%s')" % (SIN)
	curs.execute(statement)
	rows = curs.fetchall()

	curs.close()
	return rows[0][0]

def DBgetBirthday(SIN):
	## Returns person at SIN's birthday

	curs = connection.cursor()
	statement = "select p.birthday from people p where (p.sin) = ('%s')" % (SIN)
	curs.execute(statement)
	rows = curs.fetchall()

	curs.close()
	return rows[0][0]

def registerOwner(VIN, SIN):
	## Registers the owner with the VIN on the database
	# Add row to owners table with values (SIN, VIN, y/n)

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
				while(True):
					height = input("Person's height: ")
					try:
						float(height)
					except:
						print("please enter a decimal number")
						continue
					break
				while(True):
					weight = input("Person's weight: ")
					try:
						float(weight)
					except:
						print("please enter a decimal number")
						continue
					break
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
				while(True):
					birthday = input("Person's birthday [DD-MON-YY]: ")
					if not sanitizeYear(birthday):
						print("Improper date entered")
						continue
					break
						
				print ("\nName: %s\nHeight: %s\nWeight: %s\nHair Colour: %s\nHair Colour: %s\nAddress: %s\nGender: %s\nBirthday: %s" % (str(name), str(height), str(weight), str(eyeColour), str(hairColour), str(addr), str(gender), str(birthday)))
				print ("Is this information correct?")
				ans = getYN()
				if ans == 'n':
					continue
				createPerson(SIN, name, height, weight, eyeColour, hairColour, addr, gender, birthday)
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
				while(True):
					height = input("Person's height: ")
					try:
						float(height)
					except:
						print("please enter a decimal number")
						continue
					break
				while(True):
					weight = input("Person's weight: ")
					try:
						float(weight)
					except:
						print("please enter a decimal number")
						continue
					break
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

				while(True):
					birthday = input("Person's birthday [DD-MON-YY]: ")
					if not sanitizeYear(birthday):
						print("Invalid date entered")
						continue
					break
						
				print ("\nName: %s\nHeight: %s\nWeight: %s\nHair Colour: %s\nHair Colour: %s\nAddress: %s\nGender: %s\nBirthday: %s" % (str(name), str(height), str(weight), str(eyeColour), str(hairColour), str(addr), str(gender), str(birthday)))
				print ("Is this information correct?")
				ans = getYN()
				if ans == 'n':
					continue
				createPerson(SIN, name, height, weight, eyeColour, hairColour, addr, gender, birthday)
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
		while(True):
			year = input("Vehicle year: ") 
			try:
				int(year)
			except:
				print("Please enter an integer")
				continue
			break
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
							while(True):
								height = input("Person's height: ")
								try:
									float(height)
								except:
									print("Please enter a decimal number")
									continue
								break
							
							while(True):
								weight = input("Person's weight: ")
								try:
									float(weight)
								except:
									print("Please enter a decimal number")
									continue
								break

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
							while(True):
								birthday = input("Person's birthday [DD-MON-YY]: ")
								if not sanitizeYear(birthday):
									print("Improper Date Entered")
									continue
								break
						
							print ("\nName: %s\nHeight: %s\nWeight: %s\nHair Colour: %s\nHair Colour: %s\nAddress: %s\nGender: %s\nBirthday: %s" % (name, height, weight, eyeColour, hairColour, addr, gender, birthday))
							print ("Is this information correct?")
			
							answer = input("[Y/N] (q to quit): ")
							answer = answer.lower()
							if (answer == "y" or answer == ""):
								createPerson(buyerSIN, name, height, weight, eyeColour, hairColour, addr, gender, birthday)
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

		while(True):
			dateOfSale = input("Please enter the date of sale in format [DD-MON-YY]: ")
			if not sanitizeYear(dateOfSale):
				print("Improper date entered")
				continue
			break
		removeVehicleOwners(VIN)
		addOwner(VIN, buyerSIN)
		transactionID = generateID()
		createAutoSale(transactionID, VIN, sellerSIN, buyerSIN, vehPrice, dateOfSale)
		print("Thank you for reporting this sale!")
		print("Returning to the main menu...\n\n")
		break
		

def DBgetVehicleMake(VIN):
	## Returns the make of vehicle at VIN
	curs = connection.cursor()
	statement = "SELECT v.maker from vehicle v where (v.serial_no) = ('%s')" % (VIN)
	curs.execute(statement)
	rows = curs.fetchall()

	curs.close()
	return rows[0][0]

def DBgetVehicleModel(VIN):
	## Returns the model of vehicle at VIN
	curs = connection.cursor()
	statement = "SELECT v.model from vehicle v where (v.serial_no) = ('%s')" % (VIN)
	curs.execute(statement)
	rows = curs.fetchall()

	curs.close()
	return rows[0][0]

def DBgetVehicleYear(VIN):
	## Returns the year of the vehicle at VIN
	curs = connection.cursor()
	statement = "SELECT v.year from vehicle v where (v.serial_no) = ('%s')" % (VIN)
	curs.execute(statement)
	rows = curs.fetchall()

	curs.close()
	return rows[0][0]

def DBgetVehicleColor(VIN):
	## Returns the color of the vehicle at VIN
	curs = connection.cursor()
	statement = "SELECT v.color from vehicle v where (v.serial_no) = ('%s')" % (VIN)
	curs.execute(statement)
	rows = curs.fetchall()

	curs.close()
	return rows[0][0]

def createAutoSale(transactionID, VIN, sellerSIN, buyerSIN, vehPrice, dateOfSale):
	## Creates a row in the auto_sale table with all the values above
	## The current date will be put in for the s_date variable


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
	while transIDinDB(idNum):
		idNum = ''.join(random.choice(string.digits) for i in range(6))	
	return idNum

def transIDinDB(idNum):
	#Checks if a transaction id already exists
	curs = connection.cursor()
	statement = "select a.transaction_id from auto_sale a where (a.transaction_id) = ('%s')" % idNum
	curs.execute(statement)
	rows = curs.fetchall()

	curs.close()
	if len(rows) > 0:
		return True
	return False

def licenceNumInDB(NUM):
	# Checks if licence number is already in DB
	curs = connection.cursor()
	statement = "select l.licence_no from drive_licence l where (l.licence_no) = ('%s')" % NUM
	curs.execute(statement)
	rows = curs.fetchall()

	curs.close()
	if len(rows) > 0:
		return True
	return False

	
def addOwner(VIN, buyerSIN):
	## Adds an owner to the vehicle at VIN as a primary owner...


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

	curs = connection.cursor()
	statement = "delete from owner o where (o.vehicle_id) = ('%s')" % VIN 

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

	curs = connection.cursor()
	statement = "SELECT * from owner o where (o.vehicle_id) = ('%s')" % (VIN)
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
					while(True):
						height = input("Person's height: ")
						try:
							float(height)
						except:
							print("please enter a decimal number")
							continue
						break
					while(True):
						weight = input("Person's weight: ")
						try:
							float(weight)
						except:
							print("please enter a decimal number")
							continue
						break
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
				
					while(True):
						birthday = input("Person's birthday [DD-MON-YY]: ")
						if not sanitizeYear(birthday):
							print("Improper date entered")
							continue
						break

					print ("\nName: %s\nHeight: %s\nWeight: %s\nHair Colour: %s\nHair Colour: %s\nAddress: %s\nGender: %s\nBirthday: %s" % (name, height, weight, eyeColour, hairColour, addr, gender, birthday))
					print ("Is this information correct?")
					ans = getYN()

					if (ans == 'y'):
						print ("Adding person to DB")
						createPerson(SIN, name, height, weight, eyeColour, hairColour, addr, gender, birthday)
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

	while(True):
		issueDate = input("Please enter an issue date [DD-MON-YY], or 'n' for today's date: ")
		if issueDate == 'n':
			issueDate = time.strftime("%d-%b-%y")
		if not sanitizeYear(issueDate):
			print("Improper date entered")
			continue
		break

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


	licenceNum = ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(15))
	while licenceNumInDB(licenceNum):
		licenceNum = ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(15))


	createLicence(licenceNum, SIN, drivingClass, photo, issueDate, expireDate)
	print("Created licence for: %s" % DBgetPersonName(SIN))


def displayPossibleViolations():
	## Prints unique violations as they exist in the table "ticket_type"
	## For the user's reference
	curs = connection.cursor()
	statement = "select t.vtype from ticket_type t"
	curs.execute(statement)
	rows = curs.fetchall()

	possibleTickets = list()
	#for row in rows:
	#	row = row[0][0].split()

	for i in range(len(rows)):
		possibleTickets.append(rows[i][0].split()[0])
		print("%d. %s" % (i+1, str(rows[i][0].split()[0])))

	return possibleTickets



def createViolation(ticketNumber, violatorSIN, vehicleID, officerSIN, violationType, issueDate, place, descriptions):
	## Creates a violation row in the ticket table

	return True
	curs = connection.cursor()
	statement = "INSERT INTO ticket VALUES(%s, '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (ticketNumber, violatorSIN, vehicleID, officerSIN, violationType, issueDate, place, descriptions)

	try:
		curs.execute(statement)
	except cx_Oracle.DatabaseError as exc:
		
		statement = "INSERT INTO ticket VALUES(%s, '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (ticketNumber, violatorSIN, vehicleID, officerSIN, violationType, issueDate, place, descriptions)
		try:
			curs.execute(statement)
		except cx_Oracle.DatabaseError as exc:
			error, = exc.args
			print(sys.stderr, "Error creating new violation: ", statement)
			print(sys.stderr, "Oracle code: ", error.code)
			print(sys.stderr, "Oracle message: ", error.message)

	connection.commit()
	curs.close()

#List all violation records received by a person if  the drive licence_no or sin of a person  is entered.
def generateTicketNumber():
	## Generates a random number
	idNum = ''.join(random.choice(string.digits) for i in range(6))
	while ticketIDinDB(idNum):
		idNum = ''.join(random.choice(string.digits) for i in range(6))	
	return idNum

def ticketIDinDB(idNum):
	curs = connection.cursor()
	statement = "select a.ticket_no from ticket a where (a.ticket_no) = ('%s')" % idNum
	curs.execute(statement)
	rows = curs.fetchall()

	curs.close()
	if len(rows) > 0:
		return True
	return False



def startVR():
	print ("Violation Record Selected")

	while(True):
		# Ask to enter badge number
		officerID = input("Please enter the issuing officer's SIN: ")
		if (sinExists(officerID) == True): 

			# Ask for violator's SIN
			while(True):
				violatorSIN = input("Please enter the violator's SIN: ")
				if (sinExists(violatorSIN) == True): 
					
					# Ask for the vehicle VIN
					while(True):
						vehicleVIN = input("Please enter the vehicle VIN: ")
						if(vinInDB(vehicleVIN) == True):
							
							# Ask for the type of offense
							print("Please select a violation from the list below: \n")
							possibleTickets = displayPossibleViolations()

							while (True):
								violationType = input("\nTicket violation: ")
								try: 
									violationType = int(violationType)
								except:
									print("value enetered is not an integer")
									continue

								if violationType > len(possibleTickets):
									print("integer entered too large")
									continue
								if violationType < 1:
									print("integer entered too small")
									continue

								violationType = possibleTickets[violationType-1]
					
								# Ask for the date of the ticket
								while(True):
									issueDate = input("Please enter the date for which the ticket will be issued [DD-MON-YY] \nor type 'today' for today's date: ")
									if (issueDate == "today"):
										issueDate = str(time.strftime("%d-%b-%y"))
									if not sanitizeYear(issueDate):
										print("Improper date entered")
										continue
									break
									
								# Ask for a place
								place = input("Please enter the place of the violation: ")
								# Ask for additional descriptions
								while (True):
									descriptions = input("Please input any extra descriptions: ")	
									if(len(descriptions) < 1024):
								
										# Allow the user to review before submitting
										print("Please review this information:\n")
										officerName = DBgetPersonName(officerID)
										violatorName = DBgetPersonName(violatorSIN)
										print("Issuing officer name: %s\nViolator name: %s\nVIN: %s\nViolation type: %s\nViolation date: %s\nPlace: %s\nDescriptions: %s\n" % (officerName, violatorName, vehicleVIN, violationType, issueDate, place, descriptions))
										print ("Is this information correct?: ")
										ans = getYN()
										if (ans == 'y'):
											ticketNumber = generateTicketNumber()
											createViolation(ticketNumber, violatorSIN, vehicleVIN, officerID, violationType, issueDate, place, descriptions)
											print("Thank you for submitting this ticket.\nReturning to the main menu.")
											main()
									
										else:
											print("Please try the process again.")
											startVR()
											# Generate random ticket_no
									else:
										print("Sorry, that description is too long. Please try again \n")
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

	# Ask user to select search type
	# 1. Driver description
	# 2. Violation records
	# 3. Vehicle history

	while(True):
		searchInput = input("""PLEASE CHOOSE A SEARCH OPTION:
	1. Driver Description
	2. Violation Records	
	3. Vehicle history 
Select [1/2/3] [q to return to the main menu]: """)

		
		if searchInput == '1':
			while (True):
				userInput = input("""PLEASE CHOOSE A SEARCH OPTION:
			1. Licence Number
			2. Name 
		Select [1/2] [q for main menu]: """)
				if userInput == '1' or userInput == '2':
					break
				elif userInput == 'q':
					main()
				else:
					print("Please enter a valid input")
	
			if userInput == '1':
				# Search by licence Number
				licence = input("Please enter a licence number to search by: ")
				results = searchLicence(licence)
				print("== Results =========")

				#print (results)

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
		elif searchInput == '2':
			while(True):
				## 2. Violation records
				while(True):
					recordInput = input("""PLEASE CHOOSE A SEARCH OPTION:
				1. Licence Number
				2. SIN
			Select [1/2]: """)
					if recordInput == '1':
						## Search via licence number
						licenceInput = input("Please enter the licence to search by: ")
						searchLicenceViolation(licenceInput)
						break

					elif recordInput == '2':
						## Search via SIN
						SINInput = input("Please enter the SIN to search by: ")
						searchSINViolation(SINInput)
						pass

					elif recordInput == 'q':
						searchInput = 'NULL'
						break						
						
					else:
						print("Sorry, that's not an appropriate input.")	
						continue
				break
				
		elif searchInput == '3':	

			## 3. Vehicle history
			while(True):
				vehicleHistoryVIN = input ("Please enter the VIN of the vehicle in question: ")
				if (vinInDB(vehicleHistoryVIN)):
					searchVINHistory(vehicleHistoryVIN)
					break
				else:
					print("Sorry, that VIN is not in the DB. Please try again.")
					continue
		elif searchInput == 'q':
			main()
		else:
			print("That is not a valid option. Please try again.")	
			continue


def searchLicenceViolation(licenceInput):
	## Prints out all violation records for a licence_no
	curs = connection.cursor()
	statement = "select t.ticket_no, t.vdate, t.vtype, t.descriptions from ticket t, drive_licence dl where t.violator_no = dl.sin AND dl.licence_no = '%s'" % licenceInput
	curs.execute(statement)
	results = curs.fetchall()
	curs.close()

	for row in results:
		ticketNo = row[0]
		vDate = row[1]
		vType = row[2]
		descriptions = row[3]

		print("ticket number: %d\nviolation date: %s\nviolation type: %s\ndescriptions: %s\n" % (ticketNo, str(vDate.strftime('%d-%b-%y')), vType, descriptions))

def searchSINViolation(SINInput):
	## Prints out all violation records for a SIN
	curs = connection.cursor()
	statement = "select t.ticket_no, t.vdate, t.vtype, t.descriptions from ticket t, drive_licence dl where t.violator_no = dl.sin AND dl.sin = '%s'" % SINInput
	curs.execute(statement)
	results = curs.fetchall()
	curs.close()

	for row in results:
		ticketNo = row[0]
		vDate = row[1]
		vType = row[2]
		descriptions = row[3]

		print("ticket number: %d\nviolation date: %s\nviolation type: %s\ndescriptions: %s\n" % (ticketNo, str(vDate.strftime('%d-%b-%y')), vType, descriptions))

def searchVINHistory(VIN):
	## Prints history of the vehicle
	curs = connection.cursor()
	statement = "select counts.c, avgs.a, viols.cnt from (select count(*) as c from auto_sale where vehicle_id = '%s')counts, (select SUM(price)/count(*) as a from auto_sale where vehicle_id = '%s')avgs, (select count(*) as cnt from ticket where vehicle_id = '%s')viols" % (VIN, VIN, VIN)
	curs.execute(statement)
	results = curs.fetchall()
	curs.close()

	for row in results:
		salesCount = row[0]
		averagePrice = row[1]
		numberSales = row[2]

		print("Total sales: %d\nAverage price: %d\nNumber of tickets: %d\n" % (salesCount, averagePrice, numberSales))

def searchLicence(licence):
	# Returns search results from licence 
	# Need to Add Joins for people without restrictions and such
	curs = connection.cursor()
	statement = "select p.name, l.licence_no, p.addr, p.birthday, l.class, dc.description, l.expiring_date from people p, drive_licence l, driving_condition dc, restriction r where p.sin = l.sin and dc.c_id = r.r_id and l.licence_no = r.licence_no and (l.licence_no) = ('%s')" % licence
	curs.execute(statement)
	rows = curs.fetchall()
	curs.close()
	
	return rows

def searchName(name):
	# Returns search results from name
	# Need to Add Joins for people without restrictions and such
	curs = connection.cursor()
	statement = "select p.name, l.licence_no, p.addr, p.birthday, l.class, dc.description, l.expiring_date from people p, drive_licence l, driving_condition dc, restriction r where p.sin = l.sin and dc.c_id = r.r_id and l.licence_no = r.licence_no and UPPER(p.name) = UPPER('%s')" % name
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
def establishConnection():

	while(True):
		username = input("Please enter database username: ")
		password = input("Please enter database password: ")

		connectionString = (str(username) + "/" + str(password) + "@gwynne.cs.ualberta.ca:1521/CRS")
		connection = None 
		try:
			connection = cx_Oracle.connect(connectionString)
		
		except cx_Oracle.DatabaseError as exc:
			print("Invalid Credentials")
			continue
		break

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

	ValsArray = [licenceNum, SIN, drivingClass, photo, issueDate, expireDate]

	curs = connection.cursor()
	curs.setinputsizes(photo=cx_Oracle.BLOB)
	#statement = "INSERT INTO drive_licence VALUES('%s', '%s', '%s', '%s', '%s', '%s')" % (licenceNum, SIN, drivingClass, photo, issueDate, expireDate)
	try:
		#curs.execute(statement)
		curs.execute("INSERT INTO drive_licence values(:licence_no, :sin, :class, :photo, :issueDate, :expireDate)", {"licence_no":ValsArray[0], "sin":ValsArray[1], "class":ValsArray[2], "photo":ValsArray[3], "issueDate":ValsArray[4], "expireDate":ValsArray[5] })
	except cx_Oracle.DatabaseError as exc:
		error, = exc.args
		print(sys.stderr, "Error Adding new licence: ", statement)
		print(sys.stderr, "Oracle code: ", error.code)
		print(sys.stderr, "Oracle message: ", error.message)

	connection.commit()
	curs.close()

def sanitizeYear(year):
	#returns true if year is valid
	monthNames = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
	year = year.split('-')
	if len(year) != 3:
		return False
	try:
		int(year[0])
		int(year[2])
	except:
		return False

	month = year[1].lower()
	if not month in monthNames:
		return False
	return True

#!# a little clusterd right now, maybe consider a delegation function to clean up main
if __name__ =="__main__":
	connection = establishConnection()
	#createTables("a2_setup_new.sql")
	#populateTables("a2-data.sql")

	# this will be merged with mainMenu later
	#createVehicle("1e37y6", "Lamborghini", "Hurican", 2014, "blue", "0001")
	#!# Run the main code here, like it says above this should all be refactored for prettiness anyway
	main()
	connection.close()



