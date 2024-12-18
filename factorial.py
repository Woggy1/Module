
def factorial(n):

    if not isinstance(n, int) or n < 0:
        raise ValueError("Число повинно бути невід'ємним цілим.")
    return 1 if n == 0 else n * factorial(n - 1)

if __name__ == "__main__":
    try:
        number = int(input("Введіть невід'ємне ціле число: "))
        print(f"Факторіал числа {number} дорівнює {factorial(number)}")
    except ValueError as e:
        print(f"Помилка: {e}")