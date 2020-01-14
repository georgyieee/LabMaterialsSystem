import sqlite3

# connect to the db file
connection = sqlite3.connect("inventory_system.db")

# load the cursor
cursor = connection.cursor()

# create Student table
student = """CREATE TABLE Student(
				StudentID INTEGER PRIMARY KEY,
				FirstName TEXT NOT NULL,
				MiddleName TEXT,
				LastName TEXT NOT NULL,
				Program TEXT NOT NULL,
				Year INTEGER NOT NULL
			 )"""
cursor.execute(student)

# create BorrowerSlip table
borrowerSlip = """CREATE TABLE BorrowerSlip(
					BorrowerSlipID INTEGER PRIMARY KEY AUTOINCREMENT,
					StudentID INTEGER NOT NULL,
					Course TEXT NOT NULL,
					Section TEXT NOT NULL,
					LabAssistant TEXT NOT NULL,
					DateTimeBorrowed TEXT NOT NULL,
					DateTimeReturned TEXT,
					Room TEXT NOT NULL,
					Professor TEXT NOT NULL,
					FOREIGN KEY(StudentID) REFERENCES Student(StudentID)
				   )"""
cursor.execute(borrowerSlip)

# create BorrowerSlip_Item table
borrowerSlip_Item = """CREATE TABLE BorrowerSlip_Item(
						BorrowerSlipID INTEGER NOT NULL,
						ItemID INTERGER NOT NULL,
						Quantity INTEGER NOT NULL,
						Condition INTEGER NOT NULL,
						PRIMARY KEY(BorrowerSlipID, ItemID),
						FOREIGN KEY(BorrowerSlipID) REFERENCES BorrowerSlip(BorrowerSlipID),
						FOREIGN KEY(ItemID) REFERENCES Item(ItemID)
					   )"""
cursor.execute(borrowerSlip_Item)

# create Item table
item = """CREATE TABLE Item(
			ItemID INTEGER PRIMARY KEY AUTOINCREMENT,
			Name TEXT NOT NULL
		  )"""
cursor.execute(item)

# commit to save
connection.commit()

#close connection
connection.close()
