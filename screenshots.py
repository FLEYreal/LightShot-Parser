# Basics
import os
import requests
import random
import json

# Libs
from bs4 import BeautifulSoup
from colorama import Fore

def generate_random_string(length=7):
    letters = "abcdefghijklmnopqrstuvwxyz0123456789"
    return ''.join(random.choice(letters) for _ in range(length))


def get_screenshots():

    # Load Config
    with open('config.json', 'r') as file:
        config = json.load(file)

    # Generate Images
    while True:
        try:
            image_name = generate_random_string(random.randint(3,8))

            # Setup Session
            sess = requests.Session()
            sess.headers.update(config['request_data']['headers'])

            # Get page
            response = sess.get('https://prnt.sc/{}'.format(image_name))

            parser = BeautifulSoup(response.text, "html.parser")
            image_url = parser.find('meta', attrs={'property': 'og:image'})

            if not image_url:
                print(f"[ {Fore.RED}FAIL{Fore.RESET} ] Cloudflare blocked request")

            image_url = image_url.get('content')

            # If image is nothing
            if 'http' not in image_url:
                print(f"[ {Fore.RED}FAIL{Fore.RESET} ] Nothing was found")
                continue

            # Get image & Generate name
            image = sess.get(image_url)

            with open(os.path.join('screenshots', image_name + image_url[-5:]), 'wb') as file:
                file.write(image.content)

            print(f"[ {Fore.GREEN}SUCCESS{Fore.RESET} ] Image is found!")
        
        # Throw an error
        except Exception as e:
            print(f'[ {Fore.RED}EXCEPTION {Fore.RESET}]', e)


