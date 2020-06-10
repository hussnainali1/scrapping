
from bs4 import BeautifulSoup
import pandas as pd
import pymongo
import os
from datetime import datetime
import urllib

import io
import urllib

from pymongo import MongoClient
import requests
import shutil
from PIL import Image
import pytesseract as pt


pt.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

class jobsClass:
    linktt = ""
    file = ""

    def __init__(self, link, file):
        self.linktt = link
        self.file = file

    def mainPro(self):
        fun_response = requests.get(self.linktt)
        fun_data_des = fun_response.text
        fun_soup_des = BeautifulSoup(fun_data_des, 'html.parser')
        fun_main_article = fun_soup_des.find(lambda tag: tag.name == 'body' )
        fun_main_article1 = fun_main_article.find('div', {'id': 'mm-1'})
        fun_main_article2 = fun_main_article.find('id', {'id': 'wrapper'})
        fun_main_article3 = fun_main_article.find('div', {'class': 'container wpjm-container full-width'})
        fun_main_article4 = fun_main_article3.find('article', {'id': 'post-2069'})
        fun_main_article5 = fun_main_article4.find('div', {'class': 'padding-right'})
        fun_main_article6 = fun_main_article5.find('div', {'class': 'job_listings'})
        # print(fun_main_article6)
        fun_main_article8 = fun_main_article6.find('ul' )
        # print(fun_main_article8);


        fun_main_article9 = fun_main_article8.find_all('li' , recursive=False)
        # print(fun_main_article9[1].text.strip());
        i=1
        # print(link)


        dict1={}
        count = 0
        for all_ineer in fun_main_article9:
            print("this is link no = ",i)
            i=i+1
            fun_main_article10 = all_ineer.find('a',)
            # print(fun_main_article10)
            link = fun_main_article10.get('href')#######  New link
            print("the link is ==",link)

            fun_main_article_tiitle_upper = fun_main_article10.find('div', {'class': 'listing-title'})
            fun_main_article_tiitle = fun_main_article_tiitle_upper.find('h4')

            title = fun_main_article_tiitle.text.strip()   ##### news title
            # print(fun_main_article_tiitleb)##### news title

            fun_main_article_logo = fun_main_article10.find('div', {'class': 'listing-logo'})
            fun_main_article_logob = fun_main_article_logo.find('img')

            logo_link=fun_main_article_logob.get("src")###### logo link

            fun_response1 = requests.get(link)
            fun_data_des1 = fun_response1.text
            fun_soup_des1 = BeautifulSoup(fun_data_des1, 'html.parser')
            fun_main_article1bb = fun_soup_des1.find('body')
            fun_main_article1c = fun_main_article1bb.find('div', {'id': 'mm-1'})
            fun_main_article1cc = fun_main_article1bb.find('div', {'class': 'container right-sidebar'})

            fun_main_article1d = fun_main_article1cc.find('div', {'class': 'padding-right'})
            fun_main_article1e = fun_main_article1d.find('div', {'class': 'single_job_listing'})
            fun_main_article1f = fun_main_article1e.find('div', {'class': 'job_description'})
            # print()
            description = fun_main_article1f.text.strip()

            img_apply = fun_main_article1f.find_all('img')
            for aa in img_apply:
                img_apply_link  =  aa.get("src")
            print("1st pass complete")
            # =========================================================================================
            image_url = img_apply_link
            # Open the url image, set stream to True, this will return the stream content.
            resp = requests.get(image_url, stream=True)

            img = Image.open(io.BytesIO(resp.content))
            # applying ocr using pytesseract for python
            text = pt.image_to_string(img)
            print(text)
            text = text.strip()

            # =========================================================================================
            new_dic = {
                "tilte": title,
                "img": logo_link,
                "link": link,
                "discription": description,
                "description_img_link": img_apply_link,
                "description_img_link_data": text

            }
            dict1[count] = new_dic
            count = count + 1

            # dict1[count] = new_dic
            count = count + 1


        print(dict1)

        # user = os.environ.get('hussnainkhilgi1')
        # password = os.environ.get('Pakistan@123')

        # dic2= [
        #     {"name": "ali"
        #     }
        # ]
        client = pymongo.MongoClient("mongodb+srv://hussnainkhilgi1:" + urllib.parse.quote(
            "Pakistan@123") + "@cluster0-011rc.mongodb.net/Newsbuzz?retryWrites=true&w=majority")

        db = client.get_database("Newsbuzz")
        jobs_collection = db.jobs
        tempDic = {}
        for member in dict1.keys():
            # print(dict1[member])
            # print()
            tempDic.update(dict1[member])
            insert_post = jobs_collection.update(dict1[member], dict1[member], upsert=True)
            print(insert_post)


        #
        # dataframe = pd.DataFrame.from_dict(dict1)
        # dataframe.to_json('F:\FYP files\scrapping/newdata/' + self.file + '.json')