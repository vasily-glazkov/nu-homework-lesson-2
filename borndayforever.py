"""
МОДУЛЬ 5. В проекте создать новый модуль borndayforewer.py
Написать или модернизировать программу (МОДУЛЬ 3) используя условные операторы и цикл while:
Просим пользователя ввести год рождения А.С. Пушкина до тех пор, 
пока он не ввел правильный год, после этого спрашиваем 
день рождения до тех пор, пока он не ввел верный день. 
После верного ответа выводим в терминал 'Верно' и выходим из программы
"""

keep_asking_year = True
keep_asking_day = True

while keep_asking_year:  # продолжаем спрашивать пока True
    question_request = input("В каком году родился А.С. Пушкин?\n")  # 1799

    while not question_request.isdigit():
        print("Введено не целое число")
        question_request = input("В каком году родился А.С. Пушкин?\n")

    if int(question_request) == 1799:
        print("Верно")
        keep_asking_year = False  # меняем флаг на false чтобы выйти из цикла

while keep_asking_day:
    question_day = input("Какого числа? \n")  # 26 (мая)

    while not question_day.isdigit():
        print("Введено не целое число")
        question_day = input("Какого числа? \n")

    if int(question_day) == 26:
        print("Верно")
        keep_asking_day = False  # меняем флаг на false чтобы выйти из цикла
