import urllib

import pandas as pd
import pymongo
import requests
from bs4 import BeautifulSoup


class scholar:
    linktt = ""
    file = ""

    def __init__(self, link, file):
        self.linktt = link
        self.file = file
    def  mainProMethod(self):
        link_ms= "https://www.eduvision.edu.pk/scholarships/ms-mphil.php"
        fun_response = requests.get(self.linktt)
        fun_data_des = fun_response.text
        fun_soup_des = BeautifulSoup(fun_data_des, 'html.parser')
        fun_main_article = fun_soup_des.find(lambda tag: tag.name == 'body' )
        fun_main_article1 = fun_main_article.find('div', {'id': 'page'})
        fun_main_article2 = fun_main_article.find('div', {'class': 'right_sidebar'})
        fun_main_article3 = fun_main_article.find('div', {'class': 'main_contentLeft page'})
        fun_main_article4 = fun_main_article3.find('div', {'class': 'posts-wrap'})
        fun_main_article5 = fun_main_article4.find_all('div', {'class': 'row'})
        dict1={}
        count=1
        for all_row in fun_main_article5:
            fun_main_article6 = all_row.find_all('div', {'class': 'col-md-12 col-xs-12'})
            for all_ineer in fun_main_article6:
                fun_main_article7 = all_ineer.find('h2')
                title = fun_main_article7.text #############title
                fun_main_article8=fun_main_article7.find('a')
                link = fun_main_article8.get('href')############link
                link='https://www.eduvision.edu.pk/scholarships/'+ link
                #print(link)
                fun_response1 = requests.get(link)
                fun_data_des1 = fun_response1.text
                fun_soup_des1 = BeautifulSoup(fun_data_des1, 'html.parser')
                fun_main_article1b = fun_soup_des1.find('div', {'class':'content-area'})
                fun_main_article2b = fun_main_article1b.find('div', {'class': 'post_content'})
                fun_main_article3b = fun_main_article2b.find('p')
              # print()
                description= fun_main_article3b.text.strip()
                new_dic = {
                    "tilte": title,
                    "link": link,
                    "discription": description
                }
                dict1[count] = new_dic
                count = count + 1

               # print('-----------------------------------------')

       # print(dict1)

        client = pymongo.MongoClient("mongodb+srv://hussnainkhilgi1:" + urllib.parse.quote(
            "Pakistan@123") + "@cluster0-011rc.mongodb.net/Newsbuzz?retryWrites=true&w=majority")

        db = client.get_database("Newsbuzz")

        if (self.file == "MS"):
            Scholarship_collection = db.msscholarships
        else:
            Scholarship_collection = db.bsscholarships
        tempDic = {}
        for member in dict1.keys():
            tempDic.update(dict1[member])
            insert_post = Scholarship_collection.update(dict1[member], dict1[member], upsert=True)
            print(insert_post)

        # dataframe = pd.DataFrame.from_dict(dict1)
        # # print("the path is = " + 'D:/project/proj/NewsBuzz/server/dataFiles/'+self.file ,'scholarship_news.json' )
        # dataframe.to_json('F:\FYP files\scrapping/newdata/'+self.file+'scholarship_news.json')

        #D:\project\proj\newsBuzz\server\dataFiles