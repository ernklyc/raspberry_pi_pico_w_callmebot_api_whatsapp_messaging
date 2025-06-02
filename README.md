# Raspberry Pi Pico W ile CallMeBot API Kullanarak WhatsApp Mesajlaşma

## Proje Hakkında

Bu proje, Raspberry Pi Pico W mikrodenetleyici kartını kullanarak CallMeBot API aracılığıyla WhatsApp mesajları göndermek için geliştirilmiş MicroPython script'lerini içerir. Proje, farklı ihtiyaçlara yönelik üç ayrı versiyon sunmaktadır:

* **v1.py**: Basit, tek seferlik mesaj gönderimi için.
* **v2.py**: Pico W üzerinde bir web sunucusu kurarak web arayüzünden mesaj gönderme (temel arayüz).
* **v3.py**: Pico W üzerinde bir web sunucusu kurarak web arayüzünden mesaj gönderme (gelişmiş arayüz ve özellikler).

## Özellikler

* **Wi-Fi Bağlantısı**: Tüm script'ler Raspberry Pi Pico W'nin Wi-Fi üzerinden internete bağlanmasını sağlar.
* **CallMeBot API Entegrasyonu**: WhatsApp mesajlarını göndermek için CallMeBot API'sini kullanır.
* **v1.py - Basit Mesaj Gönderimi**:
    * Önceden tanımlanmış bir telefon numarasına, yine önceden tanımlanmış bir mesajı gönderir.
    * Wi-Fi bağlantısını başlatır ve mesajı gönderir.
* **v2.py - Web Sunucusu ile Mesaj Gönderimi (Temel)**:
    * Pico W üzerinde bir HTTP web sunucusu başlatır.
    * Kullanıcıların bir web tarayıcısı üzerinden Pico W'ye bağlanarak mesaj içeriğini girmesini ve göndermesini sağlar.
    * Basit bir HTML arayüzü sunar.
    * Gönderilen mesajlardaki bazı Türkçe karakterleri ve boşlukları URL uyumlu hale getirir.
* **v3.py - Web Sunucusu ile Mesaj Gönderimi (Gelişmiş)**:
    * v2.py'ye benzer şekilde Pico W üzerinde bir HTTP web sunucusu başlatır.
    * Daha modern ve kullanıcı dostu bir HTML arayüzü sunar.
    * Mesaj gönderildikten sonra kullanıcıyı bilgilendiren bir durum mesajı gösterir ve sayfayı otomatik olarak yeniler.
    * Gönderilen mesajlardaki bazı Türkçe karakterleri ve boşlukları URL uyumlu hale getirir.

## Gereksinimler

* Raspberry Pi Pico W
* Bilgisayarınızda MicroPython ile uyumlu bir IDE (örn: Thonny)
* Aktif bir internet bağlantısı olan Wi-Fi ağı (SSID ve şifresi)
* **CallMeBot API Anahtarı**:
    * [CallMeBot web sitesini](https://www.callmebot.com/blog/free-api-whatsapp-messages/) ziyaret edin.
    * "WhatsApp Messages" API'si için adımları takip ederek telefon numaranızı kaydedin ve API anahtarınızı alın. Bu anahtar, mesaj gönderebilmeniz için gereklidir.

## Kurulum

1.  **MicroPython Yükleme**: Raspberry Pi Pico W'nize güncel MicroPython firmware'ini yüklediğinizden emin olun.
2.  **Dosyaların Yüklenmesi**:
    * Bu repodaki `v1.py`, `v2.py` veya `v3.py` dosyalarından kullanmak istediğinizi Pico W'nizin dosya sistemine yükleyin (örneğin, Thonny IDE kullanarak `main.py` olarak kaydedebilir veya farklı bir isimle kaydedip manuel çalıştırabilirsiniz).
3.  **Kimlik Bilgilerinin Düzenlenmesi**:
    * Pico W'ye yüklediğiniz Python dosyasını açın.
    * Aşağıdaki değişkenleri kendi bilgilerinizle güncelleyin:

        ```python
        # Örnek (her script dosyasının başında bulunur)
        ssid = 'SIZIN_WIFI_ADINIZ'  # Wi-Fi ağınızın adı (SSID).
        password = 'SIZIN_WIFI_SIFRENIZ'  # Wi-Fi şifreniz.

        phone_number = 'ULKE_KODU_ILE_TELEFON_NUMARANIZ'  # WhatsApp mesajının gönderileceği telefon numarası. Örn: +905xxxxxxxxx
        # ÖNEMLİ: CallMeBot, telefon numarasının uluslararası formatta (+ ile başlayarak) girilmesini gerektirir.

        api_key = 'CALLMEBOT_API_ANAHTARINIZ'  # CallMeBot API için kimlik doğrulama anahtarınız.
        ```
    * Dosyayı kaydedin.

## Kullanım

### v1.py

1.  `v1.py` dosyasını gerekli kimlik bilgileriyle düzenleyip Pico W'nize yükleyin.
2.  Script'i çalıştırın (Thonny'de F5 veya "Run current script").
3.  Script, Wi-Fi'ye bağlanacak ve `message` değişkeninde tanımlı olan mesajı belirttiğiniz `phone_number`'a gönderecektir.
4.  İşlem durumu Thonny'nin Shell/REPL penceresinde görüntülenecektir.

    ```python
    # v1.py içinde gönderilecek mesajı buradan değiştirebilirsiniz:
    message = 'Eren%20KALAYCI%20%2f%20212701035%20%2F%20Mikro%20Denetleyiciler' # Gönderilecek mesaj (URL-encoded formatında yazılmıştır).
    ```

### v2.py / v3.py

1.  Kullanmak istediğiniz `v2.py` veya `v3.py` dosyasını gerekli kimlik bilgileriyle düzenleyip Pico W'nize yükleyin.
2.  Script'i çalıştırın.
3.  Script Wi-Fi ağına bağlandıktan sonra, Pico W'nin aldığı IP adresi Thonny'nin Shell/REPL penceresinde yazdırılacaktır. Örnek: `IP: 192.168.1.100` veya `Web arayüzüne gitmek için: http://192.168.1.100`.
4.  Aynı Wi-Fi ağına bağlı bir bilgisayar veya telefondan bir web tarayıcı açın.
5.  Tarayıcının adres çubuğuna Pico W'nin IP adresini yazın (örn: `http://192.168.1.100`) ve Enter'a basın.
6.  Karşınıza gelen web sayfasındaki metin kutusuna göndermek istediğiniz mesajı yazın ve "Gönder" (veya benzeri) butonuna tıklayın.
    * **v2.py**: Basit bir form ve gönderim sonrası "Mesaj Gönderildi!" mesajı içeren bir sayfaya yönlendirme yapar (başarılı gönderim varsayılır).
    * **v3.py**: Daha stil sahibi bir form sunar ve "Mesaj Gönderiliyor..." bildirimi gösterdikten sonra ana sayfaya geri döner.

## Dosya Açıklamaları

* **`v1.py`**:
    * Wi-Fi'ye bağlanır ve önceden tanımlanmış bir WhatsApp mesajını CallMeBot API'si üzerinden gönderir.
* **`v2.py`**:
    * Pico W üzerinde bir web sunucusu oluşturur.
    * Kullanıcıların web arayüzü üzerinden mesaj girmesine ve bu mesajları WhatsApp ile göndermesine olanak tanır.
    * Temel bir HTML arayüzü ve Türkçe karakterler için basit bir dönüştürme işlevi içerir.
* **`v3.py`**:
    * `v2.py`'nin geliştirilmiş halidir.
    * Daha gelişmiş ve kullanıcı dostu bir HTML/CSS arayüzü sunar.
    * Mesaj gönderme durumu hakkında geri bildirim sağlar ve Türkçe karakterleri URL uyumlu hale getirmek için düzenlemeler içerir.

## Önemli Notlar

* **CallMeBot API Limitleri**: CallMeBot API'sinin ücretsiz kullanımı belirli limitlere (örneğin, günlük mesaj sayısı) tabi olabilir. Servisin güncel koşullarını kontrol edin.
* **URL Encoding**: Mesaj içeriğinde özel karakterler veya emojiler kullanıyorsanız, bunların doğru bir şekilde URL encode edilmesi gerekebilir. `v2.py` ve `v3.py` scriptleri boşlukları `%20` ile ve bazı temel Türkçe karakterleri Latin alfabesindeki karşılıkları ile değiştirir. Daha karmaşık karakterler için ek düzenlemeler gerekebilir.
* **Hata Yönetimi**:
    * `v1.py` ve `v3.py` temel hata mesajlarını konsola yazar.
    * `v2.py`'deki web sunucusu, mesaj gönderme işlemi başarısız olsa bile kullanıcıya genellikle "Mesaj Gönderildi!" sayfasını gösterir. Gerçek gönderim durumunu doğrulamak için CallMeBot hesabınızı veya alıcı telefonu kontrol edin.
* **Güvenlik**: Bu script'ler Wi-Fi şifrenizi ve API anahtarınızı doğrudan kod içinde saklar. Pico W'nizin fiziksel ve ağ güvenliğine dikkat edin.

---
