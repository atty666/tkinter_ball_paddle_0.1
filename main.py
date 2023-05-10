from tkinter import *
import random
import time

tk = Tk()
tk.title('Game')
tk.resizable(False, False)
tk.wm_attributes("-topmost", 1, "-fullscreen", 0)

canvas = Canvas(tk, width=600, height=400, bd=0,
                highlightthickness=0)
canvas.pack()

tk.update()
tk.mainloop()
