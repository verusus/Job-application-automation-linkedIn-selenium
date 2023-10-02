from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

url = "https://en.wikipedia.org/wiki/Main_Page"
driver.get(url)

path = '//*[@id="articlecount"]/a[1]'
r = driver.find_element(By.XPATH, path)
print(r.text)

# Close the browser window when you're done
# driver.close()        # to close one tab
driver.quit()
