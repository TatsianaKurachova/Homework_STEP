from tkinter import*

root=Tk()
root.title("Сумма")

class Calc():

    def __init__(self):
        self.window = Tk()
        
        self.entry_frame = Frame(self.window)
        self.entry_frame.pack()

#Создаем элемент Надпись 
        self.a_label = Label(self.entry_frame, text = "Введите первое слагаемое")
        self.a_label.pack()
        
#Создаем текстовое поле для ввода первого слагаемого
        self.a_entry = Entry(self)
        self.a_entry.pack(self.entry_frame)

#Создаем элемент Надпись
        self.b_label = Label(self,text="Введите второе слагаемое") 
        self.b_label.pack()

#Создаем текстовое поле для ввода второго слагаемого 
        self.b_entry = Entry(self) 
        self.b_entry.pack(self.entry_frame)

#Создаем текстовое поле для вывода в него ответа  
        self.answer_label = Label(self.entry_frame,
                                         text="Ответ:")
        self.answer_label.pack ()
        self.answer_entry = Entry(self.entry_frame)
        self.answer_text = StringVar()
        self.answer = Label(self.entry_frame,
                               textvariable=self.answer_text)
        self.answer.pack()
        
        self.button = Button(self.entry_frame,
                                     text="Найти сумму",
                                     command=self.addition)
        self.button.pack()

        mainloop()

#Создаем метод для нахождения суммы 
    def addition (self):
        a=int(self.a.get())
        b=int(self.b.get())
        self.answer_text.set(eval(a) + eval(b))    

calc=Calc()
root.mainloop()