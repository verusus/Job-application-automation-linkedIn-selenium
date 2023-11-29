import pprint

from linkedin_api import Linkedin

# # Authenticate using any Linkedin account credentials
# api = Linkedin('salhiabdelhamid01@gmail.com', 'TEST@TEST11')

# # GET a profile
# profile = api.get_profile('abdelhamid-salhi-71b247294')
# pprint.pprint(profile)
# # # GET a profiles contact info
# contact_info = api.get_profile_contact_info('abdelhamid-salhi-71b247294')
# pprint.pprint(contact_info)


# # # GET 1st degree connections of a given profile
# connections = api.get_profile_connections('ACoAAEc6D0cBd8gPiOcXekZrdqk1PVshb6KXOYg')
# pprint.pprint(connections)

# posts = api.get_feed_posts(limit=10, offset=0, exclude_promoted_posts=True)
# print(posts)


# contact_infos = api.get_profile_contact_info(public_id="khadija-bouderk-2a59b7161")
# pprint.pprint(contact_infos)


# search = api.search({"python developer"}, limit=-1, offset=0)
# pprint.pprint(search)


# companies = api.search_companies(keywords=["python developer"])
# pprint.pprint(companies)


# jobs = api.search_jobs(keywords="python developer", companies=None, experience=["2", "3", "4"],
#                        job_type=["F", "C", "P", "T", "O"], job_title=None, industries=None, location_name="Casablanca",
#                        remote=None, listed_at=86400, distance=300, limit=-1, offset=0)
# # pprint.pprint(jobs)
# print(len(jobs))
#
#
# def does_fit(job):
#     if "python" in job["title"].lower() or "scrap" in job["title"].lower():
#         return True
#     elif "developpeur" in job["title"].lower().replace("é", "e") or "developer" in job["title"].lower() \
#             and "data" in job["title"].lower():
#         return True
#     else:
#         return False
#
#
# filtered_titles = list(filter(does_fit, jobs))
# pprint.pprint(filtered_titles)
#
# print(len(filtered_titles))

# todo later 2: use the following code to send messages to hr and if status was not true, note the that in the csv file to try later
# message_status = api.add_connection("abdelhamid-salhi-28037a16b", message='hello I hope you will accept my invitation. thanks')
# pprint.pprint(message_status)

# people = api.search_people(keywords="mohamed")
# pprint.pprint(people)


from linkedin_scraper import Person, actions
from selenium import webdriver
driver = webdriver.Chrome()

email = "salhiabdelhamid01@gmail.com"
password = "TEST@TEST11"
actions.login(driver, email, password) # if email and password isnt given, it'll prompt in terminal
person = Person("https://www.linkedin.com/in/abdelhamid-salhi-71b247294", driver=driver)

print(person.about)















