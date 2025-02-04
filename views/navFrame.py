import tkinter as tk
from .componets import Button
from utils.colors import primary_color
from .updateStudent import UpdateStudentFrame
from .addStudent import AddStudentFrame
from .searchStudent import SearchStudentFrame
from .listAllStudents import ListAllStudents

class NavFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent

        self.configure(width=250,height=600, background=primary_color)
        self.pack_propagate(False)

        # Add New Student Button
        self.AddNewStudent = Button(self, text="Add Student", command=self.loadAddStudent)
        self.AddNewStudent.pack(fill="x", pady=(20, 5), padx= 5)


        #list all students button
        self.ListAllStudents = Button(self, text="List Students", command=lambda:self.listStudents())
        self.ListAllStudents.pack(fill="x", pady=5, padx= 5)

        # update student button
        self.UpdateStudent = Button(self, text="Update student", command=lambda:self.loadUpdate())
        self.UpdateStudent.pack(fill="x", pady=5, padx=5)


        # delete student button
        self.DeleteStudent = Button(self, text="Delete student", command=lambda:self.loadDelete())
        self.DeleteStudent.pack(fill="x", pady=5, padx=5)


    def loadAddStudent(self):
        self.parent.switch_frame(AddStudentFrame)

    def listStudents(self):
        self.parent.switch_frame(ListAllStudents)

    def loadUpdate(self):
        self.parent.switch_search_frame(SearchStudentFrame, text = "Search Student", btntext = "Search", func = None)

    def loadDelete(self):
        self.parent.switch_search_frame(SearchStudentFrame, text = "Search Student", btntext = "Search", func = None)
        




