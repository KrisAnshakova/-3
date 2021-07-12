def user_date(**kwargs):
    """ Сбор данных о пользоватее """
    name=list(input("Введите ФИО-  ").split( ))
    age = int(input('Возраст- '))
    city = str(input('Город проживания-  '))
    phone = int(input('Номер телефона- '))
    info = [*(name), age, city, phone]
    return info
print (*user_date())
