"""İki tam sayının EBOB ve EKOK değerlerini bulur."""

import math

number1 = int(input("Birinci tam sayıyı giriniz: "))
number2 = int(input("İkinci tam sayıyı giriniz: "))

if number1 == 0 and number2 == 0:
    print("İki sayı da sıfırken EBOB ve EKOK tanımlı değildir.")
else:
    ebob = math.gcd(number1, number2)
    ekok = abs(number1 * number2) // ebob
    print(f"EBOB({number1}, {number2}) = {ebob}")
    print(f"EKOK({number1}, {number2}) = {ekok}")
