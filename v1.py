import network  # Wi-Fi bağlantısını yönetmek için kullanılan kütüphane.
import requests  # HTTP isteklerini yapmak için kullanılan kütüphane.
from time import sleep  # Kod içinde bekleme işlemleri için kullanılan kütüphane.

# Wi-Fi giriş bilgileri
ssid = 'ernklyc'  # Bağlanılacak Wi-Fi ağı adı (SSID).
password = '49200156'  # Wi-Fi şifresi.

# Telefon numarası (uluslararası formatta)
phone_number = '*********'  # WhatsApp mesajının gönderileceği telefon numarası.

# CallMeBot API anahtarı
api_key = '******'  # CallMeBot API için kimlik doğrulama anahtarı.

# Wi-Fi bağlantısını başlatma fonksiyonu
def init_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)  # Wi-Fi arayüzünü başlatır.
    wlan.active(True)  # Wi-Fi modülünü etkinleştirir.
    wlan.connect(ssid, password)  # Belirtilen SSID ve şifre ile Wi-Fi ağına bağlanır.
    connection_timeout = 10  # Bağlantı süresi sınırını 10 saniye olarak belirler.
    while connection_timeout > 0:  # Belirtilen süre boyunca Wi-Fi bağlantısını kontrol eder.
        if wlan.status() >= 3:  # Bağlantı durumu 3 veya daha büyükse bağlantının başarılı olduğunu gösterir.
            print("Connected to Wi-Fi!")  # Wi-Fi'ye başarıyla bağlanıldığını bildirir.
            network_info = wlan.ifconfig()  # Wi-Fi bağlantı bilgilerini alır.
            print('IP address:', network_info[0])  # Bağlantının IP adresini ekrana yazdırır.
            return True  # Fonksiyon başarılı olduğunda True döner.
        connection_timeout -= 1  # Zamanlayıcıyı 1 saniye azaltır.
        print('Waiting for Wi-Fi connection...')  # Wi-Fi bağlantısı için beklenildiğini bildirir.
        sleep(1)  # 1 saniyelik bekleme.
    print('Failed to connect to Wi-Fi.')  # Bağlantının başarısız olduğunu bildirir.
    return False  # Fonksiyon başarısız olduğunda False döner.

# WhatsApp mesajı gönderme fonksiyonu
def send_message(phone_number, api_key, message):
    url = f'https://api.callmebot.com/whatsapp.php?phone={phone_number}&text={message}&apikey={api_key}'  
    # CallMeBot API URL'sini, telefon numarası, mesaj ve API anahtarı ile oluşturur.
    try:
        response = requests.get(url)  # API'ye GET isteği gönderir.
        if response.status_code == 200:  # Eğer sunucudan başarılı bir yanıt dönerse:
            print('Message sent successfully!')  # Mesajın başarıyla gönderildiğini bildirir.
        else:  # Eğer bir hata kodu dönerse:
            print('Failed to send message:', response.text)  # Hata mesajını ekrana yazdırır.
    except Exception as e:  # Eğer bir istisna (hata) meydana gelirse:
        print('Error:', e)  # Hata mesajını ekrana yazdırır.

# Ana program
if __name__ == '__main__':  # Eğer bu dosya ana dosya olarak çalıştırılıyorsa:
    if init_wifi(ssid, password):  # Wi-Fi bağlantısı başarılıysa:
        message = 'Eren%20KALAYCI%20%2f%20212701035%20%2F%20Mikro%20Denetleyiciler'  
        # Gönderilecek mesaj (URL-encoded formatında yazılmıştır).
        send_message(phone_number, api_key, message)  # Mesaj gönderme fonksiyonunu çağırır.
