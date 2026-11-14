# Uygulama Sorusu 9 (Orta-zor)
# Kullanıcıdan N sayısı alın. Tek bir döngüyle 1'den N'e kadar çift sayıların
# toplamını, tek sayıların toplamını ve farkını (çift - tek) hesaplayın.

n=int(input("Bir sayı giriniz: "))

cift_sayi_toplami=0
tek_sayi_toplami=0

for i in range(1,n+1):
    if i % 2 == 0:
        cift_sayi_toplami+=i
    else:
        tek_sayi_toplami+=i

fark=cift_sayi_toplami-tek_sayi_toplami

print("Çift sayıların toplamı:",cift_sayi_toplami)
print("Tek sayıların toplamı:",tek_sayi_toplami)
print("Fark:",fark)
