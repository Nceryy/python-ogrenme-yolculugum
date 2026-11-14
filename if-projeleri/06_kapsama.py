birinci_etkinlik_bas = int(input("1. etkinliğin başlangıcı: "))
birinci_etkinlik_son = int(input("1. etkinliğin bitişi: "))

ikinci_etkinlik_bas = int(input("2. etkinliğin başlangıcı: "))
ikinci_etkinlik_son = int(input("2. etkinliğin bitişi: "))

if (not (0 <= birinci_etkinlik_bas < birinci_etkinlik_son <= 24)
    or not (0 <= ikinci_etkinlik_bas < ikinci_etkinlik_son <= 24)):
    print("Geçersiz saat bilgisi.")

elif (birinci_etkinlik_son <= ikinci_etkinlik_bas
      or ikinci_etkinlik_son <= birinci_etkinlik_bas):
    print("İki etkinlik de yapılabilir.")

elif (birinci_etkinlik_bas == ikinci_etkinlik_bas
      and birinci_etkinlik_son == ikinci_etkinlik_son):
    print("Aynı zaman aralığı.")

elif ((birinci_etkinlik_bas <= ikinci_etkinlik_bas
       and birinci_etkinlik_son >= ikinci_etkinlik_son)
      or
      (ikinci_etkinlik_bas <= birinci_etkinlik_bas
       and ikinci_etkinlik_son >= birinci_etkinlik_son)):
    print("Biri diğerini kapsıyor.")

else:
    print("Kısmi çakışma.")