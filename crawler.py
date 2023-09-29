from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

# create a new instance of the Firefox driver
driver = webdriver.Firefox()

# navigate to Google Scholar
driver.get('https://scholar.google.com/')

# find the search box and enter the query
search_box = driver.find_element(By.NAME, 'q')
query = input()
search_box.send_keys(query)
search_box.send_keys(Keys.RETURN)

# find the first article with clickable element group
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'gs_a'))
)

found_articles_info_elements = driver.find_elements(By.CLASS_NAME, 'gs_a')
for element in found_articles_info_elements:
    try:
        first_clickable_element = element.find_element(By.TAG_NAME, 'a')
        first_clickable_element.click()
        break
    except:
        None

time.sleep(1)

# author data
author_name = ''
author_uni = ''
author_research_interests = []

author_info_element = driver.find_element(By.ID, 'gsc_prf_i')
author_name = author_info_element.find_element(By.ID, 'gsc_prf_in').text
author_uni = author_info_element.find_element(
    By.CLASS_NAME, 'gsc_prf_ila').text
author_research_interests_element = driver.find_element(By.ID, 'gsc_prf_int')
research_interest_elements = author_research_interests_element.find_elements(
    By.TAG_NAME, 'a')

for element in research_interest_elements:
    author_research_interests.append(element.text)

print(author_name)
print(author_uni)
print(author_research_interests)

show_more_button = driver.find_element(By.ID, 'gsc_bpf_more')

while (show_more_button.get_attribute('disabled') == None):
    show_more_button = driver.find_element(By.ID, 'gsc_bpf_more')
    show_more_button.click()
    time.sleep(1)

# author's articles data
articles_dictionary_list = []
articles = driver.find_elements(By.CLASS_NAME, 'gsc_a_tr')
print('number of articles : ' + str(len(articles)))
article_driver = webdriver.Firefox()
try:
    for article in articles:
        title = ''
        cited_by = ''
        year = ''
        authors = ''
        publication_date = ''
        journal = ''
        volume = ''
        issue = ''
        pages = ''
        description = ''

        article_link_element = article.find_element(By.TAG_NAME, 'a')
        title = article_link_element.text

        article_link_element = article.find_element(By.CLASS_NAME, 'gsc_a_c')
        cited_by = article_link_element.text

        article_year_element = article.find_element(By.CLASS_NAME, 'gsc_a_y')
        year = article_year_element.text

        article_link = article_link_element.get_attribute('href')
        time.sleep(2)
        article_driver.get(article_link)

        article_detail_table_element = article_driver.find_element(
            By.ID, 'gsc_oci_table')
        article_detail_elements = article_detail_table_element.find_elements(
            By.CLASS_NAME, 'gs_scl')

        for element in article_detail_elements:
            element_field_name = element.find_element(
                By.CLASS_NAME, 'gsc_oci_field')
            if element_field_name.text == 'Authors':
                authors = element.find_element(
                    By.CLASS_NAME, 'gsc_oci_value').text
            if element_field_name.text == 'Publication date':
                publication_date = element.find_element(
                    By.CLASS_NAME, 'gsc_oci_value').text
            if element_field_name.text == 'Journal':
                journal = element.find_element(
                    By.CLASS_NAME, 'gsc_oci_value').text
            if element_field_name.text == 'Volume':
                volume = element.find_element(
                    By.CLASS_NAME, 'gsc_oci_value').text
            if element_field_name.text == 'Issue':
                issue = element.find_element(
                    By.CLASS_NAME, 'gsc_oci_value').text
            if element_field_name.text == 'Pages':
                pages = element.find_element(
                    By.CLASS_NAME, 'gsc_oci_value').text
            if element_field_name.text == 'Description':
                description = element.find_element(
                    By.CLASS_NAME, 'gsc_oci_value').text

        articles_dictionary_list.append({
            'Title': title,
            'Cited By': cited_by,
            'Year': year,
            'Authors': authors,
            'Publication Date': publication_date,
            'Journal': journal,
            'Volume': volume,
            'Issue': issue,
            'Pages': pages,
            'Description': description
        })

        print('Crawled: ' + title)

except:
    df = pd.DataFrame.from_records(articles_dictionary_list)
    df.to_csv('./cancer.csv')

df = pd.DataFrame.from_records(articles_dictionary_list)
df.to_csv('./cancer.csv')

# close the browser
article_driver.quit()
driver.quit()
