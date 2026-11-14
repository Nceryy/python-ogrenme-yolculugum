# Uygulama Sorusu 7 (Orta)
# Kullanıcıdan başlangıç ve bitiş alın. Başlangıç küçükse artarak,
# büyükse azalarak sayıları yazdırın. İki uç değer de dahil olsun.

baslangic=int(input("Başlangıç sayısını giriniz: "))
bitis=int(input("Bitiş sayısını giriniz: "))

if baslangic < bitis:
    for i in range(baslangic,bitis+1):
        print(i)
else:
    for i in range(baslangic,bitis-1,-1):
        print(i)
