from bs4 import BeautifulSoup
import pandas as pd
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/List_of_brightest_stars")
time.sleep(10)
# html = driver.page_source
# soup = BeautifulSoup(html, "html.parser")
scraped_data = []

def scrape():
    soup = BeautifulSoup(driver.page_source, "html.parser")

    bright_star_table = soup.find("table", attrs={"class", "wikitable sortable sticky-header jquery-tablesorter"})
    table_body = bright_star_table.find('tbody')
    table_rows = table_body.find_all('tr')

    for row in table_rows:
        table_cols = row.find_all('td')
        print(table_cols)
        temp_list = []

        for col_data in table_cols:
            col_data_text = col_data.text
            data = col_data_text.strip()
            print(data)
            temp_list.append(data)
        scraped_data.append(temp_list)

scrape()
stars_data = []
for d in range(0,len(scraped_data)):
    star_names = scraped_data[d][1]
    distance = scraped_data[d][3]
    mass = scraped_data[d][5]
    radius = scraped_data[d][6]
    luminosity = scraped_data[d][7]

    required_data = [star_names, distance, mass, radius, luminosity]
    stars_data.append(required_data)    

headers = ['Star_Name', 'Distance', 'Mass', 'Radius', 'Luminosity']
star_df_1 = pd.DataFrame(stars_data, columns=headers)
star_df_1.to_csv('scraped_data.csv',index=True, index_label="id")
