import requests
import time
import datetime

def misura_download():
    # Scarica un file di test e misura la velocità
    url = "http://speedtest.tele2.net/10MB.zip"
    start = time.time()
    r = requests.get(url, stream=True, timeout=30)
    scaricato = 0
    for chunk in r.iter_content(chunk_size=8192):
        scaricato += len(chunk)
        if scaricato >= 5 * 1024 * 1024:  # ferma dopo 5MB
            break
    fine = time.time()
    durata = fine - start
    velocita = (scaricato / 1_000_000) / durata  # Mbps
    return round(velocita, 2)

def misura_ping():
    start = time.time()
    requests.get("https://google.com", timeout=10)
    fine = time.time()
    return round((fine - start) * 1000, 2)  # in millisecondi

def controlla_internet():
    try:
        requests.get("https://google.com", timeout=5)
        return True
    except:
        return False

def avvia_bot():
    print("=== BOT MONITOR RETE AVVIATO ===")
    print("Premi CTRL+C per fermare\n")
    while True:
        ora = datetime.datetime.now().strftime("%H:%M:%S")
        if not controlla_internet():
            print(f"[{ora}] CONNESSIONE ASSENTE!")
        else:
            print(f"[{ora}] Misurazione in corso...")
            ping = misura_ping()
            download = misura_download()
            print(f"[{ora}]")
            print(f"  Download : {download} Mbps")
            print(f"  Ping     : {ping} ms")
            if ping > 100:
                print("  ATTENZIONE: ping alto!")
            if download < 5:
                print("  ATTENZIONE: download lento!")
            print()
        time.sleep(60)

avvia_bot()
