
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

def text_to_speech(text):
    chrome_options = Options()
    chrome_options.add_argument('--log-level=3')
    chrome_options.headless = False
    Path = "chromedriver.exe"
    driver = webdriver.Chrome(Path, options=chrome_options)
    driver.maximize_window()

    website = r"https://ttsmp3.com/text-to-speech/British%20English/"
    driver.get(website)

    ButtonSelection = Select(driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/form/select'))
    ButtonSelection.select_by_visible_text('British English / Brian')

    # Type the text into the input field
    input_field = driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/form/textarea')
    input_field.send_keys(text)

    # Click on the "DOWNLOAD MP3" button
    download_button = driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/form/input[1]')
    download_button.click()

    sleep(5)  # Wait for the download to complete (You may need to adjust the sleep duration)

    driver.quit()

# Example usage:
text_to_speech("Hello, this is Jarvis speaking. How can I assist you today?")
