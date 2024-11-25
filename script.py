class DigitalClock:
    def __init__(self):
        # Словарь для представления цифр в виде звёздочек
        self.digits_map = {
            '0': [" *** ", "*   *", "*   *", "*   *", " *** "],
            '1': ["  *  ", "  *  ", "  *  ", "  *  ", "  *  "],
            '2': [" *** ", "    *", " *** ", "*    ", " *** "],
            '3': [" *** ", "    *", " *** ", "    *", " *** "],
            '4': ["*   *", "*   *", " *** ", "    *", "    *"],
            '5': [" *** ", "*    ", " *** ", "    *", " *** "],
            '6': [" *** ", "*    ", " *** ", "*   *", " *** "],
            '7': [" *** ", "    *", "   * ", "  *  ", " *   "],
            '8': [" *** ", "*   *", " *** ", "*   *", " *** "],
            '9': [" *** ", "*   *", " *** ", "    *", " *** "],
            ' ': ["     ", "     ", "     ", "     ", "     "]  # Пробел
        }

    def print_digit_with_stars(self, digit):
        """Возвращает строковое представление цифры в виде звёздочек."""
        return self.digits_map[digit]

    def print_date_with_stars(self, date):
        """Выводит дату в формате дд мм гггг с цифрами в виде звёздочек."""
        # Разделение даты на части
        day, month, year = date.split()
        
        # Создание строк для вывода
        output_lines = [""] * 5
        
        # Обработка каждой цифры в дате
        for char in f"{day} {month} {year}":
            digit_lines = self.print_digit_with_stars(char)
            for i in range(5):
                output_lines[i] += digit_lines[i] + "  "

        # Вывод результата
        for line in output_lines:
            print(line)


def main():
    # Запрос даты рождения  пользователя
    date_of_birth = input("Введите дату рождения (дд мм гггг): ")
    
    # Создание экземпляра класса DigitalClock и вывод даты
    clock = DigitalClock()
    clock.print_date_with_stars(date_of_birth)


if __name__ == "__main__":
    main()
