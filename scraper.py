import requests
from bs4 import BeautifulSoup
import csv

header = ["title","company","skills"]
jobs = []


URL = input("Enter a url (blank to end): ")
while(URL != ""):
    job_data = []
    page = requests.get(URL)

    #print(page.text)

    soup = BeautifulSoup(page.content, "html.parser")


    header_tags = soup.find_all('h1')

    title = header_tags[0].text
    company = soup.find(class_="company").text
    skills = soup.find_all(class_="skills")
    skills = soup.find_all("li")

    skill_list = ""
    i = 0
    for skill in skills:
        skill_list += skill.text.strip()
        skill_list += ";"
    skill_list = skill_list[:-1]
    
    job_data.append(title)
    job_data.append(company)
    job_data.append(skill_list)

    jobs.append(job_data)
    URL = input("Enter a url (blank to end): ")


with open("jobs.csv", mode="w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(header)
    writer.writerows(jobs)

