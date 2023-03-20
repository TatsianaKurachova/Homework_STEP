import typing

a=int(input("Введите число а ="))
operation = str(input("Операция:"))
b=int(input("Введите число b ="))

def calc (a:int, b:int, operation:str):
   if "+" in operation:
      return str (a+b)
   if "-"in operation:
      return str (a-b)
   if "*" in operation:
      return str (a*b)
   if "/" in operation:
      return str (a/b)
   else:
      return str("Операция не поддерживается")   

print ('Ответ:', calc(a, b, operation))