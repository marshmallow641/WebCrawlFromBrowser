# Works on Mac, not on Windows 10 - webdriver_manager can only be found/installed on Mac
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import time

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

url = "https://www.selenium.dev/selenium/web/web-form.html"

if __name__ == '__main__':
    driver.get(url)
    time.sleep(10.0)

    driver.quit()
