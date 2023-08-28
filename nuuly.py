from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os
import argparse

# Parses arguments passed for the desired url and size
parser = argparse.ArgumentParser()
parser.add_argument('--url')
parser.add_argument('--size')
args = parser.parse_args()
url = args.url
desired_size = args.size

# Grabs the item name from the url
item_name = url.replace("/", ' ')
item_name = item_name.split('?')[0]
item_name = item_name.split(' ')[-1]

# Sets up the chrome driver
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)

# infinite loop scraping website until item is available
item_not_available = True
while item_not_available:

    driver.get(url)

    # Returns all sizes
    sizes = driver.find_elements(By.CLASS_NAME, "c-inline-tile__text")

    # Returns sizes that are unavailable
    disabled = driver.find_elements(By.CLASS_NAME, "c-inline-tile--disabled")

    # Creates list of unavailable sizes
    disabled_sizes = []
    for size in disabled:
        disabled_sizes.append(size.text)
        print("disabled sizes: " + size.text)

    # Texts user if their desired size is available
    # Change phone number in the applescript module
    if desired_size not in disabled_sizes:
        print(f"{desired_size} is available!")
        message = f'Your-nuuly-outfit-{item_name}-is-available!'
        os.system(f'osascript text_user.applescript {message}')
        item_not_available = False
    time.sleep(30) 

