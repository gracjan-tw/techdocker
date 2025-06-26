import requests
import time
import sys

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
    if len(sys.argv) != 3:
        print("Użycie: python makePing.py <interwał_w_sekundach> <URL>")
        sys.exit(1)
    
    try:
        interval = int(sys.argv[1])
        url = sys.argv[2]
        
        make_ping(interval, url)
    
    except ValueError:
        print("Interwał musi być liczbą całkowitą.")
        sys.exit(1)

if __name__ == "__main__":
    main()
