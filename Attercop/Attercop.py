# Attercop
# ==== Libraries
# == Outer Lib
# ::webdriver
from selenium import webdriver
# :: [standard] creating folders / change directories
import os 
# :: [standard] regex
import re

# == My Modules
# :: polymorphic adapter
import Classes.LinkFactory as website
import Classes.ScraperFactory as scraper

# ==== Functions
# == Collect Parameters
def askParameters():
    link = input('please insert a link you want to scrape from: ')
    scraper_type = input('please define scrape type [image | text]: ')
    file_name = None
    if scraper_type != 'image' and scraper_type != 'text':
        print('you have given undefined scrape type')
        return
    elif scraper_type == 'text':
        file_name = input('please insert a file name to save: ')
    # :: Return
    param = [link, scraper_type, file_name]
    return param

# :: change folder
def changeDirectory(folder_name):
    try:
        os.mkdir(os.path.join(os.getcwd(), folder_name))
    except:
        print('folder already exists')
    os.chdir(os.path.join(os.getcwd(), folder_name)) 

# :: End Session
def endSession(driver):
    driver.quit()
    quit()

# ==== Main
def Main():
    # ==== Setup
    # :: testers
    # https://www.artstation.com/kutay_coskuner/albums/all
    # https://www.artstation.com/kutay_coskuner/likes
    # https://github.com/kutaycoskuner?tab=repositories
    # == Parameters edit these
    link = 'https://github.com/kutaycoskuner?tab=repositories'
    scraper_type = 'text' # :: [disc] image, text
    scrape_type = 'dynamic' # :: [disc] dynamic, static
    folder_name = 'Downloads'
    file_name = 'test.txt'

    # == Get parameters from user
    # params = askParameters()
    # if params[0] : link = params[0]
    # if params[1] : scraper_type = params[1]
    # if params[2] : file_name = params[2]

    # :: string manipulation on link to extract site name
    # test
    # keys = link.split('.')
    # print(keys[1])
    # for key in keys:
    #     key = key.title()
    # return
    # test end

    # :: Change folder
    changeDirectory(folder_name)

    # == Selenium
    if scrape_type == 'dynamic':
        options = webdriver.ChromeOptions() 
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        driver = webdriver.Chrome(options=options, executable_path='C:\WebDrivers\chromedriver.exe')
        driver.get(link)

    # ==== Select Scraper: differential link process [selection]
    if re.search('artstation', link, re.M|re.I):
        data = website.Artstation(driver)
    elif re.search('github', link, re.M|re.I):
        data = website.Github(driver)
    elif re.search('pinterest', link, re.M|re.I):
        data = website.Pinterest(driver)
    else:
        print('given url has no appropriate adapter for scraping')
        return

    data = data.elaborateData()

    # == if no defined adapter or link stop
    if data == None: 
        print('no data are found')
        endSession(driver)
        
    # ==== Start Scraping [selection]
    # == dynamic image scraper
    spider = None
    if scraper_type == 'image':
        spider = scraper.DynamicImageSpider()
    elif scraper_type == 'text':
        spider = scraper.DynamicTextSpider()
    else:
        print('no spider is scripted for this action')

    if spider:
        spider.scrapeData(data, file_name)

    # ==== End Session
    endSession(driver)

# ==== Initialization
if __name__ == "__main__":
    Main()
        