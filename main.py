from tkinter import *
import random
import time


class Score:
    def __init__(self, canvas, color):
        self.score = 0
        self.canvas = canvas
        self.id = canvas.create_text(570, 30, text=self.score,
                                     fill=color,
                                     font=("Helvetica", 30))

    def hit(self):
        self.score += 1
        self.canvas.itemconfig(self.id, text=self.score)


class Ball:
    def __init__(self, canvas, rocket, score):
        self.canvas = canvas
        self.rocket = rocket
        self.score = score
        self.colors = 'yellow'
        self.color_index = 0
        self.id = canvas.create_oval(10, 10, 35, 35,
                                     fill=self.colors)
        self.canvas.move(self.id, 245, 100)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

    def hit_rocket(self, pos):
        rocket_pos = self.canvas.coords(self.rocket.id)
        if pos[2] >= rocket_pos[0] and pos[0] <= rocket_pos[2]:
            if rocket_pos[1] <= pos[3] <= rocket_pos[3]:
                self.x += self.rocket.x
                self.score.hit()
                return True
        return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if self.hit_rocket(pos):
            self.y = -3
        if pos[0] <= 0:
            self.x = 5
        if pos[2] >= self.canvas_width:
            self.x = -5

        # print(self.canvas.coords(self.id))      #enable for view ball coords


class Rocket:
    def __init__(self, canvas, color):
        self.started = False
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10,
                                          fill=color)
        self.canvas.move(self.id, 250, 320)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all("<KeyPress-Left>", self.turn_left)
        self.canvas.bind_all("<KeyPress-Right>", self.turn_right)
        self.canvas.bind_all("<Button-1>", self.start_game)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0

        # print(self.canvas.coords(self.id))

    def turn_left(self, evt):
        self.x = -6

    def turn_right(self, evt):
        self.x = 6

    def start_game(self, evt):
        self.started = True


def quit_game():
    tk.destroy()


def quit_button():
    quit_game_button = Button(canvas,
                              text='Quit',
                              command=quit_game)
    quit_game_button.place(x=200, y=350)


#def restart_game():

def restart_button():
    restart_game_button = Button(canvas,
                                 text='Restart',
                                 command=restart_game)
    restart_game_button.place(x=350, y=350)


tk = Tk()
tk.title('Game')
tk.resizable(False, False)
tk.wm_attributes("-topmost", True)

canvas = Canvas(tk, width=600, height=400, bd=0,
                highlightthickness=0)
canvas.pack()
tk.update()

score = Score(canvas, "green")
rocket = Rocket(canvas, 'blue')
ball = Ball(canvas, rocket, score)
game_over_text = canvas.create_text(300, 200, text="GAME OVER",
                                    state='hidden',
                                    font=('Helvetica', 40))

while True:
    # if ball.hit_bottom == False and rocket.stared == True:
    if not ball.hit_bottom and rocket.started:
        ball.draw()
        rocket.draw()

    if ball.hit_bottom:
        time.sleep(0.3)
        canvas.itemconfig(game_over_text, state="normal")
        quit_button()
        #restart_button()

    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
