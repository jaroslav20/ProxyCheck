### EN
# ProxyCheck

ProxyCheck is a Python script designed to check the functionality of proxy server lists. This tool allows you to download HTTP and SOCKS5 proxy lists from open sources and test them for availability and functionality.

## Description

ProxyCheck uses the `requests` library to perform HTTP requests through proxy servers. The program downloads proxy lists from community-provided resources and checks which ones are active and functional.

## Features

- Download proxy lists from open sources.
- Check the availability of HTTP and SOCKS5 proxy servers.
- Save results to text files: `working_socks5_proxies.txt` and `working_http_proxies.txt`.
- Display the list of working proxies in the console.

## Installation

1. Clone the repository:
    ```bash
    git clone git@github.com:jaroslav20/ProxyCheck.git
    cd ProxyCheck
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the script:
    ```bash
    python proxy_check.py
    ```

2. The script will automatically download proxy lists, check their functionality, and display the results in the console.

## Proxy List Source

This project uses community-provided proxy lists available at the following link:
[TheSpeedX/PROXY-List](https://github.com/TheSpeedX/PROXY-List)

The proxy lists are regularly updated and available in the following formats:

- HTTP proxies: [http.txt](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)
- SOCKS5 proxies: [socks5.txt](https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt)

## License

This project is licensed under the MIT License. See the full license text in the [LICENSE](./LICENSE) file.

## Acknowledgments

Special thanks to the [TheSpeedX](https://github.com/TheSpeedX) community for providing the proxy lists and supporting open-source projects.

## Contributing

Contributions are welcome! Please feel free to submit pull requests and open issues if you have any ideas for improvements or if you encounter any bugs.

## Contact

If you have any questions or suggestions, you can reach out to me via GitHub or email at jaroslavtihonov20@gmail.com.

- 
- 
- 


## RU
# ProxyCheck

ProxyCheck - это Python-скрипт для проверки работоспособности списков прокси-серверов. Этот инструмент позволяет загружать списки HTTP и SOCKS5 прокси с открытых источников и тестировать их на предмет доступности и работоспособности.

## Описание

ProxyCheck использует библиотеку `requests` для выполнения HTTP-запросов через прокси-серверы. Программа загружает списки прокси с ресурсов, предоставленных сообществом, и проверяет, какие из них активны и работоспособны.

## Возможности

- Загрузка списков прокси с открытых источников.
- Проверка доступности HTTP и SOCKS5 прокси-серверов.
- Запись в текстовый файл working_socks5_proxies.txt и working_http_proxies.txt.
- Вывод списка рабочих прокси в консоль.

## Установка

1. Склонируйте репозиторий:
    ```bash
    git clone git@github.com:jaroslav20/ProxyCheck.git
    cd ProxyCheck
    ```

2. Установите необходимые зависимости:
    ```bash
    pip install -r requirements.txt
    ```

## Использование

1. Запустите скрипт:
    ```bash
    python proxy_check.py
    ```

2. Скрипт автоматически загрузит списки прокси, проверит их работоспособность и выведет результат в консоль.

## Источник списков прокси

Этот проект использует списки прокси-серверов, предоставленные сообществом, доступные по следующей ссылке:
[TheSpeedX/PROXY-List](https://github.com/TheSpeedX/PROXY-List)

Списки прокси обновляются регулярно и доступны в следующих форматах:

- HTTP прокси: [http.txt](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)
- SOCKS5 прокси: [socks5.txt](https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt)

## Лицензия

Этот проект распространяется под лицензией MIT. Полный текст лицензии см. в файле [LICENSE](./LICENSE).

## Благодарности

Особая благодарность сообществу [TheSpeedX](https://github.com/TheSpeedX) за предоставление списков прокси и поддержку open-source.

## Вклад

Ваш вклад приветствуется! Пожалуйста, создавайте pull-запросы и открывайте issues, если у вас есть идеи для улучшения или вы обнаружили баги.

## Контакты

Если у вас возникли вопросы или предложения, вы можете связаться со мной через GitHub или по электронной почте: jaroslavtihonov20@gmail.com.
