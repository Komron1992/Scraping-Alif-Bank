from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

def fetch_currency_data_alif():
    # Настройка Chrome в headless-режиме
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    try:
        driver.get("https://www.alif.tj/")
        time.sleep(5)  # Ждём, пока загрузится динамический контент

        rates = []

        # Находим таблицу курсов валют
        rows = driver.find_elements(By.CSS_SELECTOR, "tbody.text-lg tr")
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            if len(cols) == 3:
                currency_text = cols[0].text.strip()
                if currency_text.startswith("1 "):  # например, "1 USD"
                    currency = currency_text.replace("1 ", "")
                    buy = cols[1].text.strip()
                    sell = cols[2].text.strip()
                    rates.append({
                        "currency": currency,
                        "buy": buy,
                        "sell": sell
                    })
        return rates
    finally:
        driver.quit()

# Пример запуска
if __name__ == '__main__':
    result = fetch_currency_data_alif()
    print(result)



