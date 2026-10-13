"""Girilen sayının tam kare olup olmadığını kontrol eder."""

import math

number = int(input("Negatif olmayan bir tam sayı giriniz: "))

if number < 0:
    print("Negatif sayıların reel karekökü yoktur.")
else:
    root = math.isqrt(number)
    if root * root == number:
        print(f"{number} tam karedir; karekökü {root}.")
    else:
        print(f"{number} tam kare değildir; yaklaşık karekökü {math.sqrt(number):.2f}.")
