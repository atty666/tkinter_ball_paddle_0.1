from tkinter import *
import random
import time


class Ball:
    def __init__(self, canvas, rocket):
        self.canvas = canvas
        self.rocket = rocket
        self.colors = ['yellow']
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

    def hit_rocket(self, pos):
        rocket_pos = self.canvas.coords(self.rocket.id)
        if pos[2] >= rocket_pos[0] and pos[0] <= rocket_pos[2]:
            if rocket_pos[1] <= pos[3] <= rocket_pos[3]:
                return True
        return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 1
        if pos[3] >= self.canvas_height:
            self.y = -1
        if self.hit_rocket(pos) == True:
            self.y = -3
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3

        #print(self.canvas.coords(self.id))      #enable for view ball coords

    def change_color(self):
        self.color_index = (self.color_index + 1) % len(self.colors)
        self.canvas.itemconfig(self.id,
                               fill=self.colors[self.color_index])


class Rocket:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10,
                                          fill=color)
        self.canvas.move(self.id, 250, 320)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all("<KeyPress-Left>", self.turn_left)
        self.canvas.bind_all("<KeyPress-Right>", self.turn_right)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0

        print(self.canvas.coords(self.id))

    def turn_left(self, evt):
        self.x = -2

    def turn_right(self, evt):
        self.x = 2


tk = Tk()
tk.title('Game')
tk.resizable(False, False)
tk.wm_attributes("-topmost", True)

canvas = Canvas(tk, width=600, height=400, bd=0,
                highlightthickness=0)
canvas.pack()
tk.update()

rocket = Rocket(canvas, 'blue')
ball = Ball(canvas, rocket)

while True:
    ball.draw()
    ball.change_color()
    rocket.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)

# tk.update()
# tk.mainloop()
