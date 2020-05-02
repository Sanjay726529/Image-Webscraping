"""
This app will scrape the choosen key word images from google search.

- This can be used to scrape images for building machine-learning/deep-learning models
- This will use flask web framework to display the scraped images

"""

# imports
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
from pathlib import Path
from glob import glob
import os
from Search.search import srch
from ImageScrapper.imagescrapper import imgscrp



# initialize the flask app
app = Flask(__name__)

# home page
@app.route("/")
@cross_origin()
def home():
    return render_template('index.html')

# display images
@app.route("/showimages")
@cross_origin()
def show_images():
    image_list = [ file for file in os.listdir('static') if file.endswith(".png") or file.endswith(".jpg") ]


    try:
        if len(image_list):
            return  render_template('displayimages.html', scrapped_images=image_list)

        else:
            print("No images are available")
            return render_template('fail.html')
    except Exception as e:
        print("No images found, Try another keyword search")
        return render_template('fail.html')

# search images
@app.route("/searchImages", methods=['GET', 'POST'])
def search_images():
    if request.method == 'POST':
        search_keyword = request.form['keyword']

        imagescrapperutil = srch()  ## Instantiate a object for ScrapperImage Class
        imagescrapper = imgscrp()
        list_images = [ file for file in os.listdir('static') if file.endswith(".png") or file.endswith(".jpg") ]
        imagescrapper.delete_downloaded_images(list_images)  ## Delete the old images before search

        image_name = search_keyword.replace(" ", "+")


        lst_images = imagescrapperutil.downloadimages(search_keyword)

        return show_images()  # redirect the control to the show images method
    else:
        print("unknown keyword")
        return show_images() # redirect the control to the show images method

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8088)

