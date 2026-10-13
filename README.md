# 🐍 Python Öğrenme Yolculuğum

Python öğrenirken yazdığım küçük uygulamalar, oyunlar ve matematik alıştırmaları. Bu depo, öğrendiklerimi düzenli biçimde bir araya getirmek ve ilerlememi görmek için hazırlandı.

> **Seviye:** Başlangıç · **Dil:** Python 3 · **Ek paket:** Yok

## 📂 Projeler

### 🧮 Matematik ve algoritmalar

| Dosya | Ne yapar? | Çalışılan konu |
| --- | --- | --- |
| [Çarpım tablosu](matematik/carpim_tablosu.py) | Seçilen sayının 1–10 arasındaki çarpımlarını gösterir. | Döngüler |
| [İkinci dereceden denklem](matematik/ikinci_dereceden_denklem.py) | Diskriminantı hesaplayıp reel kökleri bulur. | Koşullar, matematik |
| [EBOB ve EKOK](matematik/ebob_ekok.py) | İki tam sayının ortak bölen ve kat değerlerini gösterir. | `math` modülü |
| [Fibonacci dizisi](matematik/fibonacci.py) | İstenen uzunlukta Fibonacci dizisi üretir. | Listeler, döngüler |
| [Asal sayı kontrolü](matematik/asal_sayi_kontrolu.py) | Girilen sayının asal olup olmadığını söyler. | Bölünebilme, koşullar |
| [Asal sayıları listele](matematik/asal_sayilari_listele.py) | Girilen sayıya kadar olan asal sayıları bulur. | İç içe döngüler |
| [Karekök kontrolü](matematik/karekok_kontrolu.py) | Bir sayının tam kare olup olmadığını kontrol eder. | `math` modülü |

### 🛒 Küçük uygulamalar

| Dosya | Ne yapar? | Çalışılan konu |
| --- | --- | --- |
| [Alışveriş listesi](kucuk-uygulamalar/alisveris_listesi.py) | Ürün ekleme, görüntüleme ve silme işlemleri yapar. | Listeler, menüler |
| [Alışveriş tutarı](kucuk-uygulamalar/alisveris_tutari.py) | Ürün fiyatlarını toplar; 500 TL ve üzeri için %10 indirim uygular. | Giriş doğrulama, hesaplama |

### 🎮 Oyunlar

| Dosya | Ne yapar? | Çalışılan konu |
| --- | --- | --- |
| [Sayı tahmin oyunu](oyunlar/sayi_tahmin_oyunu.py) | Beş hak içinde 1–50 arasındaki gizli sayıyı bulmaya çalışırsın. | Rastgele sayılar, döngüler |

## 🚀 Nasıl çalıştırılır?

İlk kez bir Python projesi çalıştırıyorsan aşağıdaki adımları izleyebilirsin. Bu örnekler **Windows** içindir; macOS ve Linux'ta komutların başındaki `python` yerine `python3` kullanabilirsin.

### 1. Python'u kur

1. [Python'un resmî indirme sayfasını](https://www.python.org/downloads/) aç ve işletim sistemine uygun Python 3 kurulumunu yap. Windows için sunulan **Python install manager** seçeneğini kullanabilirsin.
2. Kurulum bittikten sonra açık terminal pencerelerini kapatıp **PowerShell** veya **Terminal** uygulamasını yeniden aç.
3. Kurulumu kontrol etmek için şu komutu yaz ve **Enter** tuşuna bas:

   ```powershell
   python --version
   ```

   `Python 3.x.x` benzeri bir sürüm görmelisin. Komut bulunamazsa `py --version` komutunu dene. Gerekirse [resmî Windows kurulum rehberine](https://docs.python.org/3/using/windows.html) bakabilirsin.

> Bu projeler yalnızca Python'un kendi modüllerini kullanır. Ek paket yüklemene veya `pip install` komutu çalıştırmana gerek yoktur.

### 2. Projeyi bilgisayarına indir

1. [Deponun ana sayfasında](https://github.com/Nceryy/python-ogrenme-yolculugum) yeşil **Code** düğmesine tıkla.
2. **Download ZIP** seçeneğini seç.
3. İndirilen ZIP dosyasına sağ tıklayıp **Tümünü ayıkla** seçeneğiyle dosyaları bir klasöre çıkar.
4. Çıkardığın klasörün içindeki `python-ogrenme-yolculugum-main` klasörünü aç. Burada `README.md`, `matematik`, `kucuk-uygulamalar` ve `oyunlar` birlikte görünmeli.

### 3. Terminali proje klasöründe aç

Windows Dosya Gezgini'nde bu klasör açıkken üstteki **adres çubuğuna** tıkla, `powershell` yaz ve **Enter** tuşuna bas. Böylece terminal doğrudan proje klasöründe açılır.

Doğru yerde olduğunu kontrol etmek için `dir` yazabilirsin. Listede üç proje klasörünü ve `README.md` dosyasını görmelisin.

### 4. İlk programını çalıştır

Örneğin sayı tahmin oyununu başlatmak için terminale şunu yaz:

```powershell
python oyunlar/sayi_tahmin_oyunu.py
```

- Program bir tahmin istediğinde **1 ile 50 arasında bir tam sayı** yazıp **Enter** tuşuna bas.
- Ekrandaki yönlendirmeleri takip et; gizli sayıyı bulmak için beş hakkın var.
- Program bitince yeniden oynamak için aynı komutu tekrar çalıştır.
- Bir programı bitmeden durdurmak istersen **Ctrl + C** tuşlarına bas.

Windows'ta yalnızca `py` komutu çalışıyorsa aynı örneği şöyle başlat:

```powershell
py oyunlar/sayi_tahmin_oyunu.py
```

### 📋 Diğer programları çalıştırma

Aşağıdaki komutlardan istediğin **birini** proje klasöründe açık olan terminale yaz. Her dosya bağımsız çalışır.

| Program | Çalıştırma komutu |
| --- | --- |
| Çarpım tablosu | `python matematik/carpim_tablosu.py` |
| İkinci dereceden denklem | `python matematik/ikinci_dereceden_denklem.py` |
| EBOB ve EKOK | `python matematik/ebob_ekok.py` |
| Fibonacci dizisi | `python matematik/fibonacci.py` |
| Asal sayı kontrolü | `python matematik/asal_sayi_kontrolu.py` |
| Asal sayıları listele | `python matematik/asal_sayilari_listele.py` |
| Karekök kontrolü | `python matematik/karekok_kontrolu.py` |
| Alışveriş listesi | `python kucuk-uygulamalar/alisveris_listesi.py` |
| Alışveriş tutarı | `python kucuk-uygulamalar/alisveris_tutari.py` |

**Küçük bir deneme:** Fibonacci programını başlatıp kaç terim istediği sorulduğunda `7` yaz. Ekranda `[0, 1, 1, 2, 3, 5, 8]` dizisini görmelisin.

> **Giriş ipuçları:** Tam sayı isteyen sorularda `7` gibi değerler kullan. Ondalıklı değer kabul eden sorularda virgül yerine nokta yaz: `19.90`. Alışveriş listesi yalnızca program açıkken tutulur; programı kapatınca silinir.

### 🛠️ Sık karşılaşılan sorunlar

| Sorun | Ne yapabilirsin? |
| --- | --- |
| `python` komutu bulunamıyor veya Microsoft Store açılıyor. | Önce `py --version` komutunu dene. Çalışıyorsa komutlarda `python` yerine `py` kullan. İkisi de çalışmıyorsa Python kurulumunu kontrol edip terminali yeniden aç. |
| `can't open file` veya `No such file or directory` hatası çıkıyor. | Terminalin proje ana klasöründe olduğundan emin ol. `dir` ile klasörleri kontrol et ve komuttaki dosya adını tablodaki gibi yaz. |
| Terminalde `>>>` işareti görünüyor. | Python'un etkileşimli ekranındasın. `exit()` yazıp Enter'a bas; çalıştırma komutunu ardından normal terminale yaz. |
| `ValueError` hatası çıkıyor. | Sayı beklenen yere metin veya uygun olmayan bir değer girilmiş olabilir. Programı yeniden başlat; tam sayı isteniyorsa tam sayı, ondalıklı sayı isteniyorsa noktalı değer gir. |
| Dosyaya çift tıklayınca pencere hemen kapanıyor. | Dosyayı yukarıdaki gibi terminalden çalıştır. Böylece sonuçlar ve olası hata mesajları ekranda kalır. |

## 🌱 Bu depoda neler öğreniyorum?

- Değişkenler, koşullar ve döngüler
- Listeler ve kullanıcıdan veri alma
- Basit algoritmalar ve hata durumlarını düşünme
- Kodları okunabilir klasörler ve açıklamalarla paylaşma

Bu projeler öğrenme amaçlıdır. Geliştirdikçe yeni örnekler ve iyileştirmeler ekleyeceğim.
