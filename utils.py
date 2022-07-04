def count_percent(num, total_num) -> int:
    """
    Считает процент от общего числа
    :param num: число которое необходимо отобразить в процентах
    :param total_num: общее число (всего)
    :return: integer
    """
    return int(num * 100 / total_num)


def display_statistics(wrong, correct) -> None:
    """
    Выводит на экран статистику по игре
    :param wrong: количество неправильных ответов
    :param correct: количество правильных ответов
    :return: None
    """
    total_count = wrong + correct
    print(f"Правильных ответов: {correct}")
    print(f"Количество ошибок: {wrong}")
    print(f"Процент правильных ответов: {count_percent(correct, total_count)}")
    print(f"Процент неправильных ответов: {count_percent(wrong, total_count)}")


def play_again() -> bool:
    """
    Реализует логику завершения, либо продолжения игры
    :return: True or False
    """
    print("Сыграть еще раз?")
    answer = input("Введите 'да' или 'нет': ")
    while not answer.lower() in ['да', 'нет']:
        print("Неверный ввод, попробуйте еще раз ... ")
        answer = input("Введите 'да' или 'нет': ")
    if answer.lower() == 'нет':
        return False
    return True
