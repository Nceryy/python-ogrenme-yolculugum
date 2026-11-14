# Gerçek Hayat Problemi 2 - Artan Birikim Planı
# İlk ay birikimi, aylık artış ve ay sayısını alın. Her ay bir önceki aydan
# artış kadar fazla biriktiriliyor. Her ay biriktirilen miktarı ve toplamı yazdırın.

para=int(input("İlk ayın parasını giriniz: "))
aylik_artis=int(input("Aylık artış miktarını giriniz: "))
biriktirilecek_ay=int(input("Kaç ay biriktireceksiniz: "))
toplam=0

for i in range(1,biriktirilecek_ay+1):
    toplam+=para
    print(f"{i}. ay {para} biriktirildi,","toplam:",toplam)
    para+=aylik_artis
