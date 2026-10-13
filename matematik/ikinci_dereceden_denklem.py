"""İkinci dereceden bir denklemin reel köklerini hesaplar."""

import math

a = float(input("a değerini giriniz: "))
b = float(input("b değerini giriniz: "))
c = float(input("c değerini giriniz: "))

if a == 0:
    print("a sıfır olamaz; bu durumda denklem ikinci dereceden değildir.")
else:
    delta = b**2 - 4 * a * c
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"Delta: {delta:g}; kökler: {x1:g} ve {x2:g}")
    elif delta == 0:
        x = -b / (2 * a)
        print(f"Çift katlı kök: {x:g}")
    else:
        print("Denklemin reel kökü yoktur.")
