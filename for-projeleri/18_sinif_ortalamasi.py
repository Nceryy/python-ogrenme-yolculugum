# Uygulama Sorusu 6 (Orta)
# 5 öğrencinin notunu (küsuratlı olabilir) alıp sınıf ortalamasını hesaplayın.
# Ortalama 50 veya üzeriyse "Sınıf başarılı", değilse "Sınıf başarısız" yazın.

toplam=0
for i in range(1,6):
    notu=float(input(f"{i}. öğrencinin notunu giriniz: "))
    toplam+=notu

ortalama = toplam/5

print("Ortalama:",ortalama)

if ortalama >= 50:
    print("Sınıf başarılı.")
else:
    print("Sınıf başarısız.")
