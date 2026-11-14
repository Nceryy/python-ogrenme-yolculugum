#ATM girilecek parayı en düşük adette verecek. Volkan hocanın güzel soru dediği soru! 
para=int(input("Çekmek istediğiniz tutarı giriniz: "))

if para>=200:
    ikiyuztl=para//200
    para-=(ikiyuztl*200)
    yuztl=para//100
    para-=(yuztl*100)
    ellitl=para//50
    para-=(ellitl*50)
    yirmitl=para//20
    para-=(yirmitl*20)
    ontl=para//10
    para-=(ontl*10)
    bestl=para//5
    para-=(bestl*5)
    birtl=para//1

    print("200 TL'LİK banknot:",ikiyuztl)
    print("100 TL'LİK banknot:",yuztl)
    print("50 TL'LİK banknot:",ellitl)
    print("20 TL'LİK banknot:",yirmitl)
    print("10 TL'LİK banknot:",ontl)
    print("5 TL'LİK banknot:",bestl)
    print("1 TL'LİK banknot:",birtl)

elif para>=100:
    yuztl=para//100
    para-=(yuztl*100)
    ellitl=para//50
    para-=(ellitl*50)
    yirmitl=para//20
    para-=(yirmitl*20)
    ontl=para//10
    para-=(ontl*10)
    bestl=para//5
    para-=bestl*5
    birtl=para//1

    print("100 TL'LİK banknot:",yuztl)
    print("50 TL'LİK banknot:",ellitl)
    print("20 TL'LİK banknot:",yirmitl)
    print("10 TL'LİK banknot:",ontl)
    print("5 TL'LİK banknot:",bestl)
    print("1 TL'LİK banknot:",birtl)

else:
    print("Çekilebilecek minimum tutar 100 TL'dir.")

