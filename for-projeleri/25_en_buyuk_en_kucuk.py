# Uygulama Sorusu 13 (Zorlayıcı)
# Kullanıcı N tane tamsayı girsin. Liste, max() ve min() kullanmadan
# en büyüğü, en küçüğü, toplamı ve ortalamayı bulun.

girilecek_sayi=int(input("Kaç sayı gireceksiniz: "))
en_buyuk_deger=0
en_kucuk_deger=0
toplam=0

for i in range(1,girilecek_sayi+1):
    n=int(input(f"{i}. sayıyı giriniz: "))
    toplam += n

    if i == 1:
        en_buyuk_deger=n
        en_kucuk_deger=n

    else:
        if n > en_buyuk_deger:
            en_buyuk_deger = n
        elif n < en_kucuk_deger:
            en_kucuk_deger = n

ortalama=toplam/girilecek_sayi
print("En büyük:",en_buyuk_deger)
print("En küçük:",en_kucuk_deger)
print("Toplam:",toplam)
print("Ortalama:",ortalama)
