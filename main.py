import math
from cProfile import label
from cgitb import text
from msilib.schema import Font
from tkinter import *
from tkinter.font import BOLD
from turtle import title

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text = "00:00")
    title_label.config(text = "Timer")
    check_mark.config(text = "")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    if reps == 8:
        title_label.config(text = "Long Break", fg = RED)
        count_down(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        title_label.config(text = "Short break", fg = PINK)
        count_down(SHORT_BREAK_MIN * 60)
    else:
        title_label.config(text = "Work", fg = GREEN)
        count_down(WORK_MIN * 60)
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_mins = math.floor(count/60)
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    canvas.itemconfig(timer_text, text =f"{count_mins}:{count_seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks =""
        work_sessions = math.floor(reps/60)
        for _ in range(work_sessions):
            marks +=" ✔ "
        check_mark.config(text = marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text = "Timer", fg = GREEN,font=(FONT_NAME, 32, "bold"), highlightthickness=0, bg = YELLOW )
title_label.grid(column=1, row=0)

canvas = Canvas(width=220, height=240, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)

timer_text = canvas.create_text(100, 130, text = "00:00", fill= "white", font =(FONT_NAME, 35, "bold"))
canvas.grid(column = 1, row = 1)

start_button = Button(text = "start", highlightthickness=0, command = start_timer)
start_button.grid(column = 0, row = 2)

reset_button = Button(text = "reset", highlightthickness=0, command = reset_timer)
reset_button.grid(column = 2, row = 2)

check_mark = Label(text = " ✔ ", fg = GREEN, bg = YELLOW, font=(FONT_NAME, 32, "bold")) 
check_mark.grid(column = 1, row = 3)

window.mainloop()
