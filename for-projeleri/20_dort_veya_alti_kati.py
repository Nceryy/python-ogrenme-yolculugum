# Uygulama Sorusu 8 (Orta)
# Kullanıcıdan N sayısı alın. 1'den N'e kadar 4'e veya 6'ya tam bölünebilen
# sayıları yazdırın ve kaç tane olduklarını bulun.

n=int(input("Bir sayı giriniz: "))

adet=0

for i in range(1,n+1):
    if i % 4 == 0 or i % 6 == 0:
        print(i)
        adet+=1
print("Adet:",adet)
