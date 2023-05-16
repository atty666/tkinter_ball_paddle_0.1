from tkinter import *
import random
import time


class Ball:
    def __init__(self, canvas):
        self.canvas = canvas
        self.colors = ['yellow', 'blue']
        self.color_index = 0
        self.id = canvas.create_oval(10, 10, 35, 35,
                                     fill=self.colors[self.color_index])
        self.canvas.move(self.id, 245, 100)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 1
        if pos[3] >= self.canvas_height:
            self.y = -1
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3

        # print(self.canvas.coords(self.id))      #enable for view ball coords

    def change_color(self):
        self.color_index = (self.color_index + 1) % len(self.colors)
        self.canvas.itemconfig(self.id,
                               fill=self.colors[self.color_index])


tk = Tk()
tk.title('Game')
tk.resizable(False, False)
tk.wm_attributes("-topmost", True)

canvas = Canvas(tk, width=600, height=400, bd=0,
                highlightthickness=0)
canvas.pack()
tk.update()

ball = Ball(canvas)

while True:
    ball.draw()
    ball.change_color()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)

# tk.update()
# tk.mainloop()
