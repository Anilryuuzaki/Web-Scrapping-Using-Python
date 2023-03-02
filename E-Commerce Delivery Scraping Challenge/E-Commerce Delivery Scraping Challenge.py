from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


sheet_url = "https://docs.google.com/spreadsheets/d/1QQj8gAD9jexgz2OoYEyQOIe7xVSG-0r0FyTDHSAYYg0/export?format=csv"

df = pd.read_csv(sheet_url, header = None)

# Extract the links from the cells in the "Links" column
links = df.iloc[:, 0]

# Loop through the links and extract the data of each web page
for link in links:
# create options object for headless mode
    options = Options()
    options.add_argument('--headless')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument('--disable-gpu')  # necessary if running on Windows

    # create a Chrome browser instance with the headless options
    browser = webdriver.Chrome(options=options)
    browser.get(link)
    
    try:
    # Find the element that needs to be hovered over
        hover_element = browser.find_element(By.ID, "pc-drawer-id-1")
    except:
        continue

    # Simulate the hover event
    hover = ActionChains(browser).move_to_element(hover_element)
    hover.perform()

    # Scrape the data that appears
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')
    
    types = []

    for data in soup.findAll('div',class_="XVLaDH"):
        type = data.find('div', attrs={'class': "AAaUS1"})
        types.append(type.text)
    browser.quit()
    print(', '.join(types))




