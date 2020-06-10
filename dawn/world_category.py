import urllib

import pandas as pd
import pymongo
import requests
from bs4 import BeautifulSoup

class world:
    linktt = ""
    file = ""

    def __init__(self, link, file):
        self.linktt = link
        self.file = file

    def main_heading(input_list, dic1, count):
        # print("=============")
        list22 = []
        # print("inside method1")
        # print("=============")
        tag_article_data = input_list.find_all("article")

        # print(len(tag_article))
        counter = count
        strintemp = ""

        for art_div in tag_article_data:
            Searchimg = art_div.find("figure")
            # Searchimg1 = Searchimg.find("figure")
            Searchimg2 = Searchimg.find("picture")
            Searchimg3 = Searchimg2.find("img")
            img = Searchimg3.get("src")
            # print(img)
            fun_div_h2_tag = art_div.find('h2')
            fun_link = fun_div_h2_tag.find('a')
            # print(fun_link.text)
            head2 = fun_link.text  # heading
            # heading
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
                continue;
            # print(upper_div.text)
            # print('<<<<<<<===2===>>>>>>')
            # print('<<<<<<<===now divide to a single p tag===>>>>>>')
            fun_div_des = fun_upper_div.find('div', {'class': 'story__content'})
            if not fun_upper_div.find('div', {'class': 'story__content'}):
                continue;
            fun_p_article = fun_div_des.find_all('p')

            for all_py in fun_p_article:
                temp = all_py.text
                strintemp = strintemp + "\n" + temp
                # print(all_py.text)
            # print('=========')
            # print("main method = ",counter)
            # print(link)
            # print('=========')
            new_dic2 = {
                "tilte": head2,
                "link": link,
                "img": img,
                "discription": strintemp
            }
            dic1[counter] = new_dic2
            counter = counter + 1
        list22 = [dic1, counter]
        # print('counter inside the methoa is ', counter)
        return list22

    def method1(tag_div_array1, dic3, count):
        list2=[]
        counter= count
        # print("=============")
        # print("inside method2 going inside ")
        # print("=============")
        tag_div_array1_div = tag_div_array1.find('div', {'class': "mt-2 slideshow--list"})
        inner_div_container = tag_div_array1_div.find_all('div', {'class': "clear-both"})

        for div_inside in inner_div_container:
            div_art_inside = div_inside.find_all('div')
            for inner_div_inside in div_art_inside:
                list2 = world.main_heading(inner_div_inside, dic3, counter)
                dic3 = list2[0]
                # print(dic3)
                counter= list2[1]
                list44 =[dic3, counter]
                # print('counter is ', counter)
        return list44



    def fun2(tag_div_grid_newspart , dic2, count):
        # print("=============")
        # print("inside method2")
        # print("=============")
        i = 0
        list2=[]
        counter = count
        while (i < 5):
            if i == 1 or i == 3:
                i += 1
            # print("this is i=", i)
            tag_article = tag_div_grid_newspart[i].find_all("article")
            # print(len(tag_article))

            strintemp1 = ""
            for art in tag_article:
                Searchimg = art.find("figure")
                # Searchimg1 = Searchimg.find("figure")
                Searchimg2 = Searchimg.find("picture")
                Searchimg3 = Searchimg2.find("img")
                img2 = Searchimg3.get("src")
                # print(img2)

                h2_tag = art.find('h2')

                link = h2_tag.find('a')  # // contain links
                heding = link.text #  heeading
                # print(link.text)
                linktexet = link.get("href") # contain link
                # print("=============")
                # print(link.get("href"))
                # print("=============")
                link_article = link.get("href")
                #     <<--------------this is the inner detail of news-------------------->>
                response = requests.get(link_article)
                data_des = response.text
                soup_des = BeautifulSoup(data_des, 'html.parser')
                main_article = soup_des.find('article', {'class': 'story'})
                if not soup_des.find('article', {'class': 'story'}):
                    continue;
                upper_div = main_article.find('div', {'class': 'template__main'})
                if not main_article.find('div', {'class': 'template__main'}):
                    continue;
                # print(upper_div.text)
                # print('<<<<<<<===2===>>>>>>')
                # print('<<<<<<<===now divide to a single p tag===>>>>>>')
                div_des = upper_div.find('div', {'class': 'story__content'})
                p_article = div_des.find_all('p')
                # print("---------------")

                for detail_p_tag in p_article:
                    # print(detail_p_tag.text)  # // contain entire news p tags to be saved
                    tempd= detail_p_tag.text
                    strintemp1 = strintemp1 + "\n" + tempd
                    # print(all_py.text)
                new_dic3 = {
                    "tilte": heding,
                    "link": linktexet,
                    "img" : img2,
                    "discription": strintemp1
                }
                # print('------------')
                # print(counter)
                # print(linktexet)
                # print(strintemp1)
                # print('------------')

                dic2[counter] = new_dic3
                counter = counter + 1
            i =i+1
            list2=[dic2,counter]
        return list2


    def mainMethod(self):

        #                  <<----------main work is here------>>

        response = requests.get(self.linktt)
        data = response.text

        soup = BeautifulSoup(data, 'html.parser')
        body_tag_world = soup.find('body')
        tags_place1_world = body_tag_world.find('div', {'class': "container-fluid clearfix"})
        tags_place2_world = tags_place1_world.find('div', {'class': "content"})
        tags_main_world = tags_place2_world.find("main")

        tag_div_grid = tags_main_world.find('div', {'class': "flex"})#big mews container
        #<--------for first element------->
        # print(tag_div_grid)
        tag_div_grid_1 = tag_div_grid.find_all('div', {'class': "flex__item sm:w-1/2 w-full"})#left coloum in container
        # print(tag_div_grid_1[0])
        tag_div_grid_newspart = tag_div_grid_1[0].find_all(lambda tag: tag.name == 'div' and
                                        tag.get('class') == ['mb-4'])
        dic1 = {}
        main_div_news = tag_div_grid_1[0].find('div', {'class': "mb-4 border-b border-b-grey-default border-b-solid"})
        # -------------fun call---------
        count = 0
        list1 = world.main_heading(main_div_news, dic1, count)

        dic2= list1[0]
        count=list1[1]


        list3 = world.fun2(tag_div_grid_newspart, dic2, count)
        dic3=list3[0]
        count3=list3[1]
        # # -------------fun call---------
        # print(dic3)

        # working gud
        tag_div_array1 = tag_div_grid_1[1].find('div', {'class': "mb-4 pt-2 border-b border-b-grey-default border-b-solid"})

        tag_div_array2 = tag_div_grid_1[1].find(lambda tag: tag.name == 'div' and
                                                                tag.get('class') == ['mb-4'])

        lista= world.method1(tag_div_array1, dic3, count3)
        dic4=lista[0]
        count4=lista[1]

        # print(dic4)


        single_div =tag_div_array2.find('div')




        dic5= world.main_heading(single_div, dic4, count4)
        # print(dic5)

        client = pymongo.MongoClient("mongodb+srv://hussnainkhilgi1:" + urllib.parse.quote(
            "Pakistan@123") + "@cluster0-011rc.mongodb.net/Newsbuzz?retryWrites=true&w=majority")

        db = client.get_database("Newsbuzz")


        Scholarship_collection = db.worldnews

        tempDic = {}
        for member in dic4.keys():
            tempDic.update(dic4[member])
            insert_post = Scholarship_collection.update(dic4[member], dic4[member], upsert=True)
            print(insert_post)

        # dataframe = pd.DataFrame.from_dict(dic4)
        # dataframe.to_json('F:\FYP files\scrapping/'+self.file+'.json')
        # print("=========================")
        # print(dic4)
            # inside_div_art = div_art_inside.find('article')
            # inside_art_h2 = inside_div_art.find('h2')
            # print(inside_art_h2.get('href'))


        # print(tag_div_array1.text)

