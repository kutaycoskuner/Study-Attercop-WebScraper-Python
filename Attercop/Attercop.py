# Attercop
# ==== Libraries
# webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
# bs4 for static scraping
# from bs4 import BeautifulStoneSoup
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
def removeDuplicates(data):
    unique_links = list(dict.fromkeys(data))
    return unique_links

# :: change folder
def changeDirectory(folder_name):
    try:
        os.mkdir(os.path.join(os.getcwd(), folder_name))
    except:
        print('folder already exists')
    os.chdir(os.path.join(os.getcwd(), folder_name))

# == Adapters
def adapterArtstation(driver):   
    items = driver.find_elements_by_class_name('project-image')
    data = []
    # :: projelere ait linleri topla
    for link in items:
        data.append(link.get_attribute('href'))
    # :: duplicate temizle
    data = removeDuplicates(data)
    individual_links = []
    # :: sayfalari teker teker gezerek tekil linkleri topla
    for link in data:
        driver.get(link)
        images = driver.find_elements_by_class_name('artwork-image')
        for image in images:
            src = image.find_element_by_xpath(".//picture/img")
            adress = src.get_attribute('src').rstrip("1234567890?")
            individual_links.append(adress)
    # :: veriyi esle ve temizle
    data = individual_links
    data = removeDuplicates(data)
    # :: temiz veriyi scrape icin gonder
    return data

# def adapterArtstation_discarded(driver):   
#     items = driver.find_elements_by_class_name('project-image')
#     data = []
#     for item in items:
#         source = item.find_element_by_xpath(".//img[@class='image']")
#         data.append(source.get_attribute('src'))

#     data = removeDuplicates(data)

#     # :: smallari large ile degistir
#     for ii, item in enumerate(data):
#         data[ii] = item.replace('smaller_square','large')
#     return data

def adapterGitHub(driver):
    items = driver.find_elements(By.XPATH, '//*[@id="user-repositories-list"]/ul/li')
    data = []
    for num, item in enumerate(items, start=1):
        xpath = './/*[@id="user-repositories-list"]/ul/li[' + str(num) +']/div[1]/div[1]/h3/a'
        source = driver.find_element(By.XPATH, xpath)
        data.append(source.text)
        # print(source.text)
    return sorted(data)

# == Scraper
def dynamicImageSpider(data):
    extension_key = None
    for num, link in enumerate(data, start=1):
        if re.search('.jpg', link, re.M|re.I):
            extension_key = '.jpg'
        elif re.search('.gif', link, re.M|re.I):
            extension_key = '.gif'
        elif re.search('.png', link, re.M|re.I):
            extension_key = '.png'

        if extension_key:     
            with open(str(num) + extension_key, "wb") as file:
                image = requests.get(link)
                file.write(image.content)
                print(num, link)
        else:
            print(num, link, 'could not find appropriate extension for this asset')

    print('action completed for total', len(data), 'items')

def dynamicTextScraper(data, file_name):
    with open(file_name, "w") as file:
        for num, item in enumerate(data):
            file.write(item + "\n")
            print(num, item)
    print('action completed for total', len(data), 'items')   

# ==== Main
def Main():
    # ==== Setup
    # :: testers
    # https://www.artstation.com/kutay_coskuner/albums/all
    # https://www.artstation.com/kutay_coskuner/likes
    # https://github.com/kutaycoskuner?tab=repositories
    # == Parameters edit these
    link = 'https://www.artstation.com/kutay_coskuner/likes'
    scraper_type = 'image' # :: [disc] image, text
    scrape_type = 'dynamic' # :: [disc] dynamic, static
    folder_name = 'Downloads'
    file_name = 'test.txt'

    if scrape_type == 'dynamic':
        # == Selenium
        options = webdriver.ChromeOptions() 
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        driver = webdriver.Chrome(options=options, executable_path='C:\WebDrivers\chromedriver.exe')
        driver.get(link)
    # elif scrape_type == 'static':
    #     # == request + bs4
    #     pri
    #     # request = requests.get(link)
    #     # driver = BeautifulSoup(request.content, 'lxml')

    # :: Change folder
    changeDirectory(folder_name)

    # ==== Select Scraper
    # == differential link process (adapter)
    if re.search('artstation', link, re.M|re.I):
        data = adapterArtstation(driver)
    elif re.search('github', link, re.M|re.I):
        data = adapterGitHub(driver)
    else:
        print('given url has no appropriate adapter for scraping')
        return

    # == if no extraction links stop
    if data == None: 
        print('no data are found')
        endSession(driver)
        
    # ==== Start Scraping
    # == dynamic image scraper
    if scraper_type == 'image':
        dynamicImageSpider(data)
    elif scraper_type == 'text':
        dynamicTextScraper(data, file_name)
    else:
        print('no spider is scripted for this action')

    # ==== End Session
    endSession(driver)

# ==== Initialization
if __name__ == "__main__":
    Main()
        