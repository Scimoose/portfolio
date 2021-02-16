
import tkinter as tk
import math

# ---- CONSTANTS ---- #
RED = "#F26849"
GREEN = "#6BF178"
TAN = "#F2EFC7"
FONT_NAME = "Segoe"
WORK_MIN = 45        # how many minutes are you planning to work/study?
SHORT_BREAK_MIN = 15 # how many minutes is break going to take?
WIDTH = 300
HEIGHT = 500
is_it_break = False
timer = None

# ---- TIMER RESET ---- # 

def reset():
    global timer
    global is_it_break

    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    is_it_break = False
    label.config(text="Timer")

# ---- TIMER MECHANISM ---- # 

def start_timer():
    count_down(WORK_MIN*60)

def break_timer():
    count_down(SHORT_BREAK_MIN*60)

# ---- COUNTDOWN MECHANISM ---- # 

def count_down(count):
    
    global is_it_break
    global timer

    if is_it_break is False:
        
        label.config(text="Work!")
        
        if count == 0:
            break_timer()
            label.config(text="Break!")
            is_it_break = True
    else:
        if count == 0:
            is_it_break = False
            label.config(text="Timer")

    minutes = math.floor(count / 60)
    seconds = count % 60

    if minutes < 10:
        minutes = f"0{minutes}"

    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        timer = window.after(1000, count_down, count-1)

# ---- UI SETUP ---- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=TAN)

canvas = tk.Canvas(width=WIDTH, height=HEIGHT, bd=-2, bg=TAN)
tomato_image = tk.PhotoImage(file="tomato.png")
canv_img = canvas.create_image((WIDTH/2,HEIGHT/2), image=tomato_image)
timer_text = canvas.create_text((WIDTH/2, HEIGHT/1.9), text="00:00", fill="white", font=(FONT_NAME, 28))
canvas.grid(column=1, row=1)

label = tk.Label(text="Timer")
label.config(font=(FONT_NAME, 36), fg=RED, bg=TAN)
label.grid(column=1, row=0)

button_start = tk.Button()
button_start.config(font=FONT_NAME, text="Start", fg=RED, bd=-2, bg=TAN, command=start_timer)
button_start.grid(column=0, row=2)

button_reset = tk.Button()
button_reset.config(font=FONT_NAME, text="Reset", fg=RED, bd=-2, bg=TAN, command=reset)
button_reset.grid(column=2, row=2)


window.mainloop()
