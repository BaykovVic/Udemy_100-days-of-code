from selenium import webdriver
from selenium.webdriver.common.by import By

firefox_options = webdriver.FirefoxOptions()
driver = webdriver.Firefox()

driver.get("https://market.yandex.ru/product--galaxy-s24/49508300?sku=102662400825&uniqueId=921897&do-waremd5=MAk2v7zHQVDu40Wi_R2ddQ")
price_div = driver.find_element(By.CLASS_NAME, "_1lRPs")
price_h3 = price_div.find_element(By.TAG_NAME, "h3")
price_spans = price_h3.find_elements(By.TAG_NAME, "span")

for price_span in price_spans:
    try:
        price_span.get_attribute("data-auto")
    except:
        continue
    else:
        print(price_span.text)

# Using XPath

price_span = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[1]/div/div[1]/div[3]/div[3]/section[1]/div[1]/div[2]/div/div[2]/div[1]/div[4]/div[1]/div/div[2]/div[1]/div/div/h3/span[2]")
print(f"XPATH: {price_span.text}")
driver.close()
driver.quit()

