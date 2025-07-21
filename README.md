# Scraping Alif Bank

This project scrapes currency exchange rates from the official [Alif Bank](https://www.alif.tj/) website using Selenium and Chrome in headless mode.

## 🔍 What it does

- Opens the Alif Bank website
- Extracts currency exchange rates (buy/sell) from the table
- Returns the data as a list of dictionaries

Example output:

```json
[
  {"currency": "USD", "buy": "10.90", "sell": "11.10"},
  {"currency": "EUR", "buy": "11.80", "sell": "12.00"}
]

⚙️ Installation
1. Clone the repository:
git clone https://github.com/Komron1992/Scraping-Alif-Bank.git
cd Scraping-Alif-Bank

2. Install dependencies:
pip install -r requirements.txt

🚀 Run the script
Make sure you have Python 3.8+ installed and Google Chrome available on your system.

To run the script:
python alif.py

📦 Dependencies
selenium – for browser automation

webdriver-manager – to automatically install and manage ChromeDriver

🖥 Requirements
Google Chrome (installed on your system)

Python 3.8 or higher

Internet connection
