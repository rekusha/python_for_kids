import random, time, os
from tkinter import *

class Ball:
    def __init__(self, canvas, paddle, color):
        self.score = 0
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill = color)
        self.canvas.move(self.id, 245, 100)
        self.x = 0.0
        self.y = 0.0
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False
        self.canvas.bind_all('<KeyPress-space>', self.game_start) #1. Задержка перед началом игры

    def game_start(self, evt): #1. Задержка перед началом игры
        if self.x == 0 and self.y == 0:
            starts = [-2, -1, 1, 2]
            random.shuffle(starts)
            self.x = starts[0]
            random.shuffle(starts)
            self.y = starts[0]
            canvas.delete(start_text)
        
    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
            return False
        
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if (pos[1] <= 0) or (pos[3] >= self.canvas_height):
            self.y *= -1
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if self.hit_paddle(pos) == True:
            self.y *= -1
            self.score += 1 #4. Счет в игре
            x = self.x
            pad = paddle.x
            if ((pad > 0) & (x > 0)) or ((pad < 0) & (x < 0)): #3. Ускорение мяча
                if self.x > 0:
                    self.x += 0.1
                if self.x < 0:
                    self.x -= 0.1
                if self.y > 0:
                    self.y += 0.1
                if self.y < 0:
                    self.y -= 0.1
            elif (((pad > 0) & (x < 0)) or ((pad < 0) & (x > 0))) & (x > 0.1): #3. Ускорение мяча (Замедление)
                if self.x > 0:
                    self.x -= 0.1
                if self.x < 0:
                    self.x += 0.1
                if self.y > 0:
                    self.y -= 0.1
                if self.y < 0:
                    self.y += 0.1
        if (pos[0] <= 0) or (pos[2] >= self.canvas_width):
            self.x *= -1

class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill = color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if (pos[0] <= 0) or (pos[2] >= self.canvas_width):
            self.x = 0

    def turn_left(self, evt):
        if self.canvas.coords(self.id)[0] <= 0:
            self.x = 0
        else:
            self.x = -2

    def turn_right(self, evt):
        if self.canvas.coords(self.id)[2] >= self.canvas_width:
            self.x = 0
        else:
            self.x = 2

tk = Tk()
tk.title("Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

while 1:
    paddle = Paddle(canvas, 'blue')
    ball = Ball(canvas, paddle, 'red')
    score1 = 0 #4. Счет в игре
    score_text = canvas.create_text(ball.canvas.winfo_width()-100, 50,
                                text='0', font = ('Courier', 50)) #4. Счет в игре
    start_text = canvas.create_text(ball.canvas.winfo_width()/2, ball.canvas.winfo_height()/2,
                                text='Space to start', font = ('Courier', 30)) #1. Задержка перед началом игры

    while 1:
        if ball.hit_bottom == False:
            ball.draw()
            paddle.draw()
        else:
            time.sleep(1)
            canvas.create_text(ball.canvas.winfo_width()/2, ball.canvas.winfo_height()/2,
                               text='GAME OVER', font = ('Courier', 50)) #2. Экран «Конец игры»
            time.sleep(2)
            break
        if score1 != ball.score: #4. Счет в игре
            canvas.delete(score_text)
            score_text = canvas.create_text(ball.canvas.winfo_width()-100, 50, text=ball.score, font = ('Courier', 50))
        tk.update_idletasks()
        tk.update()
        time.sleep(0.01)
