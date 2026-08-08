from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


def create_driver():
    options = Options()

    options.add_argument(
        "--start-maximized"
    )

    options.add_argument(
        "--disable-blink-features=AutomationControlled"
    )

    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/127.0.0.0 Safari/537.36"
    )

    driver = webdriver.Chrome(options=options)
    return driver


def get_page_html(driver, url):
    driver.get(url)
    time.sleep(5)

    current_url = driver.current_url

    if current_url != url:
        raise Exception(f"Redirect detected. Requested: {url}, got: {current_url}")

    return driver.page_source
