import network
import socket
import requests
from time import sleep

# Wi-Fi ayarları
ssid = 'ernklyc'
password = '49200156'
phone_number = '905438967227'
api_key = '3964202'

def init_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    
    for _ in range(10):
        if wlan.status() >= 3:
            print('WiFi Bağlandı!')
            ip = wlan.ifconfig()[0]
            print(f'\nWeb arayüzüne gitmek için: http://{ip}')
            print('Link\'e tıklayarak veya tarayıcınıza yapıştırarak açabilirsiniz.')
            return True
        sleep(1)
    return False

def send_whatsapp(message):
    message = message.replace(' ', '%20')
    message = message.replace('ı', 'i').replace('ğ', 'g').replace('ü', 'u')
    message = message.replace('ş', 's').replace('ö', 'o').replace('ç', 'c')
    
    url = f'https://api.callmebot.com/whatsapp.php?phone={phone_number}&text={message}&apikey={api_key}'
    try:
        response = requests.get(url)
        return response.status_code == 200
    except:
        return False

def web_page(success=False):
    html = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>WhatsApp Mesaj</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: Arial, sans-serif;
        }
        body {
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            background: linear-gradient(135deg, #25D366, #128C7E);
            padding: 20px;
        }
        .container {
            background: white;
            padding: 30px;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            width: 90%;
            max-width: 450px;
        }
        h1 {
            color: #128C7E;
            text-align: center;
            margin-bottom: 20px;
            font-size: 24px;
        }
        textarea {
            width: 100%;
            padding: 15px;
            border: 2px solid #ddd;
            border-radius: 10px;
            margin-bottom: 20px;
            min-height: 120px;
            font-size: 16px;
            resize: none;
        }
        textarea:focus {
            border-color: #25D366;
        }
        button {
            background: #25D366;
            color: white;
            border: none;
            padding: 15px;
            width: 100%;
            border-radius: 10px;
            cursor: pointer;
            font-size: 16px;
            font-weight: bold;
        }
        button:hover {
            background: #128C7E;
        }
        .footer {
            margin-top: 20px;
            color: white;
            text-align: center;
        }
        .status {
            text-align: center;
            padding: 15px;
            background: #25D366;
            color: white;
            border-radius: 10px;
            margin-top: 15px;
            display: ''' + ('block' if success else 'none') + ''';
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>WhatsApp Mesaj Paneli</h1>
        <form method="POST" onsubmit="showStatus()">
            <textarea name="message" placeholder="Mesajınızı buraya yazın..." required></textarea>
            <button type="submit">MESAJI GÖNDER</button>
        </form>
        <div class="status">Mesaj Gönderiliyor...</div>
    </div>
    <div class="footer">
        Eren KALAYCI © 2024 | Mikro Denetleyiciler
    </div>
    <script>
        function showStatus() {
            document.querySelector('.status').style.display = 'block';
            setTimeout(function() {
                window.location.href = "/";
            }, 3000);
        }
        ''' + ('showStatus();' if success else '') + '''
    </script>
</body>
</html>
    '''
    return html

def web_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 80))
    s.listen(5)
    
    while True:
        try:
            conn, addr = s.accept()
            request = conn.recv(1024).decode()
            
            success = False
            if 'POST' in request:
                try:
                    message = request.split('\r\n\r\n')[1].split('=')[1]
                    message = message.replace('+', ' ')
                    if send_whatsapp(message):
                        success = True
                except:
                    pass
            
            response = web_page(success)
            conn.send('HTTP/1.1 200 OK\n')
            conn.send('Content-Type: text/html\n')
            conn.send('Connection: close\n\n')
            conn.sendall(response)
            conn.close()
            
        except Exception as e:
            print('Hata:', e)
            conn.close()

if init_wifi():
    web_server()
