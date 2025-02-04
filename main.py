from tkinter import Tk
from views.login import LoginFrame
from views.navFrame import NavFrame
from views.addStudent import AddStudentFrame

class App(Tk):
    # def __init__(self):
    #     super().__init__()

    #     # self.title("Tkinter App") 
    #     # self.frame = LoginFrame(self)
    #     # self.frame.pack()

     
    #     navFrame = NavFrame(self)
    #     navFrame.pack(side="left", padx=(0, 2))

    #     addStudent = AddStudentFrame(self)
    #     addStudent.pack(side="right")
    def __init__(self):
        super().__init__()

        self.title("Tkinter App")
        self.current_frame = None  # Keep track of the current frame
        self.current_frame2 = None  # Keep track of the current frame
        self.switch_frame(AddStudentFrame)  # Start with the LoginFrame
        self.switch(NavFrame)

    def switch_frame(self, frame_class):
        """Destroy the current frame and replace it with a new one."""
        if self.current_frame is not None:
            self.current_frame.destroy()

        self.current_frame = frame_class(self)
        self.current_frame.pack(side="right")

    def switch_search_frame(self, frame_class,text = "add", btntext = "add", func = None):
        """Destroy the current frame and replace it with a new one."""
        if self.current_frame is not None:
            self.current_frame.destroy()

        self.current_frame = frame_class(self, text, btntext, func)
        self.current_frame.pack(side="right")

    def switch(self, frame_class):
        """Destroy the current frame and replace it with a new one."""
        self.current_frame2 = frame_class(self)
        self.current_frame2.pack(side="left", padx=(0, 2))

        

if __name__ == "__main__":
    app = App()
    app.mainloop()




# bg_colour = "#3d6466"





# def load_frame1():
# 	clear_widgets(frame2)
# 	frame1.tkraise()
# 	Button(
# 		frame1,
# 		text="SHUFFLE",
# 		font=("Ubuntu", 20),
# 		bg="#28393a",
# 		fg="white",
# 		cursor="hand2",
# 		activebackground="#badee2",
# 		activeforeground="black",
# 		command=lambda:load_frame2()
# 		).pack(pady=20)
	

# def load_frame2():
# 	clear_widgets(frame1)
# 	frame2.tkraise()
# 	Button(
# 		frame2,
# 		text="BACK",
# 		font=("Ubuntu", 18),
# 		bg="#28393a",
# 		fg="white",
# 		cursor="hand2",
# 		activebackground="#badee2",
# 		activeforeground="black",
# 		command=lambda:load_frame1()
# 		).pack(pady=20)


# root = Tk()
# root.title("test")
# root.geometry("500x400")

# frame1 = Frame(root, width=500, height=400, bg=bg_colour)
# frame2 = Frame(root, bg=bg_colour,width=500, height=400)

# for frame in (frame1, frame2):
# 	frame.grid(row=0, column=0, sticky="nesw")
	
# load_frame1()

# root.mainloop()