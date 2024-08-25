"""
ProxyCheck - программа для проверки работоспособности прокси-серверов (SOCKS5 и HTTP).

Описание:
Эта программа загружает списки прокси с открытого репозитория, проверяет их доступность
и выводит список работающих прокси. Поддерживаются прокси-серверы SOCKS5 и HTTP.

Списки прокси берутся из следующего репозитория:
https://github.dev/TheSpeedX/PROXY-List/

Использование этой программы предполагает соблюдение лицензии оригинального репозитория.

Автор репозитория с прокси: TheSpeedX
"""
import requests


class ProxyCheck:

    def __init__(self):
        self.test_url = "http://httpbin.org/ip"
        self.work_proxy_list_socks5 = []
        self.work_proxy_list_http = []

        # URL для чтения списка прокси
        self.proxy_url_socks5 = "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt"
        self.proxy_url_http = "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt"

    def get_proxy(self):
        with open("proxy_list.txt", "r", encoding="utf-8") as file:
            return [line.strip() for line in file]

    def getting_proxy_by_url(self, proxy_url):
        proxy_list = []
        response = requests.get(proxy_url, timeout=10)
        response.raise_for_status()  # Проверка на успешный ответ

        for line in response.text.splitlines():
            proxy_list.append(line.strip())

        return proxy_list

    def fetch_proxies(self, proxy_url):
        """Получает список прокси с указанного URL"""
        try:

            raw_proxy_list = self.getting_proxy_by_url(proxy_url)

            return raw_proxy_list

        except requests.RequestException as e:
            print(f"Ошибка получения списка прокси: {e}")
            return []

    def check_proxy(self, proxy):
        """
        Проверяет работоспособность прокси.

        :param proxy: Прокси в формате "http://IP:порт" или "socks5://IP:порт"
        :return: True если прокси работает, False в противном случае
        """
        proxies = {
            "http": proxy,
            "https": proxy,
        }

        try:
            # Выполняем запрос через прокси
            response = requests.get(self.test_url, proxies=proxies, timeout=45)

            # Проверяем, что код ответа успешный
            if response.status_code == 200:
                return True
        except requests.RequestException as e:
            # В случае ошибки, прокси не работает
            print(f"Ошибка при проверке прокси {proxy}: {e}")
            pass

        return False

    def process_proxies(self, proxy_list, proxy_type):
        """
        Обрабатывает список прокси, проверяя их работоспособность.

        :param proxy_list: Список прокси
        :param proxy_type: Тип прокси (например, SOCKS5 или HTTP)
        """
        working_proxies = []
        count = 0

        for proxy in proxy_list:
            if self.check_proxy(proxy):
                working_proxies.append(proxy)
                count += 1
                print(f"Прокси {proxy} работает.")

        print(f"Рабочих {proxy_type} прокси обнаружено: {count}")

        return working_proxies

    def save_proxies_to_file(self, filename, proxies):
        """Сохраняет список прокси в файл"""
        try:
            with open(filename, "w", encoding="utf-8") as file:
                for proxy in proxies:
                    file.write(proxy + "\n")
            print(f"Список прокси сохранен в {filename}")
        except IOError as e:
            print(f"Ошибка записи в файл {filename}: {e}")

    def run(self):
        # Получаем и проверяем SOCKS5 прокси
        proxy_list_socks5 = self.fetch_proxies(self.proxy_url_socks5)
        self.work_proxy_list_socks5 = self.process_proxies(proxy_list_socks5, "SOCKS5")

        # Получаем и проверяем HTTP прокси
        proxy_list_http = self.fetch_proxies(self.proxy_url_http)
        self.work_proxy_list_http = self.process_proxies(proxy_list_http, "HTTP")

        # Сохранение рабочих прокси в файлы
        self.save_proxies_to_file("working_socks5_proxies.txt", self.work_proxy_list_socks5)
        self.save_proxies_to_file("working_http_proxies.txt", self.work_proxy_list_http)


if __name__ == "__main__":
    PCH = ProxyCheck()
    PCH.run()

