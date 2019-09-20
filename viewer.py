from tkinter import *
import tkinter as tk
from data import Text

class Gui(tk.Frame):
    def __init__(self, master = None):

        self.ep_title = 0
        self.number = 0
        self.tx = Text()

        tk.Frame.__init__(self,master)
        
        self.grid()
        
        self.build_gui()


    def build_gui (self):
        def episode_1():
            self.number = 0
            self.canvas.create_rectangle(100,0,678,32, fill="#0096FA")
            self.canvas.create_text(75,16, fill="white", text=(self.tx.s_1_titles[self.number]), anchor="w", font=("Arial", 16, 'bold'))
            self.canvas.create_rectangle(100,36,125,60, fill="white", width=0)
            self.canvas.create_text(100,48, text="1" , anchor = "w", font=("Arial", 16, 'bold'))
            self.canvas.create_rectangle(240,36,300,60, fill="white", width=0)
            self.canvas.create_text(240,48, text=str(self.number) , anchor = "w", font=("Arial", 16, 'bold'))

        def episode_2():
            self.number = 1
            self.canvas.create_rectangle(2,0,678,32, fill="#0096FA")
            self.canvas.create_text(75,16, fill="white", text=(self.tx.s_1_titles[self.number]), anchor="w", font=("Arial", 16, 'bold'))
            self.canvas.create_rectangle(75,16,10,10, fill="#0096FA")
            self.canvas.create_text(100,48, text="1" , anchor = "w", font=("Arial", 16, 'bold'))
            self.canvas.create_text(240,48, text=str(self.number) , anchor = "w", font=("Arial", 16, 'bold'))
        
            
        self.top_frame = tk.Frame(self)
        self.top_frame.pack(side=tk.TOP, anchor = tk.NW, expand = True)

        self.season_1_button = tk.Menubutton(self.top_frame, text="  Season  1  ", font=("Arial", 16, 'bold'), fg="black", relief=RAISED, activebackground = "#0096FA", activeforeground = "white", background = "lightgray")
        self.season_1_button.menu = Menu(self.season_1_button, tearoff=0)
        self.season_1_button["menu"] = self.season_1_button.menu
        self.season_1_button.grid(row = 1, column = 1)

        self.season_1_button.menu.add_command (label=" Episode   1 ", command = episode_1, font=("Arial", 12))
        self.season_1_button.menu.add_command (label=" Episode   2 ", command = episode_2, font=("Arial", 12))
        '''
        self.season_1_button.menu.add_command (label=" Episode   3 ", command = episode_3, font=("Arial", 12))
        self.season_1_button.menu.add_command (label=" Episode   4 ", command = episode_1, font=("Arial", 12))
        self.season_1_button.menu.add_command (label=" Episode   5 ", command = episode_1, font=("Arial", 12))
        self.season_1_button.menu.add_command (label=" Episode   6 ", command = episode_1, font=("Arial", 12))
        self.season_1_button.menu.add_command (label=" Episode   7 ", command = episode_1, font=("Arial", 12))
        self.season_1_button.menu.add_command (label=" Episode   8 ", command = episode_1, font=("Arial", 12))
        self.season_1_button.menu.add_command (label=" Episode   9 ", command = episode_1, font=("Arial", 12))
        self.season_1_button.menu.add_command (label=" Episode  10 ", command = episode_1, font=("Arial", 12))
        self.season_1_button.menu.add_command (label=" Episode  11 ", command = episode_1, font=("Arial", 12))
        self.season_1_button.menu.add_command (label=" Episode  12 ", command = episode_1, font=("Arial", 12))
        self.season_1_button.menu.add_command (label=" Episode  13 ", command = episode_1, font=("Arial", 12))
        self.season_1_button.menu.add_command (label=" Episode  14 ", command = episode_1, font=("Arial", 12))
        self.season_1_button.menu.add_command (label=" Episode  15 ", command = episode_1, font=("Arial", 12))
        self.season_1_button.menu.add_command (label=" Episode  16 ", command = episode_1, font=("Arial", 12))
        self.season_1_button.menu.add_command (label=" Episode  17 ", command = episode_1, font=("Arial", 12))
        self.season_1_button.menu.add_command (label=" Episode  18 ", command = episode_1, font=("Arial", 12))
        self.season_1_button.menu.add_command (label=" Episode  19 ", command = episode_1, font=("Arial", 12))
        self.season_1_button.menu.add_command (label=" Episode  20 ", command = episode_1, font=("Arial", 12))
        self.season_1_button.menu.add_command (label=" Episode  21 ", command = episode_1, font=("Arial", 12))
        self.season_1_button.menu.add_command (label=" Episode  22 ", command = episode_1, font=("Arial", 12))
        self.season_1_button.menu.add_command (label=" Episode  23 ", command = episode_1, font=("Arial", 12))
        self.season_1_button.menu.add_command (label=" Episode  24 ", command = episode_1, font=("Arial", 12))
        '''

        self.season_2_button = tk.Menubutton(self.top_frame, text="  Season  2  ", font=("Arial", 16, 'bold'), fg="black", relief=RAISED, activebackground = "#0096FA", activeforeground = "white", background = "lightgray")
        self.season_2_button.menu = Menu(self.season_2_button, tearoff=0)
        self.season_2_button["menu"] = self.season_2_button.menu
        self.season_2_button.grid(row = 1, column = 2)


        self.season_3_button = tk.Menubutton(self.top_frame, text="  Season  3  ", font=("Arial", 16, 'bold'), fg="black", relief=RAISED, activebackground = "#0096FA", activeforeground = "white", background = "lightgray")
        self.season_3_button.menu = Menu(self.season_3_button, tearoff=0)
        self.season_3_button["menu"] = self.season_3_button.menu
        self.season_3_button.grid(row = 1, column = 3)


        self.season_4_button = tk.Menubutton(self.top_frame, text="  Season  4  ", font=("Arial", 16, 'bold'), fg="black", relief=RAISED, activebackground = "#0096FA", activeforeground = "white", background = "lightgray")
        self.season_4_button.menu = Menu(self.season_4_button, tearoff=0)
        self.season_4_button["menu"] = self.season_4_button.menu
        self.season_4_button.grid(row = 1, column = 4)


        self.season_5_button = tk.Menubutton(self.top_frame, text="  Season  5  ", font=("Arial", 16, 'bold'), fg="black", relief=RAISED, activebackground = "#0096FA", activeforeground = "white", background = "lightgray")
        self.season_5_button.menu = Menu(self.season_5_button, tearoff=0)
        self.season_5_button["menu"] = self.season_5_button.menu
        self.season_5_button.grid(row = 1, column = 5)


        self.season_6_button = tk.Menubutton(self.top_frame, text="  Season  6  ", font=("Arial", 16, 'bold'), fg="black", relief=RAISED, activebackground = "#0096FA", activeforeground = "white", background = "lightgray")
        self.season_6_button.menu = Menu(self.season_6_button, tearoff=0)
        self.season_6_button["menu"] = self.season_6_button.menu
        self.season_6_button.grid(row = 2, column = 1)


        self.season_7_button = tk.Menubutton(self.top_frame, text="  Season  7  ", font=("Arial", 16, 'bold'), fg="black", relief=RAISED, activebackground = "#0096FA", activeforeground = "white", background = "lightgray")
        self.season_7_button.menu = Menu(self.season_7_button, tearoff=0)
        self.season_7_button["menu"] = self.season_7_button.menu
        self.season_7_button.grid(row = 2, column = 2)


        self.season_8_button = tk.Menubutton(self.top_frame, text="  Season  8  ", font=("Arial", 16, 'bold'), fg="black", relief=RAISED, activebackground = "#0096FA", activeforeground = "white", background = "lightgray")
        self.season_8_button.menu = Menu(self.season_8_button, tearoff=0)
        self.season_8_button["menu"] = self.season_8_button.menu
        self.season_8_button.grid(row = 2, column = 3)


        self.season_9_button = tk.Menubutton(self.top_frame, text="  Season  9  ", font=("Arial", 16, 'bold'), fg="black", relief=RAISED, activebackground = "#0096FA", activeforeground = "white", background = "lightgray")
        self.season_9_button.menu = Menu(self.season_9_button, tearoff=0)
        self.season_9_button["menu"] = self.season_9_button.menu
        self.season_9_button.grid(row = 2, column = 4)


        self.season_10_button = tk.Menubutton(self.top_frame, text="  Season 10 ", font=("Arial", 16, 'bold'), fg="black", relief=RAISED, activebackground = "#0096FA", activeforeground = "white", background = "lightgray")
        self.season_10_button.menu = Menu(self.season_10_button, tearoff=0)
        self.season_10_button["menu"] = self.season_10_button.menu
        self.season_10_button.grid(row = 2, column = 5)



        self.middle_frame = tk.Frame(self)
        self.middle_frame.pack(side = tk.TOP, anchor = "n")


        self.canvas = tk.Canvas(self.middle_frame, bg="white", height=500, width=678)
        self.canvas.create_rectangle(2,0,678,32, fill="#0096FA")
        self.canvas.create_text(10,17, fill="white", text="Title:", anchor="w", font=("Arial", 16, 'bold'))
        self.canvas.create_text(10,48, text="Season" , anchor = "w", font=("Arial", 16, 'bold'))
        self.canvas.create_text(145,48, text="Episode" , anchor = "w", font=("Arial", 16, 'bold'))
        self.canvas.create_text(470,48, text="Episode overall 222" , anchor = "w", font=("Arial", 16, 'bold'))
        self.canvas.create_text(10,80, text="Original Airdate:" , anchor = "w", font=("Arial", 16, 'bold'))
        self.canvas.create_text(10,112, text="Summery:" , anchor = "w", font=("Arial", 16, 'bold'))
        
        self.canvas.create_line(2,1,2,500)
        self.canvas.create_line(678,0,678,500)
        self.canvas.create_line(0,64,678,64)
        self.canvas.create_line(2,2,678,2)
        self.canvas.create_line(2,500,678,500)

        self.canvas.create_line(64,0,64,32)
        self.canvas.create_line(128,32,128,64)
        self.canvas.create_line(280,32,280,64)
        self.canvas.create_line(456,32,456,64)
        self.canvas.create_line(0,32,678,32)
        self.canvas.create_line(0,96,678,96)

        self.canvas.pack(side=BOTTOM)


gui = Gui()
gui.master.title = 'Random Friends Episode Generator'
gui.mainloop()