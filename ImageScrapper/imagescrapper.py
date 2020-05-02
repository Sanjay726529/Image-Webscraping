"""
This module will allow you to create an instance with key
word and return all the URL's for the keyword images.
"""

#imports
from bs4 import BeautifulSoup as bs
import requests
import urllib
import os
import json

class imgscrp():

    # url builder
    def buildURL(self, keyw):
        return f"https://www.bing.com/images/search?q={keyw.replace(' ','+')}&FORM=HDRSC2"
        #return "https://www.google.co.in/search?q=" + keyw.replace(" ","+") + "&source=lnms&tbm=isch"

    # dowload htmlfile
    def download_html_file(self, url, header):
        html = requests.get(url, headers=header)
        parsed = bs(html.content, 'html.parser')

        return parsed

    # get image url's
    def parse_image_urls(self, raw_html):
        image_url_list = []
        for a_tags in raw_html.find_all("a", {'class':'iusc'}):
            print(a_tags)
            json_data = json.load(a_tags.m)
            print(json_data)
            image_url_list.append(json_data['murl'])

        return image_url_list

    def downloadImagesFromURL(imageUrlList, image_name, header):
        masterListOfImages = []
        count = 0

        ###print images
        imageFiles = []
        imageTypes = []
        image_counter = 0
        for i, (img, Type) in enumerate(imageUrlList):
            try:
                if (count > 5):
                    break
                else:
                    count = count + 1
                req = urllib.request.Request(img, headers=header)
                try:
                    urllib.request.urlretrieve(img, "./static/" + image_name + str(image_counter) + ".jpg")
                    image_counter = image_counter + 1
                except Exception as e:
                    print("Image write failed:  ", e)
                    image_counter = image_counter + 1
                respData = urllib.request.urlopen(req)
                raw_img = respData.read()
                # soup = bs(respData, 'html.parser')

                imageFiles.append(raw_img)
                imageTypes.append(Type)

            except Exception as e:
                print("could not load : " + img)
                print(e)
                count = count + 1
        masterListOfImages.append(imageFiles)
        masterListOfImages.append(imageTypes)

        return masterListOfImages

    def delete_downloaded_images(self, list_of_images):
        for self.image in list_of_images:
            try:
                os.remove("./static/" + self.image)
            except Exception as e:
                print('error in deleting:  ', e)
        return 0
