import psutil

print("Системный монитор")

cpu = psutil.cpu_percent(interval=1)
print("Загрузка CPU:", cpu, "%")

ram = psutil.virtual_memory().percent
print("Использование RAM:", ram, "%")

disk = psutil.disk_usage('/').percent
print("Использование диска:", disk, "%")