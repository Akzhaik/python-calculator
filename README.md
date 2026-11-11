# Python Calculator

## Описание

Python Calculator — консольная программа для выполнения математических вычислений. Программа позволяет выполнять основные арифметические операции.

## Возможности

- Сложение чисел.
- Вычитание чисел.
- Умножение чисел.
- Деление чисел.
- Возведение в степень.
- Вычисление квадратного корня.
- Проверка корректности вводимых данных.

## Технологии

| Технология | Назначение |
|---|---|
| Python | Язык программирования |
| Git | Контроль версий |
| GitHub | Хранение проекта |
| pytest | Тестирование программы |

## Структура проекта

```text
python-calculator/
├── src/
│   └── main.py
├── tests/
│   └── test_main.py
├── README.md
├── requirements.txt
└── .gitignore
```

## Требования

- Python 3.10 или выше.
- Git.
- Операционная система Windows, Linux или macOS.

## Установка

1. Клонируйте репозиторий:

```bash
git clone https://github.com/Akzhaik/python-calculator.git
```

2. Перейдите в папку проекта:

```bash
cd python-calculator
```

3. Установите зависимости:

```bash
pip install -r requirements.txt
```

## Запуск

```bash
python src/main.py
```

## Использование

Пример выполнения операций:

```python
from src.main import add, subtract, multiply, divide

print(add(10, 5))
print(subtract(10, 5))
print(multiply(10, 5))
print(divide(10, 5))
```

Результат:

```text
15
5
50
2.0
```

## Зависимости

Список необходимых библиотек находится в файле [requirements.txt](requirements.txt).

## Автор

Таласпаева Акжаик Сиюндыковна