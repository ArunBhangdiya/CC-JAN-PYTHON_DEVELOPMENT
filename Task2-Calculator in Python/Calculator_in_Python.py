from tkinter import *

root = Tk()
root.geometry("315x330")
root.resizable(0, 0)
root.title('Calculator')

expression = ""

input_text = StringVar()

def btn_clear():
    global expression
    expression = ""
    input_text.set("")

def btn_click(item):
    global expression
    expression = expression + str(item)
    i=input_text.set(expression)

def btn_equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = ""

input_frame = Frame(root, width=50, height=20, bd=0,
                    highlightbackground="black", highlightcolor="black", highlightthickness=0.5,border=1)

input_frame.pack(side=TOP)

input_field = Entry(input_frame, font=('arial', 15, 'bold'),
                    textvariable=input_text, width=25,border=1, bd=1, justify=RIGHT)

input_field.grid(row=0, column=0)

input_field.pack(ipady=10)

btns_frame = Frame(root, width=312, height=272.5, bg="white")

btns_frame.pack()

b = Button(btns_frame,text="Calculator", width=33, height=3, bd=0,  bg="white",border=1,
                cursor="hand2").grid(row=0,  padx=1,columnspan=3, pady=1)

bdivide = Button(btns_frame, text="/", fg="black", width=10, height=3, bd=0,  bg="white",border=1,
                 command=lambda: btn_click("/")).grid(row=0, column=3, padx=1, pady=1)

b7 = Button(btns_frame, text="7", fg="black", width=10, height=3, bd=0,  bg="white",border=1,
                command=lambda: btn_click(7)).grid(row=1, column=0, padx=1, pady=1)
b8 = Button(btns_frame, text="8", fg="black", width=10, height=3, bd=0,  bg="white",border=1,
                command=lambda: btn_click(8)).grid(row=1, column=1, padx=1, pady=1)
b9 = Button(btns_frame, text="9", fg="black", width=10, height=3, bd=0,  bg="white",border=1,
               command=lambda: btn_click(9)).grid(row=1, column=2, padx=1, pady=1)
bmultiply = Button(btns_frame, text="*", fg="black", width=10, height=3, bd=0,  bg="white",border=1,
                   command=lambda: btn_click("*")).grid(row=1, column=3, padx=1, pady=1)

b4 = Button(btns_frame, text="4", fg="black", width=10, height=3, bd=0,  bg="white",border=1,
               command=lambda: btn_click(4)).grid(row=2, column=0, padx=1, pady=1)
b5 = Button(btns_frame, text="5", fg="black", width=10, height=3, bd=0,  bg="white",border=1,
               command=lambda: btn_click(5)).grid(row=2, column=1, padx=1, pady=1)
b6 = Button(btns_frame, text="6", fg="black", width=10, height=3, bd=0,  bg="white",border=1,
              command=lambda: btn_click(6)).grid(row=2, column=2, padx=1, pady=1)
bminus = Button(btns_frame, text="-", fg="black", width=10, height=3, bd=0,  bg="white",border=1,
                command=lambda: btn_click("-")).grid(row=2, column=3, padx=1, pady=1)

b1 = Button(btns_frame, text="1", fg="black", width=10, height=3, bd=0,  bg="white",border=1,
              command=lambda: btn_click(1)).grid(row=3, column=0, padx=1, pady=1)
b2 = Button(btns_frame, text="2", fg="black", width=10, height=3, bd=0,  bg="white",border=1,
              command=lambda: btn_click(2)).grid(row=3, column=1, padx=1, pady=1)
b3 = Button(btns_frame, text="3", fg="black", width=10, height=3, bd=0,  bg="white",border=1,
                command=lambda: btn_click(3)).grid(row=3, column=2, padx=1, pady=1)
bplus = Button(btns_frame, text="+", fg="black", width=10, height=3, bd=0,  bg="white",border=1,
               command=lambda: btn_click("+")).grid(row=3, column=3, padx=1, pady=1)

bclear = Button(btns_frame, text="C", fg="black", width=10, height=3, bd=0,  bg="white",border=1,
                command=lambda: btn_clear()).grid(row=4, column=0, padx=1, pady=1)
b0 = Button(btns_frame, text="0", fg="black", width=10, height=3, bd=0,  bg="white",border=1, 
              command=lambda: btn_click(0)).grid(row=4, column=1, padx=1, pady=1)
bpoint = Button(btns_frame, text=".", fg="black", width=10, height=3, bd=0,  bg="white",border=1,
                command=lambda: btn_click(".")).grid(row=4, column=2, padx=1, pady=1)
bequals = Button(btns_frame, text="=", fg="black", width=10, height=3, bd=0,  bg="white",border=1,
                command=lambda: btn_equal()).grid(row=4, column=3, padx=1, pady=1)

root.mainloop()