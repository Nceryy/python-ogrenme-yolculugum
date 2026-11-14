# Soru 3: Depo robotunun koridor secimi
# Agirlik 0'dan buyuk ve en fazla 50 kg olmali.
# A koridoru aciksa en fazla 20 kg olan paketleri tasiyabilir.
# B koridoru aciksa kirilabilir olmayan, gecerli agirliktaki paketleri tasiyabilir.
# Iki koridor da uygunsa A tercih edilir.
# Metin cevaplarinin evet/hayır seceneklerine uygun oldugu varsayilir.
# Ornek: 25, evet, evet, evet -> Tasima yapilamaz.
# Ornek: 15, hayır, evet, hayır -> B koridoru secildi.

paket_agirligi = float(input("Paketin ağırlığını giriniz: "))
a_koridoru = input("A koridoru açık mı? (evet/hayır): ")
b_koridoru = input("B koridoru açık mı? (evet/hayır): ")
paket_kirilma = input("Paket kırılabilir mi? (evet/hayır): ")

if paket_agirligi <= 0 or paket_agirligi > 50:
    print("Geçersiz ağırlık.")
elif a_koridoru == "evet" and paket_agirligi <= 20:
    print("A koridoru seçildi.")
elif b_koridoru == "evet" and paket_kirilma == "hayır":
    print("B koridoru seçildi.")
else:
    print("Taşıma yapılamaz.")
