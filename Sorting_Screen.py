from tkinter import *
from tkinter import messagebox
from random import shuffle, sample
from Files.Sorting_Algorithms import algochooser
from colorsys import hls_to_rgb
from threading import *
from tkinter import *
import Files.Thread_Maker
import easygui
import customtkinter
customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class Sorting:
    def __init__(self, root, AlgoNameVar):

        self.root = root

        self.root.protocol("WM_DELETE_WINDOW", self.Close)

        self.AlgoNameVar = AlgoNameVar

        self.wx, self.wy = 1200, 700

        self.wxs, self.wys = self.root.winfo_screenwidth(), self.root.winfo_screenheight()

        self.WINDOW_X, self.WINDOW_Y = (self.wxs / 2) - (self.wx / 2), (self.wys / 2) - (self.wy / 2)

        self.CANVAS_X, self.CANVAS_Y = 950, 700

        self.FRAME1_X, self.FRAME1_Y = 250, 700

        self.root.geometry('%dx%d+%d+%d' % (self.wx, self.wy, self.WINDOW_X, self.WINDOW_Y))
        self.root.config(bg="grey")
        self.root.wm_resizable(False, False)

        # Heading
        self.root.title("Sorting Visualization Project")
        try:
            self.root.iconbitmap("Resources/sorting.ico")
        except:
            img = PhotoImage("Resources/sorting.ico")
            self.root.tk.call('wm', 'iconphoto', self.root._w, img)


        self.size_var = IntVar()
        self.size_var.set(12)

        self.speed_var = IntVar()
        self.speed_var.set(35)

        self.graph_type = IntVar()
        self.graph_type.set(0)
        self.TYPE = self.graph_type.get()

        self.starting_point = 3

        # Creating frame
        self.frame1 = Frame(root, width=self.FRAME1_X, height=self.FRAME1_Y, bg="#383838")
        self.frame1.grid_propagate(0)
        self.frame1.pack(side=LEFT)


        self.information = {'Bubble Sort': "Worst Case:O(n²)\n\nAverage Case:O(n²)\n\nBest Case:O(n)",
                            'Selection Sort': "Worst Case:O(n²)\n\nAverage Case:O(n²)\n\nBest Case:O(n²)",
                            'Merge Sort': "Worst Case:O(n*log n)\n\nAverage Case:O(n*log n)\n\nBest Case:O(n*log n)",
                            'Heap Sort': "Worst Case:O(n*log n)\n\nAverage Case:O(n*log n)\n\nBest Case:O(n*log n)",
                            'Insertion Sort': "Worst Case:O(n²)\n\nAverage Case:O(n²)\n\nBest Case:O(n)",
                            'Quick Sort': "Worst Case:O(n²)\n\nAverage Case:O(n*log n)\n\nBest Case:O(n*log n)",
                            'Shell Sort': "Worst Case:O(n²)\n\nAverage Case:O(n²)\n\nBest Case:O(n*log n)",
                            'Radix Sort': "Worst Case:O(k*(n+b))\n\nAverage Case:O(k*(n+b))\n\nBest Case:O(k*(n+b))",
                            'Count Sort': "Worst Case:O(n+k)\n\nAverage Case:O(n+k)\n\nBest Case:O(n+k)",
                            'Bucket Sort': "Worst Case:O(n+k)\n\nAverage Case:O(n+k)\n\nBest Case:O(n+k)",
                            'Textbook 1': "Average Case:O(n + k),"}


        self.algorithm = ['Insertion Sort', 'Bubble Sort', 'Merge Sort', 'Quick Sort', 'Heap Sort', 'Radix Sort', 'Count Sort', 'Bucket Sort', 'Textbook 1']


        self.algo_var = StringVar()

        #default
        self.algo_var.set(self.AlgoNameVar)
        self.algo_menu = OptionMenu(self.frame1, self.algo_var, *self.algorithm, command=self.case_chooser)
        self.algo_menu.config(font="Ageo-Light", bg="#77a3bf", activebackground="#1cafd1", cursor="circle")
        self.algo_menu["highlightthickness"] = 3
        self.algo_menu["padx"] = 20
        self.algo_menu["pady"] = 8
        self.algo_menu.grid_propagate(0)


        self.algo_menu.place(rely=0.1, relx=0.5, anchor=CENTER)


        self.frame_btn1 = Frame(self.frame1, width=230, height=40, bg="#383838")
        self.frame_btn1.grid_propagate(0)
        self.frame_btn1.place(relx=0.0, rely=0.17)

        self.btn_new = Button(self.frame_btn1, text="Choose File", padx=13, pady=3, command=self.new_list, bg="#666666", fg="azure", cursor="hand2")
        self.btn_new.place(relx=0.15, rely=0)

        self.btn_shuffle = Button(self.frame_btn1, text="Shuffle", padx=13, pady=3, command=self.shuffle_list, bg="#666666", fg="azure", cursor="hand2")
        self.btn_shuffle.place(relx=0.60, rely=0)


        self.frame_radio = Frame(self.frame1, bg="#383838", width=230, height=45, relief="flat", bd=4)
        self.frame_radio.place(relx=0, rely=0.23)
        self.frame_radio.grid_propagate(0)

        self.bar_drawing = customtkinter.CTkRadioButton(self.frame_radio, text="Bar", variable=self.graph_type, value=0, command=self.draw_type)
        self.color_drawing = customtkinter.CTkRadioButton(self.frame_radio, text="Heat", variable=self.graph_type, value=1, command=self.draw_type)

        self.bar_drawing.place(relx=0.2, rely=0)
        self.color_drawing.place(relx=0.6, rely=0)


        self.frame_btn2 = Frame(self.frame1, width=230, height=40, bg="#383838")
        self.frame_btn2.grid_propagate(0)
        self.frame_btn2.place(relx=0.0, rely=0.3)

        self.btn_sort = customtkinter.CTkButton(self.frame_btn2, text="Sort", command=self.sort_list)
        self.btn_sort.place(relx=0.23, rely=0)


        self.scale_speed = Scale(self.frame1, label="Speed: ", orient=HORIZONTAL, from_= 1, to = 500, length=230,
                                bg="#848484", troughcolor="#00b1ff", variable=self.speed_var, command=self.change_speed, relief="solid", cursor="hand2")
        self.scale_speed.place(relx=0.04, rely=0.5)
        self.scale_speed["highlightthickness"] = 0

        self.label_size = Label(self.frame1, text="Size of Array: ", bg="#383838", fg="white", font=("Ageo-Bold", 12))
        self.label_size.place(relx=0.1, rely=0.4)

        self.label_size2 = Label(self.frame1, text="", bg="#383838", fg="white",font=("Ageo-Bold", 12))
        self.label_size2.place(relx=0.6, rely=0.4)

        self.label_comparison = Label(self.frame1, text="Comparisons: 0", bg="#383838", fg="white", font=("Ageo-Bold", 12))
        self.label_comparison.place(relx=0.1, rely=0.65)


        self.frame_algo_info = Frame(self.frame1, bg="#383838", width=230, height=150, relief="sunken", bd=4)
        self.frame_algo_info.grid_propagate(0)
        self.frame_algo_info.place(relx=0.03, rely=0.7)

        self.label_avg = Label(self.frame_algo_info, bg="#383838", fg="white", text=self.information[self.algo_var.get()], font=("Ageo-bold", 14))
        self.label_avg.pack_propagate(0)
        self.label_avg.place(relx=0.1, rely=0.1)


        self.BackButton = customtkinter.CTkButton(self.frame1, text="MAIN MENU", command=self.Back, font=("Ageo-bold", 16))
        self.BackButton.grid_propagate(0)
        self.BackButton.place(relx=0.2, rely=0.94)


        self.frame2 = Frame(self.root, width=self.CANVAS_X, height=self.CANVAS_Y)
        self.frame2.pack(side=LEFT)
        self.canva = Canvas(self.frame2, width=self.CANVAS_X, height=self.CANVAS_Y, bg="#545454")
        self.canva.pack()


    def Back(self):
        self.root.destroy()
        Process = Files.Thread_Maker.START()
        Process.start()

    def Close(self):
        if messagebox.askokcancel("Quit", "Do you want to quit this amazing program?"):
            self.root.destroy()
            quit()

    def paint(self, colortype):

        self.canva.delete("all")

        self.starting_point = 2

        self.rec_width = self.CANVAS_X / self.size_var.get()

        for i in range(0, len(self.numbers)):
            self.numbers[i] = int(self.numbers[i])

        if self.TYPE == 0:

            for i in range(len(self.numbers)):
                self.canva.create_rectangle(self.starting_point, self.CANVAS_Y - self.numbers[i], self.starting_point + self.rec_width, self.CANVAS_Y, fill=colortype[i],outline="white")
                self.label_value = Label(self.canva, text=self.numbers[i], bg="#4781a8",
                                         fg="white",
                                         font=("Ageo-Bold", 12))
                self.canva.create_window(self.starting_point + 16, self.CANVAS_Y - self.numbers[i] + 12,
                                         window=self.label_value)
                print(self.numbers[i])
                self.starting_point += self.rec_width
        else:

            for i in range(len(self.numbers)):
                hls_color = hls_to_rgb(colortype[i] / 360, 0.6, 1)
                red = hls_color[0] * 255
                green = hls_color[1] * 255
                blue = hls_color[2] * 255
                self.canva.create_rectangle(self.starting_point, 0, self.starting_point + self.rec_width, self.CANVAS_Y,
                                       outline="", fill="#%02x%02x%02x" % (int(red), int(green), int(blue)))
                self.label_value = Label(self.canva, text=self.numbers[i], bg="#4781a8",
                                         fg="midnight blue",
                                         font=("Ageo-Bold", 12))
                self.canva.create_window(self.starting_point + 16, self.CANVAS_Y - self.numbers[i] + 12,
                                         window=self.label_value)
                print(self.numbers[i])
                self.starting_point += self.rec_width
        self.frame2.update()


    def open_new(self):
        path = easygui.fileopenbox()
        with open(path) as file:
            self.numbers = [line.rstrip() for line in file]

        for i in range(0, len(self.numbers)):
            self.numbers[i] = int(self.numbers[i])

        print(type(self.numbers[0]))

        return len(self.numbers)


    def new_list(self):
        numbers = []
        self.label_comparison.configure(text="Comparisons: 0")
        self.label_size2.configure(textvariable=self.size_var)

        path = easygui.fileopenbox()
        with open(path) as file:
            self.numbers = [line.rstrip() for line in file]
            print(self.numbers)
            print(len(self.numbers))

        for i in range(0, len(self.numbers)):
            self.numbers[i] = int(self.numbers[i])

        self.size_var.set(len(self.numbers))

        if self.TYPE == 0:
            colortype = ["#4781a8" for x in self.numbers]

        else:
            colortype = [((int)(x * 360) / self.CANVAS_Y) for x in self.numbers]

        self.paint(colortype)

    def shuffle_list(self):
        shuffle(self.numbers)
        self.label_comparison.configure(text="No. of comparison: 0")

        if self.TYPE == 0:
            colortype = ["#4781a8" for x in self.numbers]

        else:
            colortype = [((int)(x * 360) / self.CANVAS_Y) for x in self.numbers]

        self.paint(colortype)


    def change_size(self, event):
        self.label_comparison.configure(text="Comparisons: 0")

        path = easygui.fileopenbox()
        with open(path) as file:
            numbers = [line.rstrip() for line in file]
            print(numbers)

        if self.TYPE == 0:
            colortype = ["#4781a8" for x in self.numbers]
        else:
            colortype = [((int)(x * 360) / self.CANVAS_Y) for x in self.numbers]
        self.paint(colortype)

    def change_speed(self, event):
        pass

    def sort_list(self):
        self.label_comparison.configure(text="Comparisons: 0")
        startsort = Thread(target=algochooser(self.numbers, self.paint, self.label_comparison, self.algo_var.get(), self.TYPE, self.speed_var.get()))
        startsort.start()

    def case_chooser(self, event):
        self.label_avg.pack_forget()
        self.label_avg.configure(text=self.information[self.algo_var.get()])

    def draw_type(self):
        self.TYPE = self.graph_type.get()
        if self.TYPE == 0:
            colortype = ["#4781a8" for x in self.numbers]
        else:
            colortype = [((int)(x * 360) / self.CANVAS_Y) for x in self.numbers]
        self.paint(colortype)




