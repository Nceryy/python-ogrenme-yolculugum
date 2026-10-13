"""1 ile 50 arasında tutulan sayıyı beş geçerli tahminde bulmaya çalış."""

import random

gizli_sayi = random.randint(1, 50)
kalan_hak = 5

print("1 ile 50 arasında bir sayı tuttum. Beş tahmin hakkın var!")

while kalan_hak > 0:
    try:
        tahmin = int(input("Tahminin: "))
    except ValueError:
        print("Lütfen bir tam sayı gir.")
        continue

    if not 1 <= tahmin <= 50:
        print("Tahmin 1 ile 50 arasında olmalı.")
        continue

    kalan_hak -= 1
    if tahmin == gizli_sayi:
        puan = 100 - (4 - kalan_hak) * 15
        print(f"Bildin! Puanın: {puan}")
        break

    print("Daha büyük bir sayı dene." if tahmin < gizli_sayi else "Daha küçük bir sayı dene.")
    print(f"Kalan hak: {kalan_hak}")
else:
    print(f"Hakların bitti. Tuttuğum sayı {gizli_sayi} idi.")
        
