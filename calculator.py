from tkinter import *

first_number = secound_number = opretor = None


def get_digit(digit):
    current = result_label["text"]
    new = current + str(digit)
    result_label.config(text=new)


def clear():
    result_label.config(text='')


def get_opretor(op):
    global first_number, opretor

    first_number = int(result_label["text"])
    opretor = op
    result_label.config(text='')


def get_result():
    global first_number, secound_number, opretor
    secound_number = int(result_label["text"])

    if opretor == "+":
        result_label.config(text=str(first_number + secound_number))
    elif opretor == "-":
        result_label.config(text=str(first_number - secound_number))
    elif opretor == "*":
        result_label.config(text=str(first_number * secound_number))
    else:
       if secound_number == 0:
           result_label.config(text=("error"))
       else:
           result_label.config(text=str(round(first_number / secound_number,2)))


root = Tk()
root.title("calculator")
root.geometry("328x518")

root.resizable(0, 0)
root.configure(background="black")

result_label = Label(root, text="", bg="black", fg="white")
result_label.grid(row=0, column=0, columnspan="5", pady=(90, 30), sticky="w")
result_label.config(font=("arial", 20, "bold"))


button7 = Button(
    root,
    text="7",
    bg="#00a65a",
    fg="white",
    width=6,
    height=3,
    command=lambda: get_digit(7),
)
button7.grid(row=1, column=0)
button7.config(font=("arial", 16))

button8 = Button(
    root,
    text="8",
    bg="#00a65a",
    fg="white",
    width=6,
    height=3,
    command=lambda: get_digit(8),
)
button8.grid(row=1, column=1)
button8.config(font=("arial", 16))

button9 = Button(
    root,
    text="9",
    bg="#00a65a",
    fg="white",
    width=6,
    height=3,
    command=lambda: get_digit(9),
)
button9.grid(row=1, column=2)
button9.config(font=("arial", 16))

button_add = Button(
    root,
    text="+",
    bg="#00a65a",
    fg="white",
    width=6,
    height=3,
    command=lambda: get_opretor("+")
)
button_add.grid(row=1, column=3)
button_add.config(font=("arial", 16))

button4 = Button(
    root,
    text="4",
    bg="#00a65a",
    fg="white",
    width=6,
    height=3,
    command=lambda: get_digit(4),
)
button4.grid(row=2, column=0)
button4.config(font=("arial", 16))

button5 = Button(
    root,
    text="5",
    bg="#00a65a",
    fg="white",
    width=6,
    height=3,
    command=lambda: get_digit(5),
)
button5.grid(row=2, column=1)
button5.config(font=("arial", 16))

button6 = Button(
    root,
    text="6",
    bg="#00a65a",
    fg="white",
    width=6,
    height=3,
    command=lambda: get_digit(6),
)
button6.grid(row=2, column=2)
button6.config(font=("arial", 16))

button_sub = Button(
    root,
    text="-",
    bg="#00a65a",
    fg="white",
    width=6,
    height=3,
    command=lambda: get_opretor("-")
)
button_sub.grid(row=2, column=3)
button_sub.config(font=("arial", 16))

button1 = Button(
    root,
    text="1",
    bg="#00a65a",
    fg="white",
    width=6,
    height=3,
    command=lambda: get_digit(1),
)
button1.grid(row=3, column=0)
button1.config(font=("arial", 16))

button2 = Button(
    root,
    text="2",
    bg="#00a65a",
    fg="white",
    width=6,
    height=3,
    command=lambda: get_digit(2),
)
button2.grid(row=3, column=1)
button2.config(font=("arial", 16))

button3 = Button(
    root,
    text="3",
    bg="#00a65a",
    fg="white",
    width=6,
    height=3,
    command=lambda: get_digit(3),
)
button3.grid(row=3, column=2)
button3.config(font=("arial", 16))

button_mult = Button(
    root,
    text="x",
    bg="#00a65a",
    fg="white",
    width=6,
    height=3,
    command=lambda: get_opretor("*")
)
button_mult.grid(row=3, column=3)
button_mult.config(font=("arial", 16))

button_clr = Button(
    root, text="C", bg="#00a65a", fg="white", width=6, height=3, command=lambda: clear()
)
button_clr.grid(row=4, column=0)
button_clr.config(font=("arial", 16))

button0 = Button(root, text="0", bg="#00a65a", fg="white", width=6, height=3,command=lambda:get_digit(0))
button0.grid(row=4, column=1)
button0.config(font=("arial", 16))

button_div = Button(
    root,
    text="/",
    bg="#00a65a",
    fg="white",
    width=6,
    height=3,
    command=lambda: get_opretor("/")
)
button_div.grid(row=4, column=2)
button_div.config(font=("arial", 16))

button_equal = Button(
    root, text="=", bg="#00a65a", fg="white", width=6, height=3, command=get_result
)
button_equal.grid(row=4, column=3)
button_equal.config(font=("arial", 16))


root.mainloop()
