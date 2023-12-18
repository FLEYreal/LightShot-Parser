
import requests
import random
import json
from bs4 import BeautifulSoup

url_template = 'https://prnt.sc/'
symbols = '0123456789abcdefghijklmnopqrstuvwxyz'

def get_screenshots(amount: int):

    # Load Config
    with open('config.json', 'r') as file:
        config = json.load(file)

    # Generate Images
    for f in range(amount):

        try:

            # Generate URL & Get page
            url = url_template + generate_random_string()
            response = requests.get(url, headers=config['request_data']['headers'])

            # If page is found
            if response.status_code == 200:

                parser = BeautifulSoup(response.text, "html.parser")
                image_url = parser.find('meta', attrs= {'property': 'og:image'}).get('content')

                # If image is nothing
                if image_url != '//st.prntscr.com/2023/07/24/0635/img/0_173a7b_211be8ff.png':

                    # Save found screenshot
                    with open('screenshots/index.png', 'w', encoding='utf8') as file:
                        file.write(response.text)

            # If page is not found
            elif response.status_code == 404:
                print('404 Error')
        
        # Throw an error
        except Exception as e:
            print('Error Happened:', e)


def generate_random_string(length=7):
    letters = "abcdefghijklmnopqrstuvwxyz0123456789"
    return ''.join(random.choice(letters) for _ in range(length))


