# 'https://prnt.sc/12fgtea'

# 1. Генератор ссылок
# 2. Парсинг сайта
# 3. Сохранение скриншота
# 
# 4. API ChatGPT

# Libs
import json
from colorama import init

# Files
from screenshots import get_screenshots


# Main function to work with
def main():

    init()

    # Load Config
    with open('config.json', 'r') as file:
        config = json.load(file)

    # Get screenshots
    get_screenshots(config['attempts_amount'])


if(__name__ == '__main__'):
    main()
