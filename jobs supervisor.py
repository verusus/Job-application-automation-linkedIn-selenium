from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from linkedin_scraper import actions
from pprint import pprint

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

email = "salhiabdelhamid01@gmail.com"
password = "TEST@TEST11"
#email = "essalhi12345@gmail.com"
#password = "HAMID@ESSALHI11"

actions.login(driver, email, password, timeout=30)  # if email and password isnt given, it'll prompt in terminal

# Python URL
url = "https://www.linkedin.com/jobs/search/?currentJobId=3162047620&distance=25&f_AL=true&f_CR=103644278%2C102787409%2C101165590&f_E=2%2C3%2C4&f_F=it%2Ceng%2Cqa%2Cfin%2Ccnsl%2Cbd%2Cothr%2Cprdm%2Canls%2Ccust%2Cprjm%2Crsch&f_I=96%2C6%2C4%2C104%2C3231%2C3132%2C43%2C84%2C137%2C118%2C123%2C41%2C53%2C108&f_JT=F%2CP%2CC%2CT%2CO&f_PP=105214831%2C105556991%2C100495523%2C103077496%2C106164952%2C102571732%2C102277331%2C106224388%2C104472865%2C103671728%2C105466038%2C107116391%2C103693101%2C106088647%2C106672002%2C100075706%2C101421689%2C102244498%2C103089792&f_T=9%2C25169%2C30006%2C25201%2C2732%2C10738%2C25194%2C25170%2C39%2C25764%2C4384%2C14893%2C17265&f_WT=1%2C3%2C2&geoId=92000000&keywords=python%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&sortBy=DD"
# url = "https://www.python.org/"
driver.get(url)
driver.implicitly_wait(3)
# r = driver.find_element(By.CLASS_NAME, "jobs-search-results-list")
jobs = driver.find_elements(By.CLASS_NAME, 'job-card-container__footer-item inline-flex align-items-center')
# jobs = driver.find_elements(By.XPATH, "//div[@data-job-id]")
# jobs = driver.find_elements(By.XPATH, "//div[@class='job-card-list__insight']/ul[@class]")
# pprint(r.text)
for job in jobs:
    print(job.text)

driver.find_element()