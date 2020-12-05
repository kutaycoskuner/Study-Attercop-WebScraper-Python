# Attercop
# ==== Libraries
# :: webdriver
from selenium import webdriver
# # :: Requests allows you to send HTTP/1.1 requests
# import requests
# # :: Beautiful Soup is a library that makes it easy to scrape information from web pages.
# from bs4 import BeautifulSoup
# :: [standard] creating folders / change directories
import os 
# :: [standard] regex
import re

# ==== Functions
# :: Fixes the links
def textFixerArtstation(url):   
    print('')

def staticImageSpider(link, folder_name):
    # # :: dosyayi yarat
    # try: 
    #     os.mkdir(os.path.join(os.getcwd(), folder_name))
    # except: 
    #     print('error on file')
    #     # return
    # # :: dosyaya gec
    # os.chdir(os.path.join(os.getcwd(), folder_name))

    # :: html reqquest yap
    request = requests.get(link)
    soup = BeautifulSoup(request.text, 'html.parser').encode("utf-8")
    with open("Downloads/index.html","w") as file: # :: r for read
        file.write(str(request.text.encode("utf-8")))
        print('output file is ready')
    # images = soup.find_all('img')

    # for iterator, image in enumerate(images, start=1):
    #     name = 'a'
    #     link = image['src']
    #     with open(str(iterator) + '.png', 'wb') as file:
    #         item = requests.get(link)
    #         file.write(item.content)
    #         print('Writing ', name)

    # print('action completed by writing ' + str(len(images)) + ' items')
    #     # print(image['src'])

def dynamicImageSpider(link, folder_name):
    print('yay')



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
            # //img
            item_links.append(source.get_attribute('src'))
        for num, link in enumerate(item_links):
            print(num, link)
        print('action completed for total', len(items), 'items')

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
        