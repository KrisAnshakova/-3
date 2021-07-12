def new_fan():
    """"Делит заданные числа"""
    val1=int(input("Первое число-  "))
    val2=int(input("Второе число-  "))
    if val1>0 and val2>0:
        result = val1/val2
    else:
        print("Введи числа больше нуля")

    return result

print(new_fan())