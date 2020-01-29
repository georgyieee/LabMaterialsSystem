from tkinter import *
from Models.Student import Student
from tkinter import messagebox
from DBHelper import DBHelper
import tkinter.ttk as ttk

class StudentManager(Frame):
	
	def __init__(self, master, db):
		super().__init__(master)
		self.master = master
		self.master.title("Student Manager")
		self.db = db
		self.initialize()
		self.grid(
			row = 0,
			column = 0,
			padx = 20,
			pady = 20
		)
		self.populateStudentTable()
		
	def AddStudent(self):
		studentNumber = self.studentNumberVal.get()
		firstName = self.firstNameVal.get()
		middleName = self.middleNameVal.get()
		lastName = self.lastNameVal.get()
		program = self.programVal.get()
		year = self.yearVal.get()
		if firstName == "" or lastName == "" or program == "" or year == "" or studentNumber == "":
			messagebox.showerror("Required Fields", "Please fill up all the required fields.")
			return
		if not year.isnumeric() or not studentNumber.isnumeric():
			messagebox.showerror("Invalid Fields", "Student Number and Year should be numeric.")
			return
		try:
			student = Student(
				studentNumber,
				firstName,
				middleName,
				lastName,
				program,
				year
			)
			self.db.CreateStudent(student)
			messagebox.showinfo("Registration Successful", f"{studentNumber} has successfully been added.")
		except Exception as e:
			messagebox.showerror("Registration Error", "Student Number has already been taken.")
		self.populateStudentTable()
		
	def DeleteStudent(self):
		selected_item = self.studentTable.focus()
		if selected_item == "": return
		studentID = self.studentTable.item(selected_item)["values"][0]
		self.db.DeleteStudent(studentID)
		self.populateStudentTable()
		
	def populateStudentTable(self):
		self.studentTable.delete(*self.studentTable.get_children())
		for s in self.db.GetStudents():
			self.studentTable.insert(
				'',
				'end',
				values=(
					s.StudentID,
					s.GetFullName(),
					s.Program,
					s.Year
				)
			)
		
	def initialize(self):
		#student number
		Label(
			self,
			text = "Student Number"
		).grid(
			row = 0,
			column = 0,
			sticky = W+N+S,
			pady = 10
		)
		self.studentNumberVal = StringVar(self)
		Entry(
			self,
			textvariable = self.studentNumberVal
		).grid(
			row = 0,
			column = 1,
			sticky = W+E+N+S,
			pady = 10
		)
		
		#first name
		Label(
			self,
			text = "First Name"
		).grid(
			row = 1,
			column = 0,
			sticky = W+N+S,
			pady = 10
		)
		self.firstNameVal = StringVar(self)
		Entry(
			self,
			textvariable = self.firstNameVal
		).grid(
			row = 1,
			column = 1,
			sticky = W+E+N+S,
			pady = 10
		)
		
		#middle name
		Label(
			self,
			text = "Middle Name"
		).grid(
			row = 2,
			column = 0,
			sticky = W+N+S,
			pady = 10
		)
		self.middleNameVal = StringVar(self)
		Entry(
			self,
			textvariable = self.middleNameVal
		).grid(
			row = 2,
			column = 1,
			sticky = W+E+N+S,
			pady = 10
		)
		
		#last name
		Label(
			self,
			text = "Last Name"
		).grid(
			row = 3,
			column = 0,
			sticky = W+N+S,
			pady = 10
		)
		self.lastNameVal = StringVar(self)
		Entry(
			self,
			textvariable = self.lastNameVal
		).grid(
			row = 3,
			column = 1,
			sticky = W+E+N+S,
			pady = 10
		)
		
		#program
		Label(
			self,
			text = "Program"
		).grid(
			row = 4,
			column = 0,
			sticky = W+N+S,
			pady = 10
		)
		self.programVal = StringVar(self)
		Entry(
			self,
			textvariable = self.programVal
		).grid(
			row = 4,
			column = 1,
			sticky = W+E+N+S,
			pady = 10
		)
		
		#year
		Label(
			self,
			text = "Year"
		).grid(
			row = 5,
			column = 0,
			sticky = W+N+S,
			pady = 10
		)
		self.yearVal = StringVar(self)
		Entry(
			self,
			textvariable = self.yearVal
		).grid(
			row = 5,
			column = 1,
			sticky = W+E+N+S,
			pady = 10
		)
		
		#buttons
		Button(
			self,
			text = "Add Student",
			command = self.AddStudent
		).grid(
			row = 6,
			column = 0,
			columnspan = 2,
			sticky = W+E+N+S,
			pady = 10
		)
		Button(
			self,
			text = "Delete Student",
			command = self.DeleteStudent
		).grid(
			row = 7,
			column = 0,
			columnspan = 2,
			sticky = W+E+N+S,
			pady = 10
		)
		
		self.studentTable = ttk.Treeview(
			self,
			columns=("StudentID", "Name", "Program", "Year")
		)
		self.studentTable.column('#0', stretch=NO, minwidth=0, width=0)
		
		self.studentTable.heading('StudentID', text="Student ID", anchor=W)
		self.studentTable.heading('Name', text="Name", anchor=W)
		self.studentTable.heading('Program', text="Program", anchor=W)
		self.studentTable.heading('Year', text="Year", anchor=W)
		self.studentTable.grid(row=8, column=0, columnspan=2)
		
db = DBHelper("inventory_system.db")
root = Tk()
app = StudentManager(root, db)
root.mainloop()
