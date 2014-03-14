import sys
import datetime

def vinInDB(VIN):
	## Returns true if the given VIN is on the database
	## Returns false for now...
	return False

def printVTypes():
	## Take a list of vehicle types from the DB and print them
	## Print misc list for now...
	print """		 1. Sedan
		 2. SUV
		 3. Two-Door
		 4. Van
		 5. Truck
		 6. RV"""

def isVType(vType):
	## Check to see if vType is in the list of vehicle types on the DB
	## Return true for now...
	return True

def createVehicle(make, model, year, color, vType):
	## Put the vehicle on the DB
	## Return True for success
	## Return False for failure
	## Return True for now...
	return True

def sinExists(SIN):
	## Checks to see if a SIN exists on the DB
	## Returns True for now..
	return True

def DBgetPersonName(SIN):
	## Returns person at SIN's name
	## Return Bob for now...
	return "Bob"

def DBgetPersonHeight(SIN):
	## Returns person at SIN's height
	## Return 156cm for now...
	return 156

def DBgetPersonWeight(SIN):
	## Returns person at SIN's weight
	## Return 140lb for now...
	return 150

def DBgetPersonEyeColour(SIN):
	## Returns person at SIN's eye colour
	## Return blue for now...
	return "blue"

def DBgetPersonHairColour(SIN):
	## Returns person at SIN's hair colour
	## Return brown for now...
	return "brown"

def DBgetPersonAddress(SIN):
	## Returns person at SIN's address
	## Return 123 Marlboro Road for now...
	return "123 Marlboro Road"

def DBgetGender(SIN):
	## Returns person at SIN's gender
	## Return m for now...
	return "m"

def DBgetBirthday(SIN):
	## Returns person at SIN's birthday
	## Return 0 for now
	return 0

def registerOwner(VIN, SIN):
	## Registers the owner with the VIN on the database
	return True

def createPerson(SIN, name, height, weight, eyeColour, hairColour, addr, gender, birthday):
	## Creates a person on the database
	return True
	

def tryRegisterOwner(VIN):
	## Prep from registering owner with VIN
	adding = True
	while (adding):
		while (True):
			SIN = raw_input("Please enter the new owner's SIN: ")
			try:
				SIN = int(SIN)
				break
			except:
				print "Please enter a number"
				pass
	
		## CREATE A PERSON IN THE DB
		if (sinExists(SIN) == False):
			print "Sorry, that SIN doesn't exist..."
			ans = True
			while (ans == True):
				print "Would you like to create a new instance in the system?"
				answer = raw_input("[Y/N]: ")
				answer = answer.lower()
				if (answer == "y"):
					while (True):
						name = raw_input("Person's name: ")
						i = True
						while (i == True):
							height = raw_input("Person's height: ")
							try:
								height = int(height)
								i = False
							except:
								print "Please enter a number"
								pass
								
							
						
						while (True):
							weight = raw_input("Person's weight: ")
							try:
								weight = int(weight)
								break
							except:
								print "Please enter a number"
								pass

						eyeColour = raw_input("Person's eye colour: ")
						hairColour = raw_input("Person's hair colour: ")
						addr = raw_input("Person's address: ")
						while (True):
							gender = raw_input("Person's gender [m/f]: ")
							gender = gender.lower()
							if (gender == "m" or gender == "f"):
								break
							else:
								print "Sorry, that's not a valid option!"
								print "Please select from either 'm' or 'f'"
						while (True):
							birthday = raw_input("Person's birthday [DD:MM:YYYY]: ")
							try:
								birthday = int(birthday)
								break
							except:
								print "Please enter a number"
								continue

						
						print "\nName: %s\nHeight: %d\nWeight: %d\nHair Colour: %s\nHair Colour: %s\nAddress: %s\nGender: %s\nBirthday: %d" % (name, height, weight, eyeColour, hairColour, addr, gender, birthday)
						print "Is this information correct?"
			
						answer = raw_input("[Y/N] (q to quit): ")
						answer = answer.lower()
						if (answer == "y"):
							createPerson(SIN, name.lower(), height, weight, eyeColour.lower(), hairColour.lower(), addr.lower(), gender, birthday)
							print "Registering owner with SIN %d with vehicle with VIN %d" (SIN, VIN)
							registerOwner(VIN, SIN)
							ans = False
							break
						elif (answer == "n"):
							print "Please re-enter the information:\n"
							continue
						elif (answer == "q"):
							ans = False
							break
						else:
							print "Sorry, that's not a valid option!"

				elif (answer == "n"):
					break
				else:
					print "Sorry, that's not a valid option!"
			

		## GET PERSON'S DATA FROM DB
		else:
			name = DBgetPersonName(SIN)
			height = DBgetPersonHeight(SIN)
			weight = DBgetPersonWeight(SIN)
			eyeColour = DBgetPersonEyeColour(SIN)
			hairColour = DBgetPersonHairColour(SIN)
			addr = DBgetPersonAddress(SIN)
			gender = DBgetGender(SIN)
			birthday = DBgetBirthday(SIN)
			
			while(True):
				print "\nName: %s\nHeight: %d\nWeight: %d\nHair Colour: %s\nHair Colour: %s\nAddress: %s\nGender: %s\nBirthday: %d" % (name, height, weight, eyeColour, hairColour, addr, gender, birthday)
				print "Is this the person you're looking for?"
				answer = raw_input("[Y/N]: ")
				answer = answer.lower()

				if (answer == "y"):
					print "Registering owner with SIN %d with vehicle with VIN %d" (SIN, VIN)
					registerOwner(VIN, SIN)
					break
				elif (answer == "n"):
					break
				else:
					print "Sorry, that's not a valid option!"
		
		while(True):
			print "Would you like to add another owner?"
			answer = raw_input("[Y/N]: ")
			answer = answer.lower()
			if (answer == "y"):
				break
			elif (answer == "n"):
				adding = False
				break
			else:
				print "Sorry, that's not a valid option!"

## On Main Menu Selection 1
def startNVR():
	print "New Vehicle Registration Selected"
	
	while (True):
		while (True):
			VIN = raw_input("Please enter the new vehicle's serial number: ")
			try:
				VIN = int(VIN)
				break
			except:
				print "Please enter a number"
				pass
		if (vinInDB(VIN)):
			print "Sorry, that VIN already exists in the database. Would you like to register a new owner instead?"
			answer = raw_input("[Y/N]: ")
			answer = answer.lower()
			if (answer == "y"):
				tryRegisterOwner(VIN)
			if (answer == "n"):
				main()
		else:
			print "Let's fill in the vehicle's details..."
			make = raw_input("Vehicle make: ")
			model = raw_input("Vehicle model: ")
			year = raw_input("Vehicle year: ") ## Check this to make sure it's a valid year
			color = raw_input("Vehicle colour: ")
			print "Select a vehicle type from the list: "
			printVTypes()
			while (True):
				vType = raw_input("Select a vehicle type from the list: ")
				if (isVType(vType)):
					break
				else:
					print "That is not a valid vehicle type..."
					continue
		
			createVehicle(make, model, year, color, vType)
			
			while(True):
				print "Would you like to add a vehicle owner?"
				answer = raw_input("[Y/N]: ")
				answer = answer.lower()
				if (answer == "y"):
					tryRegisterOwner(VIN)
					print "\nThank you for registering this vehicle."
					print "Going back to the main menu...\n"
					main()
				if (answer == "n"):
					print "\nThank you for registering this vehicle."
					print "Going back to the main menu...\n"
					main()
				else:
					print "Sorry, that's not a valid option!"
					continue
		
		
			
	

def startAT():
	print "Auto Transaction Selected"

def startDLR():
	print "Driver License Registration Selected"

def startVR():
	print "Violation Record Selected"

def startSE():
	print "Search Engine Selected"


def main():
	print """PLEASE SELECT FROM THE FOLLOWING OPTIONS:
	      1. New Vehicle Registration
	      2. Auto Transaction
	      3. Driver License Registration
	      4. Violation Record
	      5. Search Engine
	      6. Exit"""

	var = 0

	while(var != "6"):
		var = raw_input("Select [1/2/3/4/5/6]: ")
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
			print "Exiting..."

		else:
			print "Sorry, that's not a valid option!"
	

	sys.exit()



if (__name__ == "__main__"):
	main()



