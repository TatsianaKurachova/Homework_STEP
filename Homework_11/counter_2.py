import tkinter

# create the main window
root = tkinter.Tk()
root.title('Подсчет слов с буковой е')

# создание поля для ввода строки
label = tkinter.Label(root, text='Введите строку:')
label.grid(row=0, column=0, sticky='W')

entry = tkinter.Entry(root)
entry.grid(row=0, column=0, columnspan=2)

# создание строки для вывода количетсва слов с буквой е
result_label = tkinter.Label(root, text='Количество слов с буквой "е": ')
result_label.grid(row=2, column=0, sticky='W')
result_field = tkinter.Entry(root)
result_field.grid(row=2, column=1)

# функция подсчета
def counter():
    text = entry.get()
    # разбиваем на слова
    words = text.split()
    # проверяем и считаем на наличие буквы "e"
    counter = 0
    for word in words:
        if 'е' in word:
            counter += 1
    # выводи результат
    result_field.delete(0, tkinter.END)
    result_field.insert(0, counter)

# создаем кнопку
counter_button = tkinter.Button(root, text="Посчитать", command=counter, bg='black', fg='white')
counter_button.grid(row=3, column=0)

# запускаем цикл
root.mainloop()