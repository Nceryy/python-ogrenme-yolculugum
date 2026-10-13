while True:
    sayi=int(input("1-10 arasında sayı giriniz (çıkmak için 0): "))

    if sayi == 0:
        break
    elif 1 <= sayi <= 10:
        for carpim in range(1,11):
            print(f"{sayi} x {carpim} = {sayi*carpim}")
    else:
        print("Lütfen 1 ile 10 arasında bir sayı giriniz")