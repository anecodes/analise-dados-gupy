import requests, time, csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from time import sleep

file = csv.writer(open('job-data.csv', 'a'))
file.writerow(['Empresa', 'Cargo', 'Localidade', 'Data']) 

browser = webdriver.Firefox()

browser.get("https://portal.gupy.io")

input_place = browser.find_element(By.XPATH, '//*[@id="react-aria-3"]')
input_place.send_keys("Dados")
click_place = browser.find_element(By.XPATH, '//*[@id="main-content"]/div/div/div[2]/div/div/div/div/div[2]/button')
click_place.click()

sleep(2)

scrolls = 40
while True:
    scrolls -= 1
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(3)
    if scrolls < 0:
        break

sleep(2)

page_content = browser.page_source
soup = BeautifulSoup(page_content, "html.parser")

imgs = soup.findAll('img')
for match in imgs:
    match.decompose()

svg = soup.findAll('svg')
for match in svg:
    match.decompose()

job_boxes = soup.find("ul", class_="zVzmE")
job_boxes_items = job_boxes.find_all('li')

for jobs in job_boxes_items:
    company = jobs.find("p", class_="cQyvth").text
    title = jobs.find("h2", class_="XNNQK").text
    location = jobs.find("span", class_="cezNaf").text
    date = jobs.find("p", class_="inqtnx").text
    
    for i in jobs:
        file.writerow([company, title, location, date])

browser.quit()
