# Basics
import json
import os

# Libs
import multiprocessing
from colorama import init, Fore

# Files
from screenshots import get_screenshots


# Main function to work with
def main():

    init()

    # Load Config
    with open('config.json', 'r') as file:
        config = json.load(file)

    # Create "screenshots" directory if it doesn't exist
    directory = 'screenshots'
    if not os.path.exists(directory):
        os.makedirs(directory)

    processes = []

    # Get screenshots
    for f in range(0, config['processes_amount']):
        process = multiprocessing.Process(target=get_screenshots)
        processes.append(process)
        process.start()
        print(f'[ {Fore.GREEN}SUCCESS{Fore.RESET} ] Process #{f} Started')


if(__name__ == '__main__'):
    main()
