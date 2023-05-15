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


class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 35, 35, fill=color)
        self.canvas.move(self.id, 245, 100)

    def draw(self):
        pass


ball = Ball(canvas, 'blue')

while True:
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)


# tk.update()
# tk.mainloop()
