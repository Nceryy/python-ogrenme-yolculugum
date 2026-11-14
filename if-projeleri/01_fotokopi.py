# Soru 1: Fotokopi ucreti
# Ilk 20 sayfanin her biri 2 TL, sonraki 30 sayfanin her biri 1.5 TL,
# 50'den sonraki sayfalarin her biri 1 TL'dir.
# Fiyatlar kademeli uygulanir. Sayfa sayisi pozitif tam sayi olmalidir.
# Ornek: 60 sayfa -> 20 * 2 + 30 * 1.5 + 10 * 1 = 95 TL.

sayfa = int(input("Sayfa sayısını giriniz: "))

if sayfa <= 0:
    print("Geçersiz sayfa sayısı.")
else:
    if sayfa <= 20:
        ucret = sayfa * 2
    elif sayfa <= 50:
        ucret = 20 * 2 + (sayfa - 20) * 1.5
    else:
        ucret = 20 * 2 + 30 * 1.5 + (sayfa - 50) * 1

    print("Toplam ücret:", ucret, "TL")
