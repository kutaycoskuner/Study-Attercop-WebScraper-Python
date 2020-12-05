# Attercop
# ==== Libraries
# webdriver
from selenium import webdriver
# Requests allows you to send HTTP/1.1 requests
import requests
# [standard] creating folders / change directories
import os 
# [standard] regex
import re

# ==== Functions
# :: Fixes the links
def textFixerArtstation(url):   
    print('')

def staticImageSpider(link, folder_name):
    print('i am static spider')

def dynamicImageSpider(link, folder_name):
    print('i am dynamic spider')



# ==== Main
def Main():
    # ==== Setup
    # :: Parameters: edit these
    link = 'https://www.artstation.com/kutay_coskuner/albums/all'
    folder_name = 'potato'

    # :: Selenium
    driver = webdriver.Chrome('C:\WebDrivers\chromedriver.exe')
    driver.get(link)

    # ==== Select scraper
    # :: differential link process (adapter)
    searchResult = re.search('artstation', link, re.M|re.I)
    if searchResult:
        items = driver.find_elements_by_class_name('project-image')
        item_links = []
        for item in items:
            source = item.find_element_by_xpath(".//img[@class='image']")
            item_links.append(source.get_attribute('src'))

        # :: unique key yap
        item_links = list(dict.fromkeys(item_links))

        # :: scrape
        for num, link in enumerate(item_links, start=1):
            with open(str(num) + '.jpg', "wb") as file:
                modified_link = link.replace('smaller_square','large')
                image = requests.get(modified_link)
                file.write(image.content)
                print(num, modified_link)
        print('action completed for total', len(item_links), 'items')
    else:
        print('given url has no appropriate adapter for scraping')
        return

    # :: Start scraping
    # dynamicImageSpider(link, folder_name)

    # ==== End session
    # :: ensure that no instance is left after finishing the script.
    driver.quit()
    # :: Session end
    quit()

# ==== Initialization
if __name__ == "__main__":
    Main()
        