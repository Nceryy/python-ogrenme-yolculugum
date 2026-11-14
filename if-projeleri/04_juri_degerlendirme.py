# Soru 4: Bilim yarismasinda juri degerlendirmesi
# Puanlar 0-100 arasinda olmali (sinirlar dahil).
# Puan farki 30'dan buyukse ucuncu juri gerekir.
# Fark en fazla 30 ise ortalamasi en az 85 olanlar finale kalir.
# Ortalamasi en az 75 olup ozgunluk belgesi olanlar da finale kalir.
# Finale kalamayanlardan ortalamasi en az 60 olanlar yedek listeye girer.
# Digerleri elenir. Belge cevabi evet/hayır olarak girilir.
# Ornek: 59, 59, evet -> Elendi.
# Ornek: 90, 60, evet -> Finale kaldi.

juri1 = int(input("1. jüri puanı: "))
juri2 = int(input("2. jüri puanı: "))
belge = input("Özgünlük belgesi var mı? (evet/hayır): ")

fark = abs(juri1 - juri2)
ortalama = (juri1 + juri2) / 2

if (juri1 < 0 or juri1 > 100) or (juri2 < 0 or juri2 > 100):
    print("Geçersiz puan.")
elif fark > 30:
    print("Üçüncü jüri gerekli.")
else:
    if ortalama >= 85 or (ortalama >= 75 and belge == "evet"):
        print("Finale kaldı.")
    elif ortalama >= 60:
        print("Yedek liste.")
    else:
        print("Elendi.")
