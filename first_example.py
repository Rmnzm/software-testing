# Команда запуска python -m pytest first_example.py -k "test_check_math"
# python - наш язык
# -m модуль запуска
# pytest - тестовый фреймворк
# first_example.py - файл для запуска
# -k ключ, для запуска конкретных тестов
# "test_check_math" - название теста (функции)


class TestExample:  # Класс как файл
    def test_check_math(self):  # Функция - тест. Проверка математики
        a = 6
        b = 9
        expected_some = 14  # ожидаемый результат
        # если результат не сходится, то выпадает ошибка из текста
        assert a + b == expected_some, f"some of variables a and b is not equal to {expected_some}"  # Проверка на булевые значения
