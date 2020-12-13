# Polymorphic Adaptors
# ==== Libraries
from selenium.webdriver.common.by import By

# ==== Functions
def removeDuplicates(data):
        unique_links = list(dict.fromkeys(data))
        return unique_links

# == Super Class
class LinkFactory:
    def __init__(self, driver):
        self.driver = driver

    # == Abstract Methods
    def elaborateData(self):
        raise NotImplementedError("Subclass must implement abstract method")

# == Sub Classes
class Artstation(LinkFactory):
    def __init__(self, driver):
        super().__init__(driver) # :: you can run super class methods as this

    def elaborateData(self):
        items = self.driver.find_elements_by_class_name('project-image')
        data = []
        # :: projelere ait linleri topla
        for link in items:
            data.append(link.get_attribute('href'))
        # :: duplicate temizle
        data = removeDuplicates(data)
        individual_links = []
        # :: sayfalari teker teker gezerek tekil linkleri topla
        for link in data:
            self.driver.get(link)
            images = self.driver.find_elements_by_class_name('artwork-image')
            for image in images:
                src = image.find_element_by_xpath(".//picture/img")
                adress = src.get_attribute('src').rstrip("1234567890?")
                individual_links.append(adress)
        # :: veriyi esle ve temizle
        data = individual_links
        data = removeDuplicates(data)
        # :: temiz veriyi scrape icin gonder
        return data

class Github(LinkFactory):
    def __init__(self, driver):
        super().__init__(driver) # :: you can run super class methods as this

    def elaborateData(self):
        items = self.driver.find_elements(By.XPATH, '//*[@id="user-repositories-list"]/ul/li')
        data = []
        for num, item in enumerate(items, start=1):
            xpath = './/*[@id="user-repositories-list"]/ul/li[' + str(num) +']/div[1]/div[1]/h3/a'
            source = self.driver.find_element(By.XPATH, xpath)
            data.append(source.text)
        return sorted(data)

class Pinterest(LinkFactory):
    def __init__(self, driver):
        super().__init__(driver) # :: you can run super class methods as this

    def elaborateData(self):
        data = []
        individual_links = []
        # :: specified 
        items = self.driver.find_elements_by_class_name('Collection-Item')
        # :: sayfalari teker teker gezerek tekil linkleri topla
        for num, item in enumerate(items, start=1):
            image = self.driver.find_element_by_xpath('//div['+ str(num) +']/div/div[1]/div[1]/a/img')
            links = image.get_attribute('srcset').split(', ')
            for num2, link in enumerate(links): 
                if num2 == len(links)-1:
                    individual_links.append(link)
        # :: veriyi esle ve temizle
        data = individual_links
        data = removeDuplicates(data)
        # :: specified end
        # :: temiz veriyi scrape icin gonder
        return sorted(data)

# ==== Discarded
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


