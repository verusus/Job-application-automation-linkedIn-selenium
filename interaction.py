from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

# url = "https://en.wikipedia.org/wiki/Main_Page"
# driver.get(url)

# path = '//*[@id="articlecount"]/a[1]'
# r = driver.find_element(By.XPATH, path)
# print(r.text)
# r.click()

# # find by link text
# wiki = driver.find_element(By.LINK_TEXT, "Wikipedia")
# wiki.click()


# search in the search bar and hit enter
# search = driver.find_element(By.NAME, "search")
# search.send_keys("python")
# search.send_keys(Keys.ENTER)

# fill in a form
url = "http://secure-retreat-92358.herokuapp.com/"
driver.get(url)

fname = driver.find_element(By.NAME, "fName")
fname.send_keys("hamid")
fname.send_keys(Keys.TAB)

lname = driver.find_element(By.NAME, "lName")
lname.send_keys("salhi")
lname.send_keys(Keys.TAB)

email = driver.find_element(By.NAME, "email")
email.send_keys("hamid@gmail.com")
email.send_keys(Keys.TAB)
email.send_keys(Keys.ENTER)


# Close the browser window when you're done
# driver.close()        # to close one tab
# driver.quit()
