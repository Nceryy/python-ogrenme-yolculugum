# Uygulama Sorusu 4 (Orta)
# Kullanıcıdan N sayısı alın. 1'den N'e kadar (N dahil) olan sayılardan
# 3'e tam bölünebilenlerin toplamını hesaplayıp yazdırın.

n=int(input("Bir sayı giriniz:"))
toplam=0
for i in range(1,n+1):
    if i % 3 ==0:
        toplam+=i

print(toplam)
