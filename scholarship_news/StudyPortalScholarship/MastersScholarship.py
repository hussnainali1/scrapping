import urllib

import pandas as pd
import pymongo
import requests
from bs4 import BeautifulSoup


class InternationalScholar:
    linktt = ""
    file = ""

    def __init__(self, link, file):
        self.linktt = link;
        self.file = file;

    def  mainProMethod(self):
        link_ms = "https://www.scholarshipportal.com/master/scholarships/united-states"
        fun_response = requests.get(self.linktt)
        fun_data_des = fun_response.text
        fun_soup_des = BeautifulSoup(fun_data_des, 'html.parser')
        fun_main_article = fun_soup_des.find(lambda tag: tag.name == 'body')
        fun_main_article1 = fun_main_article.find('div', {'id': '__nuxt'})
        fun_main_article2 = fun_main_article.find('div', {'class': 'section'})
        fun_main_article3 = fun_main_article.find('div', {'class': 'row'})
        fun_main_article4 = fun_main_article3.find('div', {'class': 'col-sm-8 col-md-9'})
        fun_main_article5 = fun_main_article4.find('div', {'class': 'l-content'})
        fun_main_article6 = fun_main_article5.find_all('a', {'class': 'scholarship scholarship__type--list'},
                                                       recursive=False)
        dict1 = {}
        count=1

        for all_ineer in fun_main_article6:
            link = all_ineer.get('href')  ############link

            fun_main_article7 = all_ineer.find('h3')
            title = fun_main_article7.text  #############title

            link = 'https://www.scholarshipportal.com' + link
            "https://www.scholarshipportal.com/scholarship/breast-cancer-car-donations-annual-college-scholarship"
            # print(link)
            # print(link)
            fun_response1 = requests.get(link)
            fun_data_des1 = fun_response1.text
            fun_soup_des1 = BeautifulSoup(fun_data_des1, 'html.parser')
            fun_main_article1bb = fun_soup_des1.find('body')
            fun_main_article1c = fun_main_article1bb.find('div', {'id': '__layout'})
            fun_main_article1cc = fun_main_article1bb.find('div')

            fun_main_article1d = fun_main_article1cc.find('div', {'class': 'content'})
            fun_main_article1e = fun_main_article1d.find('div', {'class': 'section'})
            fun_main_article1f = fun_main_article1e.find('div', {'class': 'container'})

            fun_main_article1b = fun_main_article1f.find('div', {'class': 'row'})
            fun_main_article2b = fun_main_article1b.find('main')
            des = fun_main_article1b.text.strip()

            fun_main_article3b = fun_main_article2b.find('p')

            new_dic = {
                "tilte": title,
                # "img": "https://as2.ftcdn.net/jpg/02/04/08/39/500_F_204083909_4fgqLvtkrSQf3v13a0IG8fhoMkGfERU8.jpg",
                "link": link,
                "discription": des
            }
            dict1[count] = new_dic
            count = count + 1

        client = pymongo.MongoClient("mongodb+srv://hussnainkhilgi1:" + urllib.parse.quote(
            "Pakistan@123") + "@cluster0-011rc.mongodb.net/Newsbuzz?retryWrites=true&w=majority")

        db = client.get_database("Newsbuzz")

        if (self.file == "MSscholarPortal"):
            Scholarship_collection = db.msscholarships
        else:
            Scholarship_collection = db.bsscholarships
        tempDic = {}
        for member in dict1.keys():
            tempDic.update(dict1[member])
            insert_post = Scholarship_collection.update(dict1[member], dict1[member], upsert=True)
            print(insert_post)

        # dataframe = pd.DataFrame.from_dict(dict1)
        # # print("the path is = " + 'D:/project/proj/NewsBuzz/server/dataFiles/' + self.file, 'scholarship_news.json')
        # dataframe.to_json('F:\FYP files\scrapping/newdata/' + self.file + 'scholarship_news.json')

 #D:\project\proj\newsBuzz\server\dataFiles