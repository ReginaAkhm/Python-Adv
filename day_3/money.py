import requests
import json


class Money:
    def __init__(self, ruble: int, penny: int):
        self.ruble = ruble
        self.penny = penny

    # преобразовывание к минимальному количеству копеек
    def __str__(self):
        temp = self.penny // 100
        self.ruble += temp
        self.penny -= temp * 100
        return f'{self.ruble}руб. {self.penny}коп.'

    # сложение
    def __add__(self, other):
        new_ruble = self.ruble + other.ruble
        new_penny = self.penny + other.penny
        return Money(new_ruble, new_penny)

    # вычитание
    def __sub__(self, other):
        new_ruble = self.ruble - other.ruble
        new_penny = self.penny - other.penny
        return Money(new_ruble, new_penny)

    # умножение на константу
    def __mul__(self, other):
        new_ruble = self.ruble * other
        new_penny = self.penny * other
        return Money(new_ruble, new_penny)

    def __rmul__(self, other):
        new_ruble = self.ruble * other
        new_penny = self.penny * other
        return Money(new_ruble, new_penny)

    # сравнение
    def __gt__(self, other):
        return self.penny + self.ruble * 100 > other.penny + other.ruble * 100

    def __lt__(self, other):
        return self.penny + self.ruble * 100 < other.penny + other.ruble * 100

    def __eq__(self, other):
        return self.penny + self.ruble * 100 == other.penny + other.ruble * 100

    def __ne__(self, other):
        return self.penny + self.ruble * 100 != other.penny + other.ruble * 100

    # нахождение процента от числа
    def __mod__(self, other):
        new_ruble = 0
        new_penny = round((self.penny + self.ruble * 100) / 100 * 21)
        return Money(new_ruble, new_penny)

    # конвертирование
    def convert(self, valute: str):
        url = 'https://www.cbr-xml-daily.ru/daily_json.js'
        response = requests.get(url)
        data_dict = json.loads(response.text)
        value = data_dict['Valute'][valute]['Value']
        current = round((self.ruble + self.penny / 100) * value, 2)
        print(f"~{current} {valute}")


m1 = Money(20, 60)
m2 = Money(1, 160)
print(m1)
print(m2)
m3 = m1 + m2
print(m3)
m4 = m3 * 3
print(m4)
m5 = 3 * m3
print(m5)
print(m1 > m2)
print(m1.ruble)
print(m1 % 21)
m1.convert("USD")

"""
class Money

Напишите класс для работы с денежными суммами.

Реализовать:
*   сложение
*   вычитание
*   умножение на целое число
*   сравнение (больше, меньше, равно, не равно)

денежной суммы. 
При всех операциях, сумма должна преобразовываться к сумме с минимальным количеством копеек.

Примеры:
# Создаем сумму из 20 рублей и 120 копеек
money_sum1 = Money(20, 120)
# Выводим сумму, с учетом минимального кол-ва копеек
print(money_sum1) # 21руб 20коп


# Создаем две денежные суммы
money_sum1 = Money(20, 60)
money_sum2 = Money(10, 45)

# Складываем суммы
money_result = money_sum1 + money_sum2
print(money_result)  # 31руб 5коп



Примечание: список всех методов для перегрузки операций: (https://pythonworld.ru/osnovy/peregruzka-operatorov.html).


#### Доп.задание

Добавьте операцию - вычисление процента от суммы.

Пример:

# Создаем две денежные суммы
money_sum1 = Money(20, 60)

# Находим 21% от суммы
percent_sum = money_sum1 % 21

print(percent_sum)  # 4руб 33коп

Пояснение: % (процет от суммы) - должна являться новая денежная сумма. После вычисления процента, используем
округление (функция round())


### Конвертация валют

Доработайте класс Money, добавив ему метод .convert(), для конвертации суммы в рублях в евро и доллары.
Актуальные значения можно взять, сделав запрос на: https://www.cbr-xml-daily.ru/daily_json.js

#### Отправка запроса на url-адрес

pip install requests
import requests

url = 'https://www.cbr-xml-daily.ru/daily_json.js'
response = requests.get(url)

, где url - адрес сайта, на который отправляете запрос.

В переменную response получите ответ сайта.

Для преобразования ответа из json-формата используйте функцию:

import json
data_dict = json.loads(response.text)

Модуля json

print(data_dict['Valute']['EUR']['Value'])
"""
