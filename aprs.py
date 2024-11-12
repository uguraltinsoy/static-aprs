import socket
import time
import os

def main():
    serverId = int(os.getenv("SERVER", "4"))
    callsign = os.getenv("CALLSIGN", "NOCALL")
    ssid = os.getenv("SSID", "10")
    lat = float(os.getenv("LAT", "0.0"))
    lon = float(os.getenv("LON", "0.0"))
    symbol_table = os.getenv("SYMBOL_TABLE", "/")
    symbol = os.getenv("SYMBOL", "-")
    comment = os.getenv("COMMENT", "No comment")
    interval = int(os.getenv("INTERVAL", "900"))
    if interval < 60: interval = 60
    elif interval > 900: interval = 900
    elapsed_time = interval

    while True:
        if elapsed_time >= interval:
            try:
                os.system('cls' if os.name == 'nt' else 'clear')
                PASSCODE = passcode_convert(callsign)
                sendAprsPosition(serverId, callsign, ssid, PASSCODE, lat, lon, symbol_table, symbol, comment)
                elapsed_time = 0
            except:
                print("Package could not be sent")
        time.sleep(1)
        elapsed_time += 1

def sendAprsPosition(serverId, callsign, ssid, passcode, latitude, longitude, symbol_table, symbol, comment="Python via APRS"):
    server = "rotate.aprs2.net"
    if serverId == 1: server = "rotate.aprs2.net"
    elif serverId == 2: server = "noam.aprs2.net"
    elif serverId == 3: server = "soam.aprs2.net"
    elif serverId == 4: server = "euro.aprs2.net"
    elif serverId == 5: server = "asia.aprs2.net"
    elif serverId == 6: server = "aunz.aprs2.net"
    else: server = "rotate.aprs2.net"

    port = 14580

    lat_str = aprs_lat_format(latitude)
    lon_str = aprs_lon_format(longitude)
    
    aprs_position = f"{callsign}-{ssid}>APRS,TCPIP*:!{lat_str}{symbol_table}{lon_str}{symbol}{comment}\n"

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((server, port))
        
        # APRS sunucusuna oturum aç
        login_cmd = f"user {callsign} pass {passcode} vers PythonClient 1.0\n"
        s.sendall(login_cmd.encode('utf-8'))

        # Konum bilgisini gönder
        s.sendall(aprs_position.encode('utf-8'))
        
        # Sunucudan gelen yanıtı al
        response = s.recv(1024).decode('utf-8')
        response = response.rstrip("\n")
        print(f"Running, Server response: {response}")

def aprs_lat_format(latitude):
    lat_deg = int(abs(latitude))
    lat_min = (abs(latitude) - lat_deg) * 60
    direction = 'N' if latitude >= 0 else 'S'
    return f"{lat_deg:02d}{lat_min:05.2f}{direction}"

def aprs_lon_format(longitude):
    lon_deg = int(abs(longitude))
    lon_min = (abs(longitude) - lon_deg) * 60
    direction = 'E' if longitude >= 0 else 'W'
    return f"{lon_deg:03d}{lon_min:05.2f}{direction}"

def passcode_convert(callsign):
    assert isinstance(callsign, str)
    callsign = callsign.split('-')[0].upper()
    code = 0x73e2
    for i, char in enumerate(callsign): code ^= ord(char) << (8 if not i % 2 else 0)
    return code & 0x7fff

if __name__ == "__main__":
    main()
