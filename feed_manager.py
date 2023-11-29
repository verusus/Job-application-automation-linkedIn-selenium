from pprint import pprint
from linkedin_api import Linkedin
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from linkedin_scraper import actions
from selenium.webdriver.support.wait import WebDriverWait
from bs4 import BeautifulSoup
from selenium.webdriver.support import expected_conditions as EC
import requests

# Authenticate using any Linkedin account credentials
# api = Linkedin('salhiabdelhamid01@gmail.com', 'TEST@TEST11')
# profile = api.get_profile('abdelhamid-salhi-71b247294')
# pprint(profile)

# posts = api.get_feed_posts(limit=10, offset=0, exclude_promoted_posts=True)
# print(type(posts))
# print(posts)
# print(type(posts[0]))
# for post in posts:
#     pprint(post)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

email = "salhiabdelhamid01@gmail.com"
password = "TEST@TEST11"
actions.login(driver, email, password, timeout=30)  # if email and password isnt given, it'll prompt in terminal

# xpath = '//*[@id="ember24"]/div[2]/div/div/main/div[4]/div/div[1]'
# xpath = '//div[@class="scaffold-finite-scroll__content"]'
# xpath = '//div[@class="update-components-text relative update-components-update-v2__commentary "]'
# r = driver.find_elements(By.XPATH, xpath)
# for post in r:
#     pprint(post.text)
# todo 1: try to make soup
# driver.get("https://www.linkedin.com/feed/")
# driver.implicitly_wait(10)
# def condition_met():
#     element = EC.text_to_be_present_in_element_value((By.XPATH, "//h2[@class='visually-hidden']"), "Feed post number 5")
#     while not element:
#         # Scroll down using Keys.PAGE_DOWN
#         driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
#         element = EC.text_to_be_present_in_element_value((By.XPATH, "//h2[@class='visually-hidden']"), "Feed post number 5")


# print(EC.text_to_be_present_in_element((By.XPATH, "//h2[@class='visually-hidden']"), "Feed post number 1"))
# while EC.text_to_be_present_in_element((By.XPATH, "//h2[@class='visually-hidden']"), "Feed post number 10"):
#     # Scroll down using Keys.PAGE_DOWN
#     driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)

# WebDriverWait(driver, 30).until(method=condition_met())

# html_content = driver.page_source

# Parse the HTML content of the page
# soup = BeautifulSoup(html_content, 'html.parser')
# r = soup.find_all(name="div", class_="update-components-text")
# r = soup.find_all(name="div", class_="scaffold-finite-scroll")
# for post in r:
#     print(post.getText())
# todo 1: try to scroll down then scrap
for i in range(0, 300):
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
# print(type(soup.select(selector=".feed-shared-update-v2")))
# print(soup.select(selector=".feed-shared-update-v2__description")[1])

# posts_content_list = driver.find_elements(By.XPATH, "//span[@class='break-words']/span/span[@dir='ltr']")
# todo : copy full path xpath
# posts_content_list = driver.find_elements(By.XPATH, "//main/div[4]/div/div/div/div/div/div[5]/div/div/div/span/span/span[@dir='ltr']")
# posts_content_list = driver.find_elements(By.XPATH, "//main/div[4]/div/div[1]/div")

posts_content_list = driver.find_elements(By.XPATH, "//div[@data-id]")
filtered_posts = {}


def calculate_weight(keywords_list, dict_key):
    for key in keywords_list:
        if key in normalized_post:
            post_dict[dict_key] += 1


prerequested_keywords = ["python", "data", "jupyter", "analyst", "java"]
exclude_keywords = ["B2B", "marketing", "paid", "trial", "stage", "pfe", "soutenance", "erreur", "famille", "amis",
                    "family", "friends", "soutien", "thesis", "gratitude", "grateful",
                    "supervisor", "support", "at least 4", "at least 5", "at least 6", "at least 7", "at least 8",
                    "8 ans", "7 ans", "6 ans", "5 ans", "4 ans", "8ans", "7ans", "6ans", "5ans", "4ans",
                     "8 year", "7 year", "6 year", "5 year", "4 year", "8year", "7year", "6year", "5year", "4year", "préten",
                   "conseil", "les recruteurs", "immense", "suis ravi", "finance", "business", "pleased to", "profonde"]
is_hiring = ["@", "resume", "cv", "recrutement", "join", "rejoin", "recrute", "ressource", "recruit", "hiring", "hire", "job", "work",
             "hr", "talent", "aquisition", "human", "fresher", "jobopening", "opening", "seek",
             "postule", "challenge", "role", "reach", "contrat", "cdi", "cdd", "freelance",
             "application", "condidature", "resource", "humain", "recherche", "look", "offre", "offer", "opening",
             "employment", "opportunit", "vacanc", "career", "position", "emploi", "poste", "carriere", "embauche"]
is_first_priority = ["junior", "jr", "jnr", "fraichement", "graduated", "entry"]

python_keywords = ["beautifulsoup", "bs4", "playwright", "openpyxl", "scraping", "scrap", "pandas",
                   "pycharm", "tkinter", "engineer", "css", "html", "ingenieur", "django", "flask", "data",
                   "jupyter", "analysis"]
java_keywords = ["spring", "boot", "angular", "hibernate", "hql"]
common_keywords = ["excel", "backend", "back end", "back-end", "frontend", "front end", "front-end", "selenium", "web", "api", "security", "keycloack", "developer", "full",
                   "stack", "developpeur", "git", "program", "automation", "automatisation", "data", "données",
                   "software", "scrum", "agile", "oracle", "twilio", "tequila", "sql", "docker", "ci", "cd", "qa"]
for post in posts_content_list:
    # print(post)
    # print(post.text)
    # print(post.get_attribute("data-id"))
    # https://www.linkedin.com/feed/update/urn:li:activity:7119641355227668481/

    # filtered_posts = {"python": {"count": 0, "posts": [{"prerequested_title": "", "hiring_weight": 0,
    #                                                     "priority_weight": 0, "python_weight": 0,
    #                                                     "java_weight": 0,
    #                                                     "common_weight": 0, "post_url": ""}
    #                                                    ]},
    #                   "java": {"count": 0,
    #                            "posts": [{"prerequested_title": "", "hiring_weight": 0, "priority_weight": 0,
    #                                       "python_weight": 0, "java_weight": 0, "common_weight": 0,
    #                                       "post_url": ""}]},
    #                   "network": {"count": 0, "posts": [{"prerequested_title": "", "hiring_weight": 0,
    #                                                      "priority_weight": 0, "python_weight": 0,
    #                                                      "java_weight": 0,
    #                                                      "common_weight": 0, "post_url": ""}]}
    #                   }

    # todo: make formula for keywords ex: keywords1 * 1 and keywords10 * 10 and keywords100 * 100...
    #  to be able to order them


    # todo: normalize the post.text (make it lower and replace é with e...
    normalized_post = post.text.lower().replace("é", "e").replace("è", "e").replace("ù", "u").replace("û", "u") \
        .replace("î", "i")
    for prerequested_keyword in prerequested_keywords:
        post_dict = {"hiring_weight": 0, "priority_weight": 0, "python_weight": 0,
                     "java_weight": 0, "common_weight": 0, "post_url": ""}
        if prerequested_keyword in normalized_post:

            # print(f"https://www.linkedin.com/feed/update/{post.get_attribute('data-id')}/")

            calculate_weight(is_hiring, "hiring_weight")
            calculate_weight(is_first_priority, "priority_weight")
            calculate_weight(python_keywords, "python_weight")
            calculate_weight(java_keywords, "java_weight")
            calculate_weight(common_keywords, "common_weight")
            post_dict["post_url"] = f"https://www.linkedin.com/feed/update/{post.get_attribute('data-id')}/"
            try:
                filtered_posts[prerequested_keyword]["posts"].append(post_dict)
            except KeyError:
                filtered_posts[prerequested_keyword] = {"posts": [post_dict]}

pprint(filtered_posts)

# todo 2: filter by last 24 hours for better results

    # todo later important: srap data using vpn (try using the opera browser or use another windows vpns) to get more
    #  content
