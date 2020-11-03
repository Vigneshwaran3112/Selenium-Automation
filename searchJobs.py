#packages are imported
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd
import openpyxl

data = []

# setup chrome webdriver
driver = webdriver.Chrome(ChromeDriverManager().install())

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


search = driver.find_element_by_xpath('//input[@class="search-global-typeahead__input always-show-placeholder"]')
search.send_keys('Enter jobs you want'+Keys.RETURN) #Enter to search jobs you want
time.sleep(5)

#click to close ad toggle button
toggle = driver.find_element_by_xpath('/html/body/div[8]/div/div/div/div/button').click()
time.sleep(3)

#click easyjob botton
easyjob = driver.find_element_by_xpath('//span[text()="LinkedIn Features"]').click()
time.sleep(2)

#click easyjob check box
check = driver.find_element_by_xpath('//span[text()="Easy Apply"]').click()
time.sleep(1)

#click apply button
apply = driver.find_element_by_xpath('/html/body/div[9]/div[4]/div/div[1]/header/div/div/div[2]/div/div/div/ul/li[1]/form/div/fieldset/div/div/div/button[2]').click()
time.sleep(7)

#scrap job published date and time for each searched jobs
time = driver.find_elements_by_xpath('//li[starts-with(@id,"ember")]/div/div[2]/ul/li[1]/time')
time = [l.get_attribute("datetime") for l in time]
data.extend(time)

#scrap job title for each searched jobs
jobtitle = driver.find_elements_by_xpath('//li[starts-with(@id,"ember")]/div/div/div/h3/a')
jobtitle = [l.text for l in jobtitle]
data.extend(jobtitle)

#scrap job company name for each searched jobs
companyname = driver.find_elements_by_xpath('//li[starts-with(@id,"ember")]/div/div/div/div/a')
companyname = [l.text for l in companyname]
data.extend(companyname)

#scrap job location for each searched jobs
location = driver.find_elements_by_xpath('//li[starts-with(@id,"ember")]/div/div/div/span')
location = [l.text for l in location]
data.extend(location)

#scrap job link for each searched jobs
joblink = driver.find_elements_by_xpath('//li[starts-with(@id,"ember")]/div/div/div/h3/a')
joblink = [l.get_attribute('href') for l in joblink]
data.extend(joblink)

skillmatch = driver.find_elements_by_xpath('//li[starts-with(@id,"ember")]/div/div[2]/div/div/div/div')
skillmatch = [l.text for l in skillmatch]

df = pd.DataFrame()

#convert list into dataframe format
df['Date'] = time
df['Job Title'] = jobtitle
df['Company Name'] = companyname
df['Location'] = location
df['Job Apply Link'] = joblink

#filename
filename = 'LinkedInJobs.xlsx'

#convert dataframe to excel format
df.to_excel(filename, sheet_name='new_sheet', index = False)

'''
with pd.ExcelWriter(filename, engine='openpyxl') as writer:
    writer.book = openpyxl.load_workbook(filename)
    df.to_excel(writer, sheet_name='new_sheet', index=False)
    writer.save()
    '''
