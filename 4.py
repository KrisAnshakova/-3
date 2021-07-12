def my_func():
    x=int(input("Введи целое положительное число- "))
    y=int(input("Введи целое отрицательное число-  "))
    if y<0:
        result= x**y
        res1= 1/(x**(-y))
    else:
        print("Ввели не то число")
#        break      //что-то пошло не так
    print(result, res1)
    return result, res1
my_func()