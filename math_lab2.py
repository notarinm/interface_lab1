import math

# Вариант 15
# f(x) = -∛(2 * (x - 1)^2 * (4 - x))
# Интервал [2; 4]
# Точность ε = 10^-3

a = 2.0
b = 4.0
eps = 1e-3


# Функция
def f(x):
    return -(2 * (x - 1) ** 2 * (4 - x)) ** (1 / 3)


# Коэффициент золотого сечения
phi = (math.sqrt(5) - 1) / 2


# Начальные точки
x1 = b - phi * (b - a)
x2 = a + phi * (b - a)

f1 = f(x1)
f2 = f(x2)

# Количество вычислений функции
function_calls = 2

# Номер итерации
iteration = 0

# Таблица итераций
iterations = []


# Метод золотого сечения
while (b - a) > eps:
    iteration += 1

    # Сохраняем данные текущей итерации
    iterations.append([
        iteration,
        a,
        b,
        x1,
        f1,
        x2,
        f2,
        b - a
    ])

    if f1 < f2:
        b = x2

        x2 = x1
        f2 = f1

        x1 = b - phi * (b - a)
        f1 = f(x1)

        function_calls += 1

    else:
        a = x1

        x1 = x2
        f1 = f2

        x2 = a + phi * (b - a)
        f2 = f(x2)

        function_calls += 1


# Найденная точка минимума
x_min = (a + b) / 2
f_min = f(x_min)


# Вывод результатов
print("=" * 115)
print("МЕТОД ЗОЛОТОГО СЕЧЕНИЯ")
print("Вариант 15")
print("f(x) = -(2*(x-1)^2*(4-x))^(1/3)")
print("Интервал: [2; 4]")
print(f"Точность: ε = {eps}")
print("=" * 115)

print(
    f"{'№':>3} "
    f"{'a':>10} "
    f"{'b':>10} "
    f"{'x1':>10} "
    f"{'f(x1)':>12} "
    f"{'x2':>10} "
    f"{'f(x2)':>12} "
    f"{'Длина':>12}"
)

print("-" * 115)


# Вывод таблицы
for row in iterations:
    print(
        f"{row[0]:>3} "
        f"{row[1]:>10.6f} "
        f"{row[2]:>10.6f} "
        f"{row[3]:>10.6f} "
        f"{row[4]:>12.8f} "
        f"{row[5]:>10.6f} "
        f"{row[6]:>12.8f} "
        f"{row[7]:>12.6f}"
    )


print("-" * 115)

print(f"Количество итераций: {iteration}")
print(f"Количество вычислений функции: {function_calls}")
print(f"Конечный интервал: [{a:.8f}; {b:.8f}]")
print(f"Длина конечного интервала: {b - a:.8f}")
print(f"x_min = {x_min:.8f}")
print(f"f(x_min) = {f_min:.8f}")
print(f"Коэффициент сокращения интервала: {phi:.8f}")