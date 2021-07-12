def my_func():
    """Функция,которая принимает три позиционных аргумента,
     и возвращает сумму наибольших двух аргументов
     """
    numbers=[]
    i = 0
    while len(numbers)<3:
        num=int(input('Введите целое число- '))
        numbers.append(num)
        i=+1
    num1, num2, num3=numbers
    result = (sum(numbers)-min(num1, num2, num3))
    return result

print(my_func())