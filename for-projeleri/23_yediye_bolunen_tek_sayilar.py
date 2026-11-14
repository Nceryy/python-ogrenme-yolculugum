# Uygulama Sorusu 11 (Orta-zor)
# Başlangıç ve bitiş arasında (ikisi de dahil) 7'ye tam bölünen ama çift
# olmayan sayıları yazdırın; adedini, toplamını ve ortalamasını bulun.
# Hiç yoksa "Koşulu sağlayan sayı bulunamadı" yazın.

baslangic=int(input("Başlangıç sayısını giriniz: "))
bitis=int(input("Bitiş sayısını giriniz: "))
adet=0
toplam=0
for i in range(baslangic,bitis+1):
    if i % 7 == 0 and i % 2 == 1:
        print(i)
        adet+=1
        toplam+=i

if adet == 0:
    print("Koşulu sağlayan sayı bulunamadı.")
else:
    ortalama=toplam/adet
    print("Adet:",adet)
    print("Toplam:",toplam)
    print("Ortalama:",ortalama)
