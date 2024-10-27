from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import random

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode (without opening a browser window)
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Set up the absolute path to your WebDriver
path = 'D:\\djangoProject\\python_bot\\chromedriver.exe'  # Use the full path

# Initialize the WebDriver using the Service class
webdriver_service = Service(executable_path=path)
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

try:
    # Open the website
    driver.get('https://m.alemsesi.com/song/15192/merdan-jepbarow---yetissem')

    # Loop to simulate 1,000 plays
    for i in range(1000):
        try:
            # Find the play button using XPath and click it
            play_button = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[1]/div[1]/div[1]/div[7]/div/button[1]')
            play_button.click()
            print(f"Play {i + 1} clicked.")

            # Wait for a while to simulate listening to the song
            play_duration = random.randint(30, 60)
            time.sleep(play_duration)

            # Reload the page before the next play to ensure it counts as a new session
            driver.refresh()

            # Random delay before the next iteration to mimic human behavior
            delay = random.randint(5, 20)
            time.sleep(delay)

        except Exception as e:
            print(f"Error on play {i + 1}: {e}")
            time.sleep(10)

finally:
    # Close the WebDriver
    driver.quit()
    print("Finished 1,000 plays.")
