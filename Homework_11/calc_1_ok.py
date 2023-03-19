import tkinter as tk

class Addition:
    def __init__(self):
        self.window = tk.Tk()

        self.entry_frame = tk.Frame(self.window)
        self.entry_frame.pack()

# Создаем элемент Надпись
# Создаем текстовое поле для ввода первого слагаемого 
        self.a_label = tk.Label(self.entry_frame,
                                      text="Введите первое число:")
        self.a_label.pack()
        self.a_entry = tk.Entry(self.entry_frame)
        self.a_entry.pack()

# Создаем элемент Надпись
# Создаем текстовое поле для ввода второго слагаемого 
        self.b_label = tk.Label(self.entry_frame,
                                      text="Введитe второе число:")
        self.b_label.pack()
        self.b_entry = tk.Entry(self.entry_frame)
        self.b_entry.pack()

# Создаем элемент Надпись
# Создаем текстовое поле для вывода результата 
        self.result_label = tk.Label(self.entry_frame,
                                         text="Ответ:")
        self.result_label.pack ()
        self.result_entry = tk.Entry(self.entry_frame)
        self.result_text = tk.StringVar()
        self.result = tk.Label(self.entry_frame,
                               textvariable=self.result_text)
        self.result.pack()
        

        self.button = tk.Button(self.entry_frame,
                                     text="Найти сумму",
                                     command=self.addition)
        self.button.pack()

        tk.mainloop()
    
    def addition(self):
        a = self.a_entry.get()
        b = self.b_entry.get()
        self.result_text.set(eval(a) + eval(b))

add = Addition()