from tkinter import *
from tkinter import messagebox
import Files.Thread_Maker
from Files.Sorting_Screen import *
import customtkinter


class Window:
    def __init__(self, root):

        self.root = root

        self.root.protocol("WM_DELETE_WINDOW", self.Close)

        self.wx, self.wy = 500, 250
        self.wxs, self.wys = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self.WINDOW_X, self.WINDOW_Y = (self.wxs / 2) - (self.wx / 2), (self.wys / 2) - (self.wy / 2)
        self.root.geometry('%dx%d+%d+%d' % (self.wx, self.wy, self.WINDOW_X, self.WINDOW_Y))
        self.root.config(bg="#383838")
        self.root.resizable(False, False)

        self.root.title("Sorting Visualization")
        try:
            self.root.iconbitmap("Resources/algorithm.ico")
        except:
            img = PhotoImage("Resources/algorithm.ico")
            self.root.tk.call('wm', 'iconphoto', self.root._w, img)

        # Heading
        self.MainLabel = customtkinter.CTkLabel(self.root, text='Sorting Visualization', font=("Ageo-Bold", 30))
        self.MainLabel.pack(pady=15)

        self.MainLabel = customtkinter.CTkLabel(self.root,
                                                text='Made by\nUsman Yaqoob(20K-0355) &\nManahil Fatima(20K-0134)',
                                                font=("Ageo-Bold", 17))
        self.MainLabel.pack(pady=15)

        self.NextButton = customtkinter.CTkButton(master=self.root, text="GO!", command=self.Run1,font=("Ageo-Bold", 15))

        self.NextButton.pack(pady=20)


    def Exit(self):
        self.root.destroy()

    def Close(self):
        if messagebox.askokcancel("Quit", "Do you want to quit this amazing program?"):
            self.root.destroy()
            exit()

    def Back(self):
        self.root.destroy()
        Process = Files.Start_Threading.START()
        Process.start()


    def Run1(self):
        self.root.destroy()
        sort_window = Tk()
        Sorting(sort_window, 'Bubble Sort')
        sort_window.mainloop()


