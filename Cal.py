from tkinter import Tk,Entry, Button, StringVar




class Calculator:
    def __init__(self, master):
        root.title("Calculator")
        root.geometry('367x430+0+0')
        root.resizable(False, False)
        root.config(bg="#17161b")

        self.equation = StringVar()
        self.entry_value = ''






        Entry(width=17, bg='#E5FFCC', font=('Arial Bold', 28), textvariable=self.equation).place(x=0, y=0)

        Button(width=11, height=4, text='C', relief='flat', bg='#0066CC', command=self.clear).place(x=5, y=53)
        Button(width=11, height=4, text='/', relief='flat', bg='#CCE5FF', command=lambda: self.show('/')).place(x=95,  y=53)
        Button(width=11, height=4, text='x', relief='flat', bg='#CCE5FF', command=lambda: self.show('*')).place(x=185, y=53)
        Button(width=11, height=4, text='/', relief='flat', bg='#CCE5FF', command=lambda: self.show('/')).place(x=275, y=53)

        Button(width=11, height=4, text='7', relief='flat', bg='#CCE5FF', command=lambda: self.show('7')).place(x=5, y=128)
        Button(width=11, height=4, text='8', relief='flat', bg='#CCE5FF', command=lambda: self.show('8')).place(x=95, y=128)
        Button(width=11, height=4, text='9', relief='flat', bg='#CCE5FF', command=lambda: self.show('9')).place(x=185, y=128)
        Button(width=11, height=4, text='-', relief='flat', bg='#CCE5FF', command=lambda: self.show('-')).place(x=275,
                                                                                                                y=128)

        Button(width=11, height=4, text='4', relief='flat', bg='#CCE5FF', command=lambda: self.show('4')).place(x=5, y=203)
        Button(width=11, height=4, text='5', relief='flat', bg='#CCE5FF', command=lambda: self.show('5')).place(x=95, y=203)
        Button(width=11, height=4, text='6', relief='flat', bg='#CCE5FF', command=lambda: self.show('6')).place(x=185, y=203)
        Button(width=11, height=4, text='+', relief='flat', bg='#CCE5FF', command=lambda: self.show('+')).place(x=275,
                                                                                                                y=203)

        Button(width=11, height=4, text='1', relief='flat', bg='#CCE5FF', command=lambda: self.show('1')).place(x=5, y=278)
        Button(width=11, height=4, text='2', relief='flat', bg='#CCE5FF', command=lambda: self.show('2')).place(x=95,
                                                                                                                y=278)
        Button(width=11, height=4, text='3', relief='flat', bg='#CCE5FF', command=lambda: self.show('3')).place(x=185,y=278)

        Button(root, width=11, height=4, text='%', relief='flat', bg='#CCE5FF', command=lambda: self.show('%')).place(
            x=5, y=353)
        Button(width=11, height=4, text='0', relief='flat', bg='#CCE5FF', command=lambda: self.show('0')).place(x=95, y=353)
        Button(width=11, height=4, text='.', relief='flat', bg='#CCE5FF', command=lambda: self.show('.')).place(x=185, y=353)
        Button(width=11, height=9, text='=', relief='flat', bg='#CCE5FF', command=self.solve).place(x=275, y=278)

        # Button(width=11, height=4, text='+', relief='flat', bg='#CCE5FF', command=lambda: self.show('+')).place(x=270, y=275)

    def show(self, value):
       self.entry_value += str(value)
       self.equation.set(self.entry_value)


    def clear(self):
       self.entry_value = ''
       self.equation.set(self.entry_value)


    def solve(self):
       result = eval(self.entry_value)
       self.equation.set(result)

root = Tk()
Calculator = Calculator(root)
root.mainloop()
