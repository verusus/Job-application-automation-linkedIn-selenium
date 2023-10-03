import threading
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

url = "https://orteil.dashnet.org/experiments/cookie/"
driver.get(url)

path = '//*[@id="cookie"]'
r = driver.find_element(By.XPATH, path)

is_five_min = False


# todo: make a thread
def is_five_sec():
    global is_five_min
    while not is_five_min:
        time.sleep(5)
        print("5 sec is up!")

        time_machine = driver.find_element(By.XPATH, '//*[@id="buyTime machine"]')
        portal = driver.find_element(By.XPATH, '//*[@id="buyPortal"]')
        alchemy_lab = driver.find_element(By.XPATH, '//*[@id="buyAlchemy lab"]')
        shipment = driver.find_element(By.XPATH, '//*[@id="buyShipment"]')
        mine = driver.find_element(By.XPATH, '//*[@id="buyMine"]')
        factory = driver.find_element(By.XPATH, '//*[@id="buyFactory"]')
        grandma = driver.find_element(By.XPATH, '//*[@id="buyGrandma"]')
        cursor = driver.find_element(By.XPATH, '//*[@id="buyCursor"]')

        list_element = [time_machine, portal, alchemy_lab, shipment, mine, factory, grandma, cursor]
        for element in list_element:
            # Get the classes of the element
            element_classes = element.get_attribute("class")

            # Check if the desired class is present in the element's classes
            if "grayed" in element_classes:
                pass
            else:
                element.click()
                print("Element does not have the class 'your-desired-class'")


sec_thread = threading.Thread(target=is_five_sec)
sec_thread.start()


def is_five_minutes():
    global is_five_min
    time.sleep(5*60)
    is_five_min = True


min_thread = threading.Thread(target=is_five_minutes)
min_thread.start()

while not is_five_min:
    r.click()

