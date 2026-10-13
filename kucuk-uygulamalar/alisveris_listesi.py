# Alisveris listesi
# Bu program listeler, while, if/elif/else ve for konularini tekrar etmek icin.

urunler = []

while True:
    print("\n--- ALISVERIS LISTESI ---")
    print("1 - Urun ekle")
    print("2 - Urunleri goster")
    print("3 - Urun sil")
    print("4 - Cik")

    secim = input("Seciminiz (1-4): ")

    if secim == "1":
        urun = input("Eklenecek urun: ").strip()
        if urun == "":
            print("Bos bir urun ekleyemezsiniz.")
        else:
            urunler.append(urun)
            print(urun, "listeye eklendi.")

    elif secim == "2":
        if len(urunler) == 0:
            print("Liste bos.")
        else:
            print("Listenizdeki urunler:")
            for urun in urunler:
                print("-", urun)

    elif secim == "3":
        urun = input("Silinecek urun: ").strip()
        if urun in urunler:
            urunler.remove(urun)
            print(urun, "listeden silindi.")
        else:
            print("Bu urun listede yok.")

    elif secim == "4":
        print("Gorusuruz!")
        break

    else:
        print("Lutfen 1, 2, 3 veya 4 secin.")
