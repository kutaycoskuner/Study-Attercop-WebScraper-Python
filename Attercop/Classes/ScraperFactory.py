#
# ==== Libraries
# :: Requests allows you to send HTTP/1.1 requests
import requests
# :: [standard] regex
import re

# ==== Polymorphism
# == Super Class
class ScraperFactory:
    # == Abstract Methods
    def scrapeData(self):
        raise NotImplementedError("Subclass must implement abstract method")

# == Sub Classes
class DynamicImageSpider(ScraperFactory):
    def scrapeData(self, data, file_name):
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

class DynamicTextSpider(ScraperFactory):
    def scrapeData(self, data, file_name):
        with open(file_name, "w") as file:
            for num, item in enumerate(data):
                file.write(item + "\n")
                print(num, item)
        print('action completed for total', len(data), 'items')  
    


