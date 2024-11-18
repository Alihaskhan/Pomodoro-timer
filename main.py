from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 0.05
LONG_BREAK_MIN = 20
CHECKMARK = "🗸"
reps = 0
WORK_SEC = WORK_MIN * 60
SHORT_BREAK_SEC = SHORT_BREAK_MIN * 60
LONG_BREAK_SEC = LONG_BREAK_MIN * 60
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
         count_down(LONG_BREAK_SEC)
         todo.config(text="Break", fg=RED)
    elif reps % 2 == 0 and reps != 8:
        count_down(SHORT_BREAK_SEC)
        todo.config(text="Break", fg=PINK)
    else:
        count_down(WORK_SEC)
        todo.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        for x in range(math.floor(reps / 2)):
            marks += CHECKMARK
        check.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(column=1, row=1)



todo = Label(text="Timer", font=(FONT_NAME, 30, "bold"), fg=GREEN ,bg=YELLOW)
todo.grid(column=1, row=0)

start = Button(text="Start", highlightthickness=0, command=start_timer)
start.grid(column=0, row=2)

reset = Button(text="Reset")
reset.grid(column=2, row=2)

check = Label(text="", font=(60) , bg=YELLOW, fg="black")
check.grid(column=1, row=3)

window.mainloop()


