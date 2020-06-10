import urllib

import pandas as pd
import pymongo
import requests
from bs4 import BeautifulSoup

   #              <<<<<<<-----------dawn news/tech-------------->>>>>>>> working

class tech:
    linktt = ""
    file = ""

    def __init__(self, link, file):
        self.linktt = link
        self.file = file

    def mainMethod1(self):

        response = requests.get(self.linktt)
        data = response.text
        dic1 = {}

        soup = BeautifulSoup(data, 'html.parser')
        body_tag = soup.find('body')
        tags_place1 = body_tag.find('div', {'class': "container-fluid clearfix"})
        # print("here i M ")
        # print(tags_place1)
        tags_place2 = tags_place1.find('main')
        tags_place3 = tags_place2.find('div', {'class': "flex"})
        tags_place4 = tags_place3.find_all('div', {'class': "flex__item w-full"})
        for main_content in tags_place4:

            tags_place5 = main_content.find_all('div', {
                'class': "mb-4 sm:border-b sm:border-b-solid sm:border-b-grey-default"})
            # print(tags_place5[1])
            # break
            for inner_news in tags_place5:
                tags_place6 = inner_news.find('div', {'class': "flex"})
                tags_place7 = tags_place6.find_all('div', {'class': "flex__item sm:w-1/4 w-full"})
                # print(tags_place7[0])
                # break
                for all_articl in tags_place7:
                    dic1 = tech.main_tech(all_articl,dic1)

        # print("end here")
        print(dic1)

        client = pymongo.MongoClient("mongodb+srv://hussnainkhilgi1:" + urllib.parse.quote(
            "Pakistan@123") + "@cluster0-011rc.mongodb.net/Newsbuzz?retryWrites=true&w=majority")

        db = client.get_database("Newsbuzz")
        tech_collection = db.technologies
        tempDic = {}
        for member in dic1.keys():
            tempDic.update(dic1[member])
            insert_post = tech_collection.update(dic1[member], dic1[member], upsert=True)
            print(insert_post)
            # dataframe = pd.DataFrame.from_dict(dic1)
        # dataframe.to_json('F:\FYP files\scrapping/'+self.file+'.json')



    def main_tech(input_list, dic1):
        tag_article_data = input_list.find_all("article")
        # print(len(tag_article))
        count = dic1.__len__()
        temp1 = ""
        for art_div in tag_article_data:
            Searchimg = art_div.find("figure")
            # Searchimg1 = Searchimg.find("figure")
            Searchimg2 = Searchimg.find("picture")
            Searchimg3 = Searchimg2.find("img")
            img2 = Searchimg3.get("src")

            fun_div_h2_tag = art_div.find('h2')
            fun_link = fun_div_h2_tag.find('a')
            # print(fun_link.text)
            title = fun_link.text  # title
            # print(fun_link.get("href"))
            link = fun_link.get("href")  # link
            fun_link_article = fun_link.get("href")
            #     <<--------------this is the inner detail of news-------------------->>
            fun_response = requests.get(fun_link_article)
            fun_data_des = fun_response.text
            fun_soup_des = BeautifulSoup(fun_data_des, 'html.parser')
            fun_main_article = fun_soup_des.find('article', {'class': 'story'})
            if not fun_soup_des.find('article', {'class': 'story'}):
                continue

            fun_upper_div = fun_main_article.find('div', {'class': 'template__main'})
            if not fun_main_article.find('div', {'class': 'template__main'}):
                continue
            # print(upper_div.text)
            # print('<<<<<<<===2===>>>>>>')
            # print('<<<<<<<===now divide to a single p tag===>>>>>>')
            fun_div_des = fun_upper_div.find('div', {'class': 'story__content'})
            if not fun_upper_div.find('div', {'class': 'story__content'}):
                continue
            fun_p_article = fun_div_des.find_all('p')
            for all_py in fun_p_article:
                # print(all_py.text)
                temp = all_py.text
                temp1 = temp1 + temp
            # print(img2)
            new_dic1 = {
                "tilte": title,
                "link": link,
                "img": img2,
                "discription": temp1
            }
            dic1[count] = new_dic1
            count = count + 1
            print(dic1)
        # print(dic1)
        return dic1


