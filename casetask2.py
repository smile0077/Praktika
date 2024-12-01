import art  # Подключаем модуль art
from datetime import datetime  # Подключаем модуль datetime

def draw_digit(digit):
    """Возвращает представление цифры в виде звёздочек."""
    patterns = {
        '0': [" *** ",
              "*   *",
              "*   *",
              "*   *",
              " *** "],
        '1': ["  *  ",
              "  *  ",
              "  *  ",
              "  *  ",
              "  *  "],
        '2': [" *** ",
              "    *",
              " *** ",
              "*    ",
              " *** "],
        '3': [" *** ",
              "    *",
              " *** ",
              "    *",
              " *** "],
        '4': ["*   *",
              "*   *",
              " *** ",
              "    *",
              "    *"],
        '5': [" *** ",
              "*    ",
              " *** ",
              "    *",
              " *** "],
        '6': [" *** ",
              "*    ",
              " *** ",
              "*   *",
              " *** "],
        '7': [" *** ",
              "    *",
              "   * ",
              "  *  ",
              " *   "],
        '8': [" *** ",
              "*   *",
              " *** ",
              "*   *",
              " *** "],
        '9': [" *** ",
              "*   *",
              " *** ",
              "    *",
              " *** "],
        ' ': ["     ",
              "     ",
              "     ",
              "     ",
              "     "]  # Пробел
    }
    return patterns[digit]

def draw_date(date):
    """Выводит дату в формате дд мм гггг с использованием звёздочек."""
    lines = ['' for _ in range(5)]  # 5 строк для отображения
    for char in date:
        digit_lines = draw_digit(char)
        for i in range(5):
            lines[i] += digit_lines[i] + '  '  # Добавляем пробел между цифрами

    for line in lines:
        print(line)

def get_weekday(day, month, year):
    """Определяет день недели для заданной даты."""
    weekdays = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
    date = datetime(year, month, day)
    return weekdays[date.weekday()]

def is_leap_year(year):
    """Определяет, является ли год високосным."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def calculate_age(birth_date):
    """Вычисляет возраст пользователя на основе даты рождения."""
    today = datetime.now()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

def main():
    # Выводим заголовок с помощью модуля art
    print(art.text2art("Case-task 2:)"))

    # Запрашиваем у пользователя дату рождения по частям
    day = int(input("Введите день рождения (дд): "))
    month = int(input("Введите месяц рождения (мм): "))
    year = int(input("Введите год рождения (гггг): "))
    
    # Формируем полную дату
    birth_date = datetime(year, month, day)

    # Выводим дату рождения в формате звёздочек
    print("\nДата рождения:")
    draw_date(f"{day:02d} {month:02d} {year}")

    # Определяем день недели
    weekday = get_weekday(day, month, year)
    print(f"День недели: {weekday}")

    # Проверяем, является ли год високосным
    leap_year = is_leap_year(year)
    print(f"Високосный год: {'Да' if leap_year else 'Нет'}")

    # Вычисляем возраст
    age = calculate_age(birth_date)
    print(f"Текущий возраст: {age} лет")

    # Получаем текущую дату и выводим её
    current_date = datetime.now().strftime("%d %m %Y")
    print("\nТекущая дата:")
    draw_date(current_date)

if __name__ == "__main__":  # Исправлено условие
    main()
