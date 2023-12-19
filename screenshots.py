# Basics
import os
import requests
import random
import json

# Libs
from bs4 import BeautifulSoup
from colorama import Fore

url_template = 'https://prnt.sc/'
symbols = '0123456789abcdefghijklmnopqrstuvwxyz'

def generate_random_string(length=7):
    letters = "abcdefghijklmnopqrstuvwxyz0123456789"
    return ''.join(random.choice(letters) for _ in range(length))


def get_screenshots(amount: int):

    # Load Config
    with open('config.json', 'r') as file:
        config = json.load(file)

    # Generate Images
    for f in range(amount):

        try:

            # Setup Session
            sess = requests.Session()
            sess.headers.update(config['request_data']['headers'])

            # Generate URL & Get page
            url = url_template + generate_random_string()
            response = sess.get(url)

            # If page is found
            if response.status_code == 200:

                parser = BeautifulSoup(response.text, "html.parser")
                image_url = parser.find('meta', attrs= {'property': 'og:image'})

                if not image_url:
                    print(f"[ {Fore.RED}FAIL{Fore.RESET} ] Cloudflare blocked request")

                image_url = image_url.get('content')

                # If image is nothing
                if 'http' not in image_url:
                    print(f"[ {Fore.RED}FAIL{Fore.RESET} ] Screenshot was removed")
                    continue

                # Get image & Generate name
                image = sess.get(image_url)
                image_name = generate_random_string(10)
                
                with open(os.path.join('screenshots', image_name + image_url[-5:]), 'wb') as file:
                    file.write(image.content)

                print(f"[ {Fore.GREEN}SUCCESS{Fore.RESET} ] Image is found!")


            # If page is not found
            elif response.status_code == 404:
                print(f'[ {Fore.RED}FAIL{Fore.RESET} ] Page is not Found')
                continue
        
        # Throw an error
        except Exception as e:
            print(f'[ {Fore.RED}EXCEPTION {Fore.RESET}]', e)


