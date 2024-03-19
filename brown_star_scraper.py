from bs4 import BeautifulSoup as bs
import pandas as pd
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/List_of_brown_dwarfs")
time.sleep(40)
# html = driver.page_source
# soup = BeautifulSoup(html, "html.parser")
scraped_data = []

soup = bs(driver.page_source, "html.parser")
brown_star_table = soup.find_all("table", {"class":"wikitable sortable jquery-tablesorter"})

temp_list = []
table_rows = brown_star_table[1].find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)
    
star_names = []
distance = []
mass = []
radius = []

print(temp_list)
# stars_data = []

for r in range(1, len(temp_list)):

    star_names.append(temp_list[r][0])
    distance.append(temp_list[r][5])
    mass.append(temp_list[r][8])
    radius.append(temp_list[r][9])
    
    # required_data = [star_names, distance, mass, radius]
    # stars_data.append(required_data) 

# headers =  ['Star_Name', 'Distance', 'Mass', 'Radius']
# df2 = pd.DataFrame(stars_data, columns=headers)
# df2.to_csv('brown_dwarf_stars.csv', index=True, index_label="id")

headers = ['Star_Name','Distance','Mass','Radius']  
df2 = pd.DataFrame(list(zip(star_names,distance,mass,radius,)),columns=['Star_Name','Distance','Mass','Radius'])
print(df2)

df2.to_csv('brown_dwarf_stars.csv', index=True, index_label="id")