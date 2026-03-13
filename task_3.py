import requests, json

URL = "https://www.cbr-xml-daily.ru/daily_json.js"
FILE = "resource/save.json"

def get_data():
    try:
        return requests.get(URL, timeout=5).json()["Valute"]
    except:
        print("Ошибка: не удалось получить данные")
        return {}

def load():
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {}

def save(data):
    try:
        with open(FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except:
        print("Ошибка: не удалось сохранить файл")

def show_all():
    data = get_data()
    for k, v in data.items():
        print(k, "-", v["Value"])

def show_one():
    code = input("Код валюты: ").upper().strip()
    if not code:
        print("Ошибка: код пустой")
        return

    data = get_data()
    print(code, data[code]["Value"]) if code in data else print("Ошибка: валюта не найдена")

def add_group():
    groups = load()

    name = input("Название группы: ").strip()
    if not name:
        print("Ошибка: пустое название")
        return
    if name in groups:
        print("Ошибка: группа уже существует")
        return

    codes = input("Коды валют: ").upper().split()
    if not codes:
        print("Ошибка: введите валюты")
        return

    groups[name] = codes
    save(groups)
    print("Группа создана")

def show_groups():
    groups = load()
    if not groups:
        print("Нет групп")
        return

    for g, c in groups.items():
        print(g + ":", ", ".join(c))

def edit_group():
    groups = load()
    name = input("Название группы: ").strip()

    if name not in groups:
        print("Ошибка: группа не найдена")
        return

    act = input("добавить/удалить (д/у): ").lower()
    code = input("Код валюты: ").upper().strip()

    if not code:
        print("Ошибка: код пустой")
        return

    if act == "д":
        if code in groups[name]:
            print("Валюта уже есть")
        else:
            groups[name].append(code)
            save(groups)
            print("Добавлено")

    elif act == "у":
        if code not in groups[name]:
            print("Такой валюты нет")
        else:
            groups[name].remove(code)
            save(groups)
            print("Удалено")

    else:
        print("Ошибка: команда неверная")

while True:
    print("\n1 все валюты")
    print("2 одна валюта")
    print("3 создать группу")
    print("4 показать группы")
    print("5 редактировать группу")
    print("0 выход")

    c = input("> ").strip()

    if not c:
        print("Ошибка: пустая команда")
        continue

    if c == "1":
        show_all()
    elif c == "2":
        show_one()
    elif c == "3":
        add_group()
    elif c == "4":
        show_groups()
    elif c == "5":
        edit_group()
    elif c == "0":
        break
    else:
        print("Ошибка: такой команды нет")