# # Attercop
# # ==== Libraries
# # :: Requests allows you to send HTTP/1.1 requests
# import requests
# # :: Beautiful Soup is a library that makes it easy to scrape information from web pages.
# from bs4 import BeautifulSoup
# # :: [standard] creating folders / change directories
# import os 
# # :: [standard] regex
# import re

# # ==== Functions
# # :: Fixes the links
# def textFixerArtstation(url):   
#     print('')

# # :: Spider function
# def imageSpider(link, folder_name):
#     # # :: dosyayi yarat
#     # try: 
#     #     os.mkdir(os.path.join(os.getcwd(), folder_name))
#     # except: 
#     #     print('error on file')
#     #     # return
#     # # :: dosyaya gec
#     # os.chdir(os.path.join(os.getcwd(), folder_name))

#     # :: html reqquest yap
#     request = requests.get(link)
#     soup = BeautifulSoup(request.text, 'html.parser').encode("utf-8")
#     with open("Downloads/index.html","w") as file: # :: r for read
#         file.write(str(request.text.encode("utf-8")))
#         print('output file is ready')
#     # images = soup.find_all('img')

#     # for iterator, image in enumerate(images, start=1):
#     #     name = 'a'
#     #     link = image['src']
#     #     with open(str(iterator) + '.png', 'wb') as file:
#     #         item = requests.get(link)
#     #         file.write(item.content)
#     #         print('Writing ', name)

#     # print('action completed by writing ' + str(len(images)) + ' items')
#     #     # print(image['src'])


# # ==== Main
# def Main():
#     # :: Test links
#     # :: Parameters: edit these
#     link = ""
#     folder_name = "potato"

#     #     # :: Process link
#     # searchResult = re.search('artstation', link, re.M|re.I)
#     # if searchResult:
#     #     textFixerArtstation(link)

#     # :: Start scraping
#     imageSpider(link, folder_name)

# # ==== Initialization
# if __name__ == "__main__":
#     Main() 
        