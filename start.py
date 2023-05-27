from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def set_chrome_options() -> Options:
    """Sets chrome options for Selenium.
    Chrome options for headless browser is enabled.
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument('ignore-certificate-errors')
    return chrome_options

def start() -> None:
    driver = webdriver.Chrome(options=set_chrome_options())
    
    query = 'sins of a solar empire' #my query about a video game
    driver.get('http://www.google.com')

    search = driver.find_element("name", "q")
    search.send_keys(query)
    search.send_keys(Keys.RETURN)

    links = driver.find_elements(By.CSS_SELECTOR, "a") #I went on Google Search and found the container class for the link

    for link in links:
        print(link.get_attribute("href"))

    driver.close()

if __name__ == "__main__":
    start()