"""
## Автомобиль

Описать класс Car
``` python
class Car:
  ...

car1 = Car()
```

а) У машины должны быть атрибуты
* "сколько бензина в баке" (gas)
* "вместимость бака" - сколько максимум влезаем бензина (capacity)
* "расход топлива на км" (gas_per_km)

б) метод "залить столько-то литров в бак"

``` python
car1.fill(5)  # залили 5 литров
```

должна учитываться вместительность бака
если пытаемся залить больше, чем вмещается, то заполняется полностью + print'ом выводится сообщение о лишних литрах

в) метод "проехать сколько-то км"

``` python
car1.ride(50)  # едем 50 км (если хватит топлива)
```

выведет сообщение "проехали ... километров"
в результате поездки потратится бензин
Машина едет пока хватает бензина

г) добавить атрибут с пробегом, который увеличивается в результате ride
"""

class Car:
    def __init__(self, gas, capacity, gas_per_km):
        self.gas = gas
        self.capacity = capacity
        self.gas_per_km = gas_per_km
        self.mileage = 0


    def fill(self, litres):
        if (self.gas + litres) <= self.capacity:
            self.gas += litres

        else:
            print(f'Бак полностью заполнен, не вместилось {self.gas + litres - self.capacity} л.')
            self.gas = self.capacity


    def ride(self, distance):
        if self.gas_per_km * distance <= self.gas:
            self.gas -= self.gas_per_km * distance
            self.mileage += distance

        else:
            mileage = int(self.gas / self.gas_per_km)
            self.mileage += mileage
            self.gas = 0
            print(f'Не хватило топлива, проехали {mileage, 2 } км.')



