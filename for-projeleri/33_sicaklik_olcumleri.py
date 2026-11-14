# Gerçek Hayat Problemi 6 - Hava İstasyonu Sıcaklık Ölçümleri
# Ölçüm sayısını ve her ölçümün sıcaklığını alın. En yüksek sıcaklığı ve hangi
# ölçümde olduğunu, ortalama sıcaklığı ve donma (0 veya altı) ölçümü sayısını yazdırın.

olcum_sayisi=int(input("Ölçüm sayısı: "))

toplam=0
donma_olcumu=0

for i in range(1,olcum_sayisi+1):
    olcum_sicakligi=float(input(f"{i}. ölçüm: "))

    if i == 1:
        en_buyuk_deger = olcum_sicakligi
        olcum = i

    if olcum_sicakligi > en_buyuk_deger:
        en_buyuk_deger = olcum_sicakligi
        olcum = i

    if olcum_sicakligi<= 0:
        donma_olcumu+=1

    toplam += olcum_sicakligi

ortalama=toplam/olcum_sayisi

print("En yüksek sıcaklık: ",en_buyuk_deger,"(",f"{olcum}. ölçüm",")")
print("Ortalama sıcaklık: ",ortalama)
print("Donma ölçümü sayısı: ",donma_olcumu)
