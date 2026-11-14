# Gerçek Hayat Problemi 3 - Sınav Süresi Geri Sayacı
# Sınav süresi ve duyuru aralığını alın. Kalan süreyi geri sayarak yazdırın.
# Kalan süre 10 dakika veya azsa "Son dakikalar!" ekleyin, sonda "Sınav bitti." yazın.

sinav_suresi=int(input("Sınav süresini giriniz: "))
duyuru_araligi=int(input("Duyuru aralığını giriniz: "))
sinav_duyuru=int(sinav_suresi/duyuru_araligi)
for i in range(sinav_suresi,0,-duyuru_araligi):

    if i <= 10:
        print(i,"dakika kaldı - son dakikalar!")
    else:
        print(i,"dakika kaldı.")

print("Sınav bitti.")
