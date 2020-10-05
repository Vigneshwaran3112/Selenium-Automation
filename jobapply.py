#packages imported
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd
import openpyxl

data = []
c = 0

# setup webdriver
webdriver_selected = input("Type 1 to use Chrome or 2 to use Firefox:")
if webdriver_selected == "1":
    driver = webdriver.Chrome()
else:
    driver = webdriver.Firefox()

#maximize the chrome brower window 
driver.maximize_window()

#redirect linkedin webpage
driver.get("https://www.linkedin.com")

#click signin button
sign_in = driver.find_element_by_class_name('nav__button-secondary')
sign_in.click()
time.sleep(2)

#enter user details
username = driver.find_element_by_name('session_key')
username.send_keys('LinkedIn id') # Enter Id you want to login linkedin account

password = driver.find_element_by_name('session_password')
password.send_keys('LinkedIn password') # Enter password
password.send_keys(Keys.RETURN)
time.sleep(5)



file = 'LinkedInJobs.xlsx' #to create filename for scraped data to store

df = pd.read_excel(file, sheet_name='new_sheet', usecols="E")#read excel data

joblinks = df.values.tolist()

for i in range(0,7):
    data.extend(joblinks[i])

for link in data:
    driver.get(link)
    apply = driver.find_element_by_xpath('//button[@class="jobs-apply-button artdeco-button artdeco-button--3 artdeco-button--primary ember-view"]').click()
    time.sleep(2)
    c = c + 1
    
    try:

        number = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div/form/div/div[1]/div[3]/div[2]/div/div/input').send_keys('your mobile number')#enter number

        try:

            nxt = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div/form/footer/div[2]/button').click()
            time.sleep(2)

            upload = driver.find_element_by_name('file').send_keys('C:/Users/... your resume file location path')#enter your resume file location path from system
            time.sleep(2)

            nxt2 = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div/form/footer/div[2]/button[2]').click()
            time.sleep(2)

        except:

            try:
                upload = driver.find_element_by_name('file').send_keys('C:/Users/... your resume file location path')#enter your resume file location path from system
                time.sleep(2)
            except:
                continue
    except:
        continue


print('\n{} jobs are applied...'.format(c))
