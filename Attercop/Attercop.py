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
# :: End Session
def endSession(driver):
    driver.quit()
    quit()

# :: Remove Duplicates
def removeDuplicates(item_links):
    unique_links = list(dict.fromkeys(item_links))
    return unique_links

# :: # :: change folder
def changeDirectory(folder_name):
    try:
        os.mkdir(os.path.join(os.getcwd(), folder_name))
    except:
        print('folder already exists')
    os.chdir(os.path.join(os.getcwd(), folder_name))

# :: Fixes the links
def adapterArtstation(driver):   
    items = driver.find_elements_by_class_name('project-image')
    item_links = []
    for item in items:
        source = item.find_element_by_xpath(".//img[@class='image']")
        item_links.append(source.get_attribute('src'))

    item_links = removeDuplicates(item_links)

    # :: smallari large ile degistir
    for ii, item in enumerate(item_links):
        item_links[ii] = item.replace('smaller_square','large')

    return item_links

# :: scrape
def dynamicImageSpider(item_links):
    for num, link in enumerate(item_links, start=1):
        with open(str(num) + '.jpg', "wb") as file:
            image = requests.get(link)
            file.write(image.content)
            print(num, link)
    print('action completed for total', len(item_links), 'items')



# ==== Main
def Main():
    # ==== Setup
    # :: Parameters: edit these
    link = 'https://www.artstation.com/kutay_coskuner/albums/all'
    scraper_type = 'image' # image, text
    folder_name = 'Downloads'

    # :: Selenium
    driver = webdriver.Chrome('C:\WebDrivers\chromedriver.exe')
    driver.get(link)

    # :: Change folder
    changeDirectory(folder_name)

    # ==== Select Scraper
    # :: differential link process (adapter)
    searchResult = re.search('artstation', link, re.M|re.I)
    if searchResult:
        item_links = adapterArtstation(driver)
    else:
        print('given url has no appropriate adapter for scraping')
        return

    # :: if no extraction links stop
    if item_links == None: 
        print('no item links are found')
        endSession(driver)

    # ==== Start Scraping
    # :: dynamic image scraper
    if scraper_type == 'image':
        dynamicImageSpider(item_links)
    elif scraper_type == 'text':
        print('text scraper is not yet implemented')
    else:
        print('no spider is scripted for this action')

    # ==== End Session
    endSession(driver)

# ==== Initialization
if __name__ == "__main__":
    Main()
        