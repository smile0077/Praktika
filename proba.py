def get_digit_to_stars_mapping():
    return {
        '0': ["***", "* *", "* *", "* *", "***"],
        '1': ["  *", "  *", "  *", "  *", "  *"],
        '2': ["***", "  *", "***", "*  ", "***"],
        '3': ["***", "  *", "***", "  *", "***"],
        '4': ["* *", "* *", "***", "  *", "  *"],
        '5': ["***", "*  ", "***", "  *", "***"],
        '6': ["***", "*  ", "***", "* *", "***"],
        '7': ["***", "  *", "  *", "  *", "  *"],
        '8': ["***", "* *", "***", "* *", "***"],
        '9': ["***", "* *", "***", "  *", "***"],
    }

def print_digit_in_stars(digit, mapping):
    """Печатает цифру в виде звёздочек."""
    if digit in mapping:
        return mapping[digit]
    return ["   "] * 5  # Пустая строка для недопустимых символов

def print_birthday_with_stars(birthday):
    mapping = get_digit_to_stars_mapping()
    
    # Проверка на корректность формата ввода
    try:
        day, month, year = birthday.split()
        if not (day.isdigit() and month.isdigit() and year.isdigit()):
            raise ValueError("Дата должна содержать только цифры.")
        
        # Печать каждой строки для всех четырёх цифр
        for i in range(5):  # Каждая цифра имеет 5 строк
            for part in [day, month, year]:
                for digit in part:  # Итерируемся по каждой цифре в части
                    print(print_digit_in_stars(digit, mapping)[i], end=' ')
                print(end=' ')  # Пробел между день, месяц и год
            print()  # Переход на новую строку

    except ValueError as e:
        print(f"Ошибка ввода: {e}")

# Пример использования функции
user_birthday = "03 11 1990"
print_birthday_with_stars(user_birthday)
