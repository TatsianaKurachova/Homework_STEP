from tkinter import*

# create the main window
root = Tk()
root.title('Телефонная книга')
root.geometry("400x200")

# создание поля для ввода имени абонента
label_name = Label(root, text='Введите имя абонента:')
label_name.grid(row=0, column=0)
entry_name = Entry(root)
entry_name.grid(row=0, column=1)

# создание поля для ввода номера телефона
label_number_of_phone = Label(root, text='Введите номер телефона:')
label_number_of_phone.grid(row=1, column=0)
entry_number_of_phone = Entry(root)
entry_number_of_phone.grid(row=1, column=1)

# функция
def add():
    name = entry_name.get()
    number = entry_number_of_phone.get()
    list_text.insert(END,name + "\t"+ number + "\n")
    
# создаем кнопку
button = Button(root, text="Добавить", command=add)
button.grid(row=2, column=1)

list_text = Text(root, height = 6, width = 40)
list_text.grid(row=3, column=1)

# запускаем цикл
root.mainloop()