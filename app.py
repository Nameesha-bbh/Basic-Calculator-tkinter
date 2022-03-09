from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("350x450")
root.resizable(False,False)
root.configure(bg="#3399ff")
root.iconbitmap("calculator_icon.ico")

equationFont = ('ariel',20,'bold')
buttonFont = ('new times roman', 12)
equation = StringVar()
equation.set('0')
expression = ''

def press(n):
    global expression
    expression += str(n)
    equation.set(expression)
    
def evaluate():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ''
    except:
        equation.set('ERROR')
        expression = ''
    
def clear():
    global expression
    expression = ''
    equation.set('0')
    
def backspace():
    try:
        global expression
        expression = expression.rstrip(expression[-1])
        equation.set(expression)
    except:
        pass
    
equationFrame = Frame(root, bg="#3399ff")
equationFrame.pack()

buttonFrame = Frame(root, bg="#3399ff")
buttonFrame.pack()


equationField = Entry(equationFrame, textvariable=equation, font=equationFont, justify='right', state="disabled")
equationField.pack(ipadx=10,ipady=10,pady=20)

button1 = Button(buttonFrame, text='1', font=buttonFont, relief='ridge', bg='#80bfff', borderwidth=1, width=8, height=3, command=lambda: press(1))
button2 = Button(buttonFrame, text='2', font=buttonFont, relief='ridge', bg='#80bfff', borderwidth=1, width=8, height=3, command=lambda: press(2))
button3 = Button(buttonFrame, text='3', font=buttonFont, relief='ridge', bg='#80bfff', borderwidth=1, width=8, height=3, command=lambda: press(3))
plus = Button(buttonFrame, text='+', font=buttonFont, relief='ridge', bg='#80bfff', borderwidth=1, width=8, height=3, command=lambda: press('+'))

button4 = Button(buttonFrame, text='4', font=buttonFont, relief='ridge', bg='#80bfff', borderwidth=1, width=8, height=3, command=lambda: press(4))
button5 = Button(buttonFrame, text='5', font=buttonFont, relief='ridge', bg='#80bfff', borderwidth=1, width=8, height=3, command=lambda: press(5))
button6 = Button(buttonFrame, text='6', font=buttonFont, relief='ridge', bg='#80bfff', borderwidth=1, width=8, height=3, command=lambda: press(6))
minus = Button(buttonFrame, text='-', font=buttonFont, relief='ridge', bg='#80bfff', borderwidth=1, width=8, height=3, command=lambda: press('-'))

button7 = Button(buttonFrame, text='7', font=buttonFont, relief='ridge', bg='#80bfff', borderwidth=1, width=8, height=3, command=lambda: press(7))
button8 = Button(buttonFrame, text='8', font=buttonFont, relief='ridge', bg='#80bfff', borderwidth=1, width=8, height=3, command=lambda: press(8))
button9 = Button(buttonFrame, text='9', font=buttonFont, relief='ridge', bg='#80bfff', borderwidth=1, width=8, height=3, command=lambda: press(9))
multiply = Button(buttonFrame, text='*', font=buttonFont, relief='ridge', bg='#80bfff', borderwidth=1, width=8, height=3, command=lambda: press('*'))

button0 = Button(buttonFrame, text='0', font=buttonFont, relief='ridge', bg='#80bfff', borderwidth=1, width=8, height=3, command=lambda: press(0))
decimal = Button(buttonFrame, text='.', font=buttonFont, relief='ridge', bg='#80bfff', borderwidth=1, width=8, height=3, command=lambda: press('.'))
clear = Button(buttonFrame, text='C', font=buttonFont, relief='ridge', bg='#80bfff', borderwidth=1, width=8, height=3, command=clear)
divide = Button(buttonFrame, text='/', font=buttonFont, relief='ridge', bg='#80bfff', borderwidth=1, width=8, height=3, command=lambda: press('/'))

equal = Button(buttonFrame, text='=', font=buttonFont, relief='ridge', bg='#80bfff', borderwidth=1, width=8, height=3, command=evaluate)
backspace = Button(buttonFrame, text='<<', font=buttonFont, relief='ridge', bg='#80bfff', borderwidth=1, width=8, height=3,command=backspace)

button1.grid(row=0,column=0)
button2.grid(row=0,column=1)
button3.grid(row=0,column=2)
plus.grid(row=0,column=3)

button4.grid(row=1,column=0)
button5.grid(row=1,column=1)
button6.grid(row=1,column=2)
minus.grid(row=1,column=3)

button7.grid(row=2,column=0)
button8.grid(row=2,column=1)
button9.grid(row=2,column=2)
multiply.grid(row=2,column=3)

button0.grid(row=3,column=0)
decimal.grid(row=3,column=1)
clear.grid(row=3,column=2)
divide.grid(row=3,column=3)

equal.grid(row=4,column=0,columnspan=3,sticky='nsew')
backspace.grid(row=4,column=3)


root.mainloop()