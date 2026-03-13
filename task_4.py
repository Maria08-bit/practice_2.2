import requests

try:
    user = input("Введите имя пользователя GitHub: ").strip()

    if not user:
        print("Ошибка: имя пользователя не может быть пустым.")
        exit()

    url = f"https://api.github.com/users/{user}"

    response = requests.get(url)

    if response.status_code == 404:
        print("Ошибка: пользователь не найден.")
        exit()

    if response.status_code != 200:
        print("Ошибка: не удалось получить данные профиля.")
        exit()

    data = response.json()

    print("\n--- Профиль пользователя ---")
    print("Имя:", data.get("name"))
    print("Ссылка:", data.get("html_url"))
    print("Количество репозиториев:", data.get("public_repos"))
    print("Количество подписок:", data.get("following"))
    print("Количество подписчиков:", data.get("followers"))

    repos_response = requests.get(url + "/repos")

    if repos_response.status_code != 200:
        print("Ошибка: не удалось получить список репозиториев.")
        exit()

    repos = repos_response.json()

    print("\n--- Репозитории ---")

    if not repos:
        print("У пользователя нет репозиториев.")
    else:
        for r in repos:
            print("Название:", r.get("name"))
            print("Ссылка:", r.get("html_url"))
            print("Язык:", r.get("language"))
            print("Видимость:", r.get("visibility"))
            print("Ветка по умолчанию:", r.get("default_branch"))
            print("-" * 30)

except Exception:
    print("Произошла неизвестная ошибка.")