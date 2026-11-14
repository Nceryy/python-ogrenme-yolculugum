# Gerçek Hayat Problemi 4 - Haftalık Ders Çalışma Çizelgesi
# Hafta içi (1-5) her gün için çalışma saatini alın, hafta sonu (6-7) "dinlenme"
# yazdırın. Sonda toplam çalışma saatini ve günlük ortalamayı gösterin.

toplam=0
for i in range(1,6):
    calisma_saati=float(input(f"{i}. gün çalışma saati: "))

    toplam+=calisma_saati

for i in range(6,8):
    print(f"{i}. gün: Hafta sonu- dinlenme")
ortalama=toplam/5

print("Toplam çalışma:",toplam)
print("Günlük ortalama:",ortalama)
