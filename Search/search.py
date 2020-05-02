"""
This module will help in search, clean and return the images of
the keyword
"""

from ImageScrapper.imagescrapper import imgscrp

class srch():

    def __init__(self):
        pass

    def downloadimages(self, search_word):
        scrape = imgscrp()
        web_url = scrape.buildURL(keyw=search_word)
        header = {'useragent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36 Edg/81.0.416.68'}

        html_data = scrape.download_html_file(web_url, header)
        imageURLList = scrape.parse_image_urls(html_data)
        masterListOfImages = scrape.downloadImagesFromURL(imageURLList, search_word, header)

        return masterListOfImages

