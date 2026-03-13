import requests

urls = [
    "https://github.com/",
    "https://www.binance.com/en",
    "https://tomtit.tomsk.ru/",
    "https://jsonplaceholder.typicode.com/",
    "https://moodle.tomtit-tomsk.ru/"
]

def check(url):
    try:
        r = requests.get(url, timeout=5)
        code = r.status_code

        if code == 200:
            status = "доступен"
        elif code == 403:
            status = "вход запрещен"
        elif code == 404:
            status = "не найден"
        else:
            status = "не доступен"

        print(f"{url} — {status} — {code}")

    except:
        print(f"{url} — не доступен — ошибка")

for u in urls:
    check(u)