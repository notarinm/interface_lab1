import re
from datetime import datetime


# Проверка паспорта
def input_passport():
    while True:
        passport = input("Введите паспорт (12 34-567890): ")

        if re.fullmatch(r"\d{2} \d{2}-\d{6}", passport):
            return passport
        print("Ошибка! Неверный формат паспорта. Попробуйте ещё раз.")


# Проверка имени
def input_name():
    while True:
        name = input("Введите ФИО: ")

        if re.fullmatch(r"[А-Яа-яЁёA-Za-z ]+", name):
            return name
        print("Ошибка! Имя должно содержать только буквы и пробелы.")


# Проверка даты рождения
def input_birth_date():
    while True:
        date = input("Введите дату рождения (2006-03-02): ")

        # Проверяем формат даты
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", date):
            print("Ошибка! Дата должна быть в формате ГГГГ-ММ-ДД.")
            continue

        # Проверяем, существует ли такая дата
        try:
            datetime.strptime(date, "%Y-%m-%d")
            return date
        except ValueError:
            print("Ошибка! Такой даты не существует. Попробуйте ещё раз.")


# Проверка телефона
def input_phone():
    while True:
        phone = input("Введите телефон (+7(999) 123-45-67): ")

        pattern1 = r"\+\d\(\d{3}\) \d{3}-\d{2}-\d{2}"
        pattern2 = r"\d\(\d{3}\) \d{3}-\d{4}"

        if re.fullmatch(pattern1, phone) or re.fullmatch(pattern2, phone):
            return phone
        print("Ошибка! Неверный формат телефона.")


# Проверка температуры
def input_temperature():
    while True:
        temperature = input("Введите температуру (36.60): ")

        if re.fullmatch(r"\d{2}\.\d{2}", temperature):
            return float(temperature)
        print("Ошибка! Температура должна быть в формате XX.XX.")


# Основная программа
print("Введите информацию о пациенте")
print()

passport = input_passport()
name = input_name()
birth_date = input_birth_date()
phone = input_phone()
temperature = input_temperature()

print()
print("Информация о пациенте:")
print("Паспорт:", passport)
print("ФИО:", name)
print("Дата рождения:", birth_date)
print("Телефон:", phone)
print("Температура:", temperature)