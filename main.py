import requests
import time
import sys
import os

def make_ping(interval, url):
    while True:
        try:
            response = requests.get(url)
            
            if response.status_code == 200:
                try:
                    json_data = response.json()
                    print(json_data)
                except ValueError:
                    print("Odpowiedź nie jest w formacie JSON.")
            else:
                print(f"Zapytanie do {url} zakończone niepowodzeniem. Kod statusu: {response.status_code}")
        
        except requests.exceptions.RequestException as e:
            print(f"Błąd połączenia: {e}")
        
        time.sleep(interval)

def main():
    try:
        interval = int(os.getenv("MAKEPING_INTERVAL"))
        url = os.getenv("MAKEPING_URL")
        
        make_ping(interval, url)
    
    except ValueError:
        print("Interwał musi być liczbą całkowitą.")
        sys.exit(1)

if __name__ == "__main__":
    main()
