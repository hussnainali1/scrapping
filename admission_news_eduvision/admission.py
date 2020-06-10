import urllib

import pandas as pd
import pymongo
import requests
from bs4 import BeautifulSoup

class admission:
    linktt = ""
    file = ""

    def __init__(self, link, file):
        self.linktt = link
        self.file = file
    def  mainProMethod(self):
        fun_response = requests.get(self.linktt)
        fun_data_des = fun_response.text
        fun_soup_des = BeautifulSoup(fun_data_des, 'html.parser')
        fun_main_article = fun_soup_des.find(lambda tag: tag.name == 'body' )
        fun_main_article1 = fun_main_article.find('div', {'id': 'page'})
        fun_main_article2 = fun_main_article.find('div', {'class': 'right_sidebar'})
        fun_main_article3 = fun_main_article.find('div', {'class': 'main_contentLeft page'})
        fun_main_article4 = fun_main_article3.find_all('div', {'class': 'col-lg-12 col-md-12 col-sm-12 col-xs-12'})
        dic1={}
        i=1
        counter = 1
        # fun_main_article5 = fun_main_article4.find_all('div', {'class': 'col-lg-12 col-md-12 col-sm-12 col-xs-12'})
        # fun_main_article5 = fun_main_article4.find('div', {'class': 'col-lg-12 col-md-12 col-sm-12 col-xs-12'})
        fun_main_article6 = fun_main_article4[1].find('table')
        fun_main_article7 = fun_main_article6.find('tbody')
        fun_main_article8 = fun_main_article7.find_all('tr')
        for rec in fun_main_article8:
            detail = rec.text.strip()
            img= rec.find("img").get("src")

            new_dic1 = {
                "category" : 'admission' ,
                "img_link": img,
                "discription": detail
            }
            dic1[counter]=new_dic1
            counter=counter+1
            i=i+1


        client = pymongo.MongoClient("mongodb+srv://hussnainkhilgi1:" + urllib.parse.quote(
            "Pakistan@123") + "@cluster0-011rc.mongodb.net/Newsbuzz?retryWrites=true&w=majority")

        db = client.get_database("Newsbuzz")
        # dbname = db+"." + self.file + "admission"
        if(self.file== "MS"):
            admission_collection = db.msadmissions
        else:
            admission_collection = db.bsadmissions
        tempDic = {}
        for member in dic1.keys():
            # print(dict1[member])
            # print()
            tempDic.update(dic1[member])
            insert_post = admission_collection.update(dic1[member], dic1[member], upsert=True)
            print(insert_post)

        # while(i<18):
        #     # print(len(fun_main_article5))
        #     for scholar in fun_main_article5:
        #         if i==4 or i==16 or i==18:
        #             if i==16:
        #                 i=i+1
        #             if i==18:
        #                 break
        #             i=i+1
        #
        #         else:
        #
        #             print('value if i is', i)
        #             fun_main_article6 = fun_main_article5[i].find('div', {'class': 'entry-main'})
        #             # if(i==22):
        #             #     print(fun_main_article6)
        #             detail = fun_main_article6.text.strip()
        #             new_dic1 = {
        #                 "category" : 'admission' ,
        #                 "discription": detail
        #             }
        #             dic1[counter]=new_dic1
        #             counter=counter+1
        #             i=i+1


        # print(dic1)


        # dataframe = pd.DataFrame.from_dict(dic1)
        # dataframe.to_json('F:\FYP files\scrapping/'+self.file+'admission_news.json')




