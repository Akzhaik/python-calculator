def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Ошибка: деление на ноль"
    return a / b

def power(a, b):
    return a ** b

def get_number():
    while True:
        try:
            return float(input("Введите число: "))
        except ValueError:
            print("Ошибка! Введите число.")

def search_operation(history, operation):
    return [item for item in history
            if operation.lower() in item.lower()]

if __name__ == "__main__":
    print("=== КАЛЬКУЛЯТОР ===")
    a = get_number()
    b = get_number()

    print("Сложение:", add(a, b))
    print("Вычитание:", subtract(a, b))
    print("Умножение:", multiply(a, b))
    print("Деление:", divide(a, b))
    print("Степень:", power(a, b))