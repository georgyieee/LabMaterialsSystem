import sqlite3
from Models.Student import Student
from Models.Item import Item
from Models.BorrowerSlip import BorrowerSlip
from Models.BorrowerSlip_Item import BorrowerSlip_Item

class DBHelper:
	
	def __init__(self, db):
		self.connection = sqlite3.connect(db)
		self.connection.executescript("pragma foreign_keys=on")
		self.cursor = self.connection.cursor()
		
	def __del__(self):
		self.connection.close()
		
	def CreateStudent(self, student):
		command = f"""INSERT INTO Student
					  VALUES(
					   {student.StudentID},
					   '{student.FirstName}',
					   '{student.MiddleName}',
					   '{student.LastName}',
					   '{student.Program}',
					   {student.Year}
				   )"""
		self.cursor.execute(command)
		self.connection.commit()
		
	def GetStudents(self):
		command = "SELECT * FROM Student"
		self.cursor.execute(command)
		students = self.cursor.fetchall()
		res = []
		for s in students:
			res.append(Student(s[0],
							   s[1],
							   s[2],
							   s[3],
							   s[4],
							   s[5]))
		return res
		
	def GetStudent(self, studentID):
		command = f"SELECT * FROM Student WHERE StudentID = {studentID}"
		self.cursor.execute(command)
		s = self.cursor.fetchone()
		if s == None:
			return None
		return Student(s[0], s[1], s[2], s[3], s[4], s[5])
		
	def UpdateStudent(self, student):
		command = f"""UPDATE Student SET
					   FirstName = '{student.FirstName}',
					   MiddleName = '{student.MiddleName}',
					   LastName = '{student.LastName}',
					   Program = '{student.Program}',
					   Year = {student.Year}
				      WHERE StudentID = {student.StudentID}"""
		self.cursor.execute(command)
		self.connection.commit()
		
	def DeleteStudent(self, studentID):
		self.cursor.execute(f"SELECT BorrowerSlipID FROM BorrowerSlip WHERE StudentID = {studentID}")
		borrowerSlips = self.cursor.fetchall()
		for bs in borrowerSlips:
			self.cursor.execute(f"DELETE FROM BorrowerSlip_Item WHERE BorrowerSlipID = {bs[0]}")
		command1 = f"DELETE FROM BorrowerSlip WHERE StudentID = {studentID}"
		command2 = f"DELETE FROM Student WHERE StudentID = {studentID}"
		self.cursor.execute(command1)
		self.cursor.execute(command2)
		self.connection.commit()

	def CreateItem(self, item):
		command = f"INSERT INTO Item VALUES(NULL, '{item.Name}')"
		self.cursor.execute(command)
		self.connection.commit()
		
	def GetItems(self):
		command = f"SELECT * FROM Item"
		self.cursor.execute(command)
		items = self.cursor.fetchall()
		res = []
		for i in items:
			res.append(Item(i[0], i[1]))
		return res
		
	def GetItem(self, itemID):
		command = f"SELECT * FROM Item WHERE ItemID = {itemID}"
		self.cursor.execute(command)
		i = self.cursor.fetchone()
		if i == None:
			return None
		return Item(i[0], i[1])
		
	def UpdateItem(self, item):
		command = f"""UPDATE Item SET Name = '{item.Name}'
					  WHERE ItemID = {item.ItemID}"""
		self.cursor.execute(command)
		self.connection.commit()
	
	def DeleteItem(self, itemID):
		command1 = f"DELETE FROM BorrowerSlip_Item WHERE ItemID = {itemID}"
		command2 = f"DELETE FROM Item WHERE ItemID = {itemID}"
		self.cursor.execute(command1)
		self.cursor.execute(command2)
		self.connection.commit()
		
	def CreateBorrowerSlip(self, borrowerSlip):
		command = f"""INSERT INTO BorrowerSlip VALUES(
						NULL,
						{borrowerSlip.StudentID},
						'{borrowerSlip.Course}',
						'{borrowerSlip.Section}',
						'{borrowerSlip.LabAssistant}',
						'{borrowerSlip.DateTimeBorrowed}',
						'{borrowerSlip.DateTimeReturned}',
						'{borrowerSlip.Room}',
						'{borrowerSlip.Professor}')"""
		self.cursor.execute(command)
		self.connection.commit()
	   
	def GetBorrowerSlips(self):
		command = "SELECT * FROM BorrowerSlip"
		self.cursor.execute(command)
		borrowerSlips = self.cursor.fetchall()
		res = []
		for bs in borrowerSlips:
			res.append(BorrowerSlip(
				bs[0], bs[1], bs[2], bs[3], bs[4],
				bs[5], bs[6], bs[7], bs[8]))
		return res
		
	def GetBorrowerSlip(self, borrowerSlipID):
		command = f"SELECT * FROM BorrowerSlip WHERE BorrowerSlipID = {borrowerSlipID}"
		self.cursor.execute(command)
		bs = self.cursor.fetchone()
		if bs == None:
			return None
		return BorrowerSlip(bs[0], bs[1], bs[2], bs[3], bs[4],
							bs[5], bs[6], bs[7], bs[8])
							
	def UpdateBorrowerSlip(self, borrowerSlip):
		command = f"""UPDATE BorrowerSlip SET
						StudentID = {borrowerSlip.StudentID},
						Course = '{borrowerSlip.Course}',
						Section = '{borrowerSlip.Section}',
						LabAssistant = '{borrowerSlip.LabAssistant}',
						DateTimeBorrowed = '{borrowerSlip.DateTimeBorrowed}',
						DateTimeReturned = '{borrowerSlip.DateTimeReturned}',
						Room = '{borrowerSlip.Room}',
						Professor = '{borrowerSlip.Professor}'
					  WHERE BorrowerSlipID = {borrowerSlip.BorrowerSlipID}"""
		self.cursor.execute(command)
		self.connection.commit()
		
	def DeleteBorrowerSlip(self, borrowerSlipID):
		command1 = f"DELETE FROM BorrowerSlip_Item WHERE BorrowerSlipID = {borrowerSlipID}"
		command2 = f"DELETE FROM BorrowerSlip WHERE BorrowerSlipID = {borrowerSlipID}"
		self.cursor.execute(command1)
		self.cursor.execute(command2)
		self.connection.commit()
		
	def CreateBorrowerSlip_Item(self, borrowerSlip_item):
		command = f"""INSERT INTO BorrowerSlip_Item VALUES(
						{borrowerSlip_item.BorrowerSlipID},
						{borrowerSlip_item.ItemID},
						{borrowerSlip_item.Quantity},
						{borrowerSlip_item.Condition})"""
		self.cursor.execute(command)
		self.connection.commit()
		
	def GetBorrowerSlip_Items(self, borrowerSlipID):
		command = f"SELECT * FROM BorrowerSlip_Item WHERE BorrowerSlipID = {borrowerSlipID}"
		self.cursor.execute(command)
		borrowerSlip_items = self.cursor.fetchall()
		res = []
		for bsi in borrowerSlip_items:
			res.append(BorrowerSlip_Item(bsi[0], bsi[1], bsi[2], bsi[3]))
		return res
		
	def GetBorrowerSlip_Item(self, borrowerSlipID, itemID):
		command = f"SELECT * FROM BorrowerSlip_Item WHERE BorrowerSlipID = {borrowerSlipID} AND ItemID = {itemID}"
		self.cursor.execute(command)
		bsi = self.cursor.fetchone()
		if bsi == None: 
			return None
		return BorrowerSlip_Item(bsi[0], bsi[1], bsi[2], bsi[3])
	
	def UpdateBorrowerSlip_Item(self, borrowerSlip_item):
		command = f"""UPDATE BorrowerSlip_Item SET
						Quantity = {borrowerSlip_item.Quantity},
						Condition = {borrowerSlip_item.Condition}
					   WHERE BorrowerSlipID = {borrowerSlip_item.BorrowerSlipID} AND
					   ItemID = {borrowerSlip_item.ItemID}"""
		self.cursor.execute(command)
		self.connection.commit()
	
	def DeleteBorrowerSlip_Item(self, borrowerSlipID, itemID):
		command = f"DELETE FROM BorrowerSlip_Item WHERE BorrowerSlipID = {borrowerSlipID} AND ItemID = {itemID}"
		self.cursor.execute(command)
		self.connection.commit()
		

