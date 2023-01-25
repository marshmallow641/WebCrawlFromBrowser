from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import time

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

if __name__ == '__main__':
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    time.sleep(10.0)

    driver.quit()
