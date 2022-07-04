"""
МОДУЛЬ 6. В проекте создать новый модуль victory.py

Используя любые средства написать программу викторина:
Выбрать минимум 5 известных людей и узнать их год рождения.
Программа должна по очереди спрашивать у пользователя год рождения знаменитости.
После того как пользователь ввел все ответы, программа считает и выводит на экран:
- количество правильных ответов
- количество ошибок
- процент правильных ответов (можно посчитать как ПРАВИЛЬНЫЕ ОТВЕТЫ*100/ВСЕГО ВОПРОСОВ)
- процент неправильных ответов
После вывода информации программа спрашивает пользователя хочет ли он начать игру сначала,
если да - то повторяем все сначала, если ответ нет - выходим из программы
"""
from utils import display_statistics, play_again

famous_people = {
    "Александр Пушкин": 1799,
    "Лев Толстой": 1828,
    "Гвидо ван Россум": 1956,
    "Алан Тьюринг": 1912,
    "Дмитрий Менделеев": 1834,
}

wrong = 0  # счетчик ошибок
correct = 0  # счетчик верных ответов
keep_playing = True

while keep_playing:
    while (wrong + correct) < len(famous_people):
        for key, value in famous_people.items():
            print(f"В каком году родился {key}?")
            answer = input("Ваш ответ (только цифры - 4 знака): ")

            while not answer.isdigit():
                print("Введено не целое число")
                answer = input("Ваш ответ (только цифры - 4 знака): ")

            if value == int(answer):
                correct += 1
                print("Верный ответ")
            else:
                wrong += 1
                print("Вы ошиблись")

        display_statistics(wrong, correct)  # Функции вынесены в файл utils.py
        keep_playing = play_again()

        if keep_playing:
            wrong = 0
            correct = 0
