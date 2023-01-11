import random
import time
from tkinter import *
from Files.Welcome_Screen import Window
from threading import *

class START(Thread):
    def run(self):
        root=Tk()
        Window(root)
        root.mainloop()