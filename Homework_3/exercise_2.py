a=int(input("Введите число а ="))
b=int(input("Введите число b ="))
c=int(input("Введите число c ="))
if (a>b>c):
    print('Самое большое', a)
elif (b>a>c):
    print('Самое большое', b)
elif (c>b>a):
    print('Самое большое', c)