# Soru 2: Turnuvada oyuncu eslestirme
# Puanlar 0-3000 arasinda (sinirlar dahil), bekleme sureleri negatif olmamali.
# Puan farki en fazla 200 ise eslestirme yapilir.
# Fark 200'den buyuk ve en fazla 500 ise iki oyuncu da en az 5 dakika beklemeli.
# Diger durumlarda eslestirme yapilamaz.
# Ornek: 1000, 1500, 5, 5 -> Eslestirme yapilabilir.
# Ornek: 1000, 1500, 5, 4 -> Eslestirme yapilamaz.

puan1 = int(input("1. oyuncunun puanı: "))
puan2 = int(input("2. oyuncunun puanı: "))
dakika1 = int(input("1. oyuncunun bekleme süresi: "))
dakika2 = int(input("2. oyuncunun bekleme süresi: "))

fark = abs(puan1 - puan2)

if (puan1 < 0 or puan1 > 3000 or
    puan2 < 0 or puan2 > 3000 or
    dakika1 < 0 or dakika2 < 0):
    print("Geçersiz bilgi.")
elif fark <= 200:
    print("Eşleştirme yapılabilir.")
elif fark <= 500 and dakika1 >= 5 and dakika2 >= 5:
    print("Eşleştirme yapılabilir.")
else:
    print("Eşleştirme yapılamaz.")
