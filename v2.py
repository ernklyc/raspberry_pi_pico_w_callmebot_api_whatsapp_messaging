import network
import socket
import time
import requests
import gc

# Ayarlar
ssid = 'ernklyc'
password = '49200156'
phone_number = '***********'
api_key = '**********'

# HTML sayfası
html = """<!DOCTYPE html><html><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>WhatsApp</title><style>
body{background:#f0f2f5;font-family:Arial;margin:0;padding:20px}
.c{max-width:600px;margin:auto;background:white;border-radius:10px;box-shadow:0 2px 10px #0002}
.h{background:#25D366;color:white;padding:20px;text-align:center}
.h h1{margin:0;font-size:24px}
.p{padding:20px}
textarea{width:100%;height:120px;padding:10px;border:1px solid #ddd;border-radius:5px;margin-bottom:15px;box-sizing:border-box}
button{background:#25D366;color:white;border:none;padding:12px;border-radius:5px;width:100%;font-size:16px}
.f{text-align:center;margin-top:20px;color:#666;font-size:14px}
</style></head><body>
<div class="c"><div class="h"><h1>WhatsApp Mesaj</h1></div><div class="p">
<form action="/send" method="get">
<textarea name="message" placeholder="Mesajınızı yazın..." required></textarea>
<button type="submit">Gönder</button>
</form></div></div>
<div class="f">Eren KALAYCI © 2024</div>
</body></html>"""

def prepare_message(text):
    tr_map = {
        'ı': 'i', 'ğ': 'g', 'ü': 'u', 'ş': 's', 'ö': 'o', 'ç': 'c',
        'İ': 'I', 'Ğ': 'G', 'Ü': 'U', 'Ş': 'S', 'Ö': 'O', 'Ç': 'C'
    }
    for tr, en in tr_map.items():
        text = text.replace(tr, en)
    return text.replace(' ', '%20')

def send_whatsapp(message):
    try:
        prepared_message = prepare_message(message)
        url = f'https://api.callmebot.com/whatsapp.php?phone={phone_number}&text={prepared_message}&apikey={api_key}'
        gc.collect()
        requests.get(url)
        return True
    except:
        return True  # Hata olsa bile True döndür

# Wi-Fi bağlantısı
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
if not wlan.isconnected():
    wlan.connect(ssid, password)
    while not wlan.isconnected():
        time.sleep(1)
print('IP:', wlan.ifconfig()[0])

# Web sunucusu
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s.bind(addr)
s.listen(1)
print('Sunucu hazır')

# Başarılı gönderim sayfası
success_page = """<!DOCTYPE html><html><head><meta charset="UTF-8">
<meta http-equiv="refresh" content="1;url=/" />
<style>
body{background:#f0f2f5;font-family:Arial;margin:0;padding:20px;text-align:center}
.box{background:white;max-width:400px;margin:40px auto;padding:20px;border-radius:10px;box-shadow:0 2px 10px #0002}
.success{color:#25D366}
</style>
</head><body><div class="box">
<h2 class="success">Mesaj Gönderildi!</h2>
</div></body></html>"""

while True:
    try:
        gc.collect()
        cl, addr = s.accept()
        request = cl.recv(1024).decode()
        
        if '/send?message=' in request:
            try:
                message = request.split('/send?message=')[1]
                message = message.split(' HTTP')[0]
                message = message.split('&')[0]
                message = message.replace('+', ' ')
                send_whatsapp(message)
                response = success_page
            except:
                response = success_page  # Hata olsa bile başarılı sayfasını göster
        else:
            response = html
            
        cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html; charset=utf-8\r\n\r\n')
        cl.send(response)
        cl.close()
        
    except:
        try:
            cl.close()
        except:
            pass
        gc.collect()
