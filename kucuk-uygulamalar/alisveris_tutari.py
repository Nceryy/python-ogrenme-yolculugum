"""Ürün fiyatlarını toplar; 500 TL ve üzeri için %10 indirim uygular."""

while True:
    urun_sayisi = int(input("Kaç ürün aldınız? "))
    if urun_sayisi > 0:
        break
    print("Lütfen sıfırdan büyük bir sayı giriniz.")

toplam = 0.0
for sira in range(1, urun_sayisi + 1):
    while True:
        fiyat = float(input(f"{sira}. ürünün fiyatı (TL): "))
        if fiyat > 0:
            break
        print("Fiyat sıfırdan büyük olmalıdır.")
    toplam += fiyat

if toplam >= 500:
    toplam *= 0.90
    print("%10 indirim uygulandı.")

print(f"Ödenecek tutar: {toplam:.2f} TL")
    
