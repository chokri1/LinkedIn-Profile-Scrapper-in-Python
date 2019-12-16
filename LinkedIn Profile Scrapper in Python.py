#importation de BeautifulSoup et webdriver
from bs4 import BeautifulSoup
from selenium import webdriver


#automatise login
browser = webdriver.Chrome('WebDriver/chromedriver.exe')
browser.get('https://www.linkedin.com/uas/login')
file = open('loginInfo.txt')
lines = file.readlines()
username = lines[0]
password = lines[1]
elementID = browser.find_element_by_id('username')
elementID.send_keys(username)
elementID = browser.find_element_by_id('password')
elementID.send_keys(password)
elementID.submit()

#getting profile link
link = 'https://www.linkedin.com/in/ernestmistica/'
browser.get(link)
#extraire les informations
src = browser.page_source
soup = BeautifulSoup(src, 'lxml')

name_div = soup.find('div', {'class': 'flex-1 mr5'})
name_loc = name_div.find_all('ul')
name = name_loc[0].find('li').get_text().strip()
loc = name_loc[1].find('li').get_text().strip()
profile_title = name_div.find('h2').get_text().strip()
connection = name_loc[1].find_all('li')
connection = connection[1].get_text().strip()
#créer une liste de données
info = []
info.append(link)
info.append(name)
info.append(profile_title)
info.append(loc)
info.append(connection)
#affichage de liste(info)
print(info)

quit()