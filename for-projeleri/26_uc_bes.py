# Uygulama Sorusu 14 (Zorlayıcı)
# 1'den N'e kadar: hem 3'e hem 5'e bölünüyorsa "Üç-Beş", yalnızca 3'e "Üç",
# yalnızca 5'e "Beş", hiçbirine bölünmüyorsa sayının kendisini yazdırın.
# Sonda her birinden kaç tane yazıldığını gösterin.

n=int(input("Bir sayı giriniz: "))
uc_bes=0
uc=0
bes=0

for i in range(1,n+1):
    if i % 3 == 0 and i % 5 == 0:
        print("Üç-Beş")
        uc_bes+=1
    elif i % 3 == 0:
        print("Üç")
        uc+=1
    elif i % 5 == 0:
        print("Beş")
        bes+=1
    else:
        print(i)

print("Üç adedi:",uc)
print("Beş adedi,",bes)
print("Üç-Beş adedi:",uc_bes)
