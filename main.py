import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from linkedin_scraper import actions


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)


email = "salhiabdelhamid01@gmail.com"
password = "TEST@TEST11"
actions.login(driver, email, password) # if email and password isnt given, it'll prompt in terminal
# Navigate to a URL
url = "https://www.linkedin.com/jobs/search/?currentJobId=3711478515&distance=25&f_AL=true&f_E=2%2C3%2C4&f_F=it%2Ceng%2Cbd%2Ccnsl%2Cothr%2Cfin%2Cprjm%2Canls%2Cprdm%2Cqa%2Crsch%2Ccust&f_I=96%2C6%2C4%2C3132%2C104%2C43%2C3231%2C84%2C137%2C41%2C108%2C123%2C53%2C118&f_JT=F%2CP%2CC%2CT%2CO&f_PP=105214831%2C105556991%2C100495523%2C103077496%2C106164952%2C102571732%2C102277331%2C106224388%2C104472865%2C103671728%2C105466038%2C107116391%2C103693101%2C106088647%2C106672002%2C100075706%2C101421689%2C102244498%2C103089792&f_T=9%2C25201%2C25194%2C25169%2C10738%2C17265%2C25170%2C39%2C30006%2C14893%2C25764%2C2732%2C4384&f_WT=1%2C3%2C2&geoId=92000000&keywords=python%20developer&sortBy=DD"
# url = "https://www.python.org/"
driver.get(url)
# todo later 1: use this way to automate sending messages to people (hr) or to find the peoples urns in csv file

# path = '/html/body/div[1]/header/nav/div/a[2]'
# r = driver.find_element(By.XPATH, path)
# r.click()
#
# google_sign_in_path = '//*[@id="container"]/div/div[1]'
# r = driver.find_element(By.XPATH, path)
# r.click()
#
# time.sleep(5)
# driver.implicitly_wait(10)
# r = driver.find_element(By.ID, "username")
# r.send_keys("essalhi12345@gmail.com")
# PASS: HAMID@ESSALHI11

# Close the browser window when you're done
# driver.close()        # to close one tab
# driver.quit()
