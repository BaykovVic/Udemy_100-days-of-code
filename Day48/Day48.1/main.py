from selenium import webdriver


firefox_options = webdriver.FirefoxOptions()
driver = webdriver.Firefox()

driver.get("https://google.com")
driver.close()
driver.quit()

