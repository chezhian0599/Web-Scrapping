# importing the necessary libraries
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup

# reading the csv file
data = pd.read_csv("data_file.csv")

#selecting chrome webdriver and storing it in a variable called driver

driver = webdriver.Chrome()

# Creating a for loop to Iterate over the dataframe and scrap the data

for i in range(len(data['URL'])):
    #print(i)
    url = data['URL'][i]
    url_id = data['URL_ID'][i]
    driver.get(url)
    html = driver.page_source
    content = BeautifulSoup(html, 'lxml')
    try:
        title = content.find("h1", {"class": "entry-title"})
        #title = content.find('div', attrs={'class': "entry-title"})
        in_content = content.find("div", {"class": "td-post-content"})
        print(title.get_text())
        print(in_content.get_text())
        
        file = open("%s.txt" %(url_id),"a")
        file.write(title.get_text())
        file.write("\n")
        file.write(in_content.get_text())
        file.write("\n")
        file.write("\n")
        file.close()

    except:
        print("Page Error")
driver.quit()

