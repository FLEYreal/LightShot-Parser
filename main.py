# Basics
import json

# Libs
import multiprocessing
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
    for f in range(1, config['processes_amount']):
        parsing = multiprocessing.Process(target=get_screenshots())
        parsing.start()


if(__name__ == '__main__'):
    main()
