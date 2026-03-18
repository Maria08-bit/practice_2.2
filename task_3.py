import requests
import json

URL = "https://www.cbr-xml-daily.ru/daily_json.js"
FILE = "resource/save.json"


def get_data():
    try:
        return requests.get(URL, timeout=5).json()["Valute"]
    except Exception:
        print("Ошибка: не удалось получить данные")
        return {}


def load():
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


def save(data):
    try:
        with open(FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception:
        print("Ошибка: не удалось сохранить файл")


def show_all():
    data = get_data()
    if not data:
        return

    for code, value in data.items():
        print(code, "-", value["Value"])


def show_one():
    code = input("Код валюты: ").upper().strip()

    if not code:
        print("Ошибка: код пустой")
        return

    data = get_data()

    if code in data:
        print(code, "-", data[code]["Value"])
    else:
        print("Ошибка: валюта не найдена")


def add_group():
    groups = load()

    name = input("Название группы: ").strip()

    if not name:
        print("Ошибка: пустое название")
        return

    if name in groups:
        print("Ошибка: группа уже существует")
        return

    data = get_data()

    codes = input("Коды валют (через пробел): ").upper().split()

    if not codes:
        print("Ошибка: введите валюты")
        return

    valid_codes = [c for c in codes if c in data]

    if not valid_codes:
        print("Ошибка: нет корректных валют")
        return

    groups[name] = valid_codes
    save(groups)

    print("Группа создана")


def show_groups():
    groups = load()

    if not groups:
        print("Нет групп")
        return

    for name, codes in groups.items():
        print(f"{name}: {', '.join(codes)}")


def edit_group():
    groups = load()

    name = input("Название группы: ").strip()

    if name not in groups:
        print("Ошибка: группа не найдена")
        return

    data = get_data()

    print("1 - добавить валюту")
    print("2 - удалить валюту")

    action = input("> ").strip()

    code = input("Код валюты: ").upper().strip()

    if not code:
        print("Ошибка: код пустой")
        return

    if action == "1":
        if code not in data:
            print("Ошибка: такой валюты нет")
            return

        if code in groups[name]:
            print("Валюта уже есть")
        else:
            groups[name].append(code)
            save(groups)
            print("Добавлено")

    elif action == "2":
        if code not in groups[name]:
            print("Такой валюты нет в группе")
        else:
            groups[name].remove(code)
            save(groups)
            print("Удалено")

    else:
        print("Ошибка: неверная команда")


while True:
    print("\n1 все валюты")
    print("2 одна валюта")
    print("3 создать группу")
    print("4 показать группы")
    print("5 редактировать группу")
    print("0 выход")

    choice = input("> ").strip()

    if not choice:
        print("Ошибка: пустая команда")
        continue

    if choice == "1":
        show_all()
    elif choice == "2":
        show_one()
    elif choice == "3":
        add_group()
    elif choice == "4":
        show_groups()
    elif choice == "5":
        edit_group()
    elif choice == "0":
        break
    else:
        print("Ошибка: такой команды нет")