# Uygulama Sorusu 10 (Orta-zor)
# Kullanıcıdan pozitif bir tamsayı alın. Bütün bölenlerini yazdırın,
# kaç böleni olduğunu bulun ve sayının asal olup olmadığını söyleyin.

sayi=int(input("Bir sayı giriniz: "))
bolen_sayisi=0
for i in range(1,sayi+1):
    if sayi % i == 0:
        print(i)
        bolen_sayisi+=1

print("Bölen sayısı:",bolen_sayisi)

if bolen_sayisi >2:
    print("Asal sayı değildir.")
elif bolen_sayisi == 1:
    print("Asal sayı değildir.")
else:
    print("Asal sayıdır.")
