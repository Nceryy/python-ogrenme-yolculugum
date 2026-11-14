# Uygulama Sorusu 5 (Orta)
# Kullanıcıdan N sayısı alın. 1'den N'e kadar her sayının tek mi çift mi
# olduğunu yazdırın. Sonda kaç çift ve kaç tek sayı olduğunu gösterin.

n=int(input("Bir sayı giriniz: "))

cift_sayi_adedi = 0
tek_sayi_adedi = 0

for i in range(1,n+1):
    if i % 2 == 1:
        print(i,"tek")
        tek_sayi_adedi+=1
    else:
        print(i,"çift")
        cift_sayi_adedi+=1

print("Çift sayı adedi:",cift_sayi_adedi)
print("Tek sayı adedi:",tek_sayi_adedi)
