import urllib

import pymongo
import requests
from bs4 import BeautifulSoup
import pandas as pd
from collections import defaultdict
# =====function to get data from the extracted links
def  iterate(internal_link):
    
    
    # internal_link = "https://www.dailynews.com/2019/11/11/amazon-confirms-woodland-hills-store-to-replace-old-toys-r-us-near-warner-center/"
    fun_response = requests.get(internal_link)
    fun_data = fun_response.text
    fun_soup = BeautifulSoup(fun_data, 'html.parser')
    fun_main_body = fun_soup.find('body')
    fun_inner_div_1st = fun_main_body.find('div', {'id': 'page'})
    fun_inner_div_2nd = fun_inner_div_1st.find('div', {'id': 'content'})
    fun_inner_div_3rd = fun_inner_div_2nd.find('div', {'class': 'content-area'})
    fun_inner_div_4th = fun_inner_div_3rd.find('main')
    fun_inner_div_5th = fun_inner_div_4th.find('article')
    fun_inner_div_6th = fun_inner_div_5th.find('div', {'class': 'article-content'})
    fun_inner_div_7th = fun_inner_div_6th.find('div', {'class': 'article-content-wrapper'})
    temp_img = ""
    # ----------------------------------

    if  fun_inner_div_7th.find('figure'):
        element4bb = fun_inner_div_7th.find('figure')
        element4c = element4bb.find('img')
        temp_img = element4c.get('data-src')
    else:
        temp_img="https://images.pexels.com/photos/518543/pexels-photo-518543.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940"


    print(temp_img)


    # ----------------------------------

    fun_inner_div_8th = fun_inner_div_7th.find('div', {'class': 'article-body'})
    fun_inner_div_9th = fun_inner_div_8th.find('div', {'class': 'body-copy'})
    fun_inner_div_10th = fun_inner_div_9th.find_all('p')
    dic2 = {}
    temp1=""
    for p_tag in fun_inner_div_10th:
        temp_text = p_tag.find(text=True, recursive=False);
        if not temp_text == None:
           temp1=temp1+"\n"+temp_text
    dic2[0]=temp1;
    dic2[1] = temp_img;
    # for p_tag in fun_inner_div_10th:
    #     print(p_tag.text)
    #print(temp1)
    return dic2
# =============function  ends here

def fun_article_tag(fun_div_article,dic1):
    dic2={}
    ele1 = fun_div_article.find('div', {'class': 'article-info'})
    ele2 = ele1.find('header')
    ele3 = ele2.find('h5')
    counter = dic1.__len__()
    if not ele2.find('h5'):
        ele3 = ele2.find('h2')
    ele4 = ele3.find('a')
    ele5=ele4.find("span").text ####description
    # print(ele4.get('href'))
    link_1b = ele4.get('href')####link
    dic2=iterate(link_1b)
    temp1 =dic2[0];
    img_t = dic2[1]

    new_dic1b = {
        "tilte": ele5,
        "link": link_1b,
        "img" : img_t ,
        "discription": temp1
    }
    counter =counter+1
    dic1[counter] = new_dic1b

    #print(dic1b)
    return dic1

def fun_first_section(first_section):
        fun_div1 = first_section.find('div', {'class': 'feature-wrapper'})
        fun_div2 = fun_div1.find('div', {'class': 'feature-bottom'})
        fun_div3 = fun_div2.find('div', {'class': 'landing-secondary-main headline-list'})
        fun_div4 = fun_div3.find('ul')
        fun_div5 = fun_div4.find_all('li')
        dic1={}
        counter=1
        for element_in in fun_div5:
            element4b = element_in.find('article')
            #----------------------------------
            # element4bb = element4b.find('figure')
            # element4c = element4bb.find('img')
            # temp_img= element4c.get('data-src')
            # print(temp_img)
            # break

            #----------------------------------
            element5b = element4b.find('div', {'class': 'article-info'})
            element6a = element5b.find('header')
            element6b = element6a.find('h5')
            # print()
            element7b = element6b.find('a')
            element7bb=element7b.find("span").text
            # print(element7bb)###### title
            # print(element7b.get('href'))
            link_1a = element7b.get('href')###### link

            dic2=iterate(link_1a)
            temp = dic2[0];
            img_t = dic2[1]

            new_dic = {
                "tilte": element7bb,
                "link": link_1a,
                "img": img_t,
                "discription": temp
            }
            dic1[counter]=new_dic
            counter=counter+1
            #print(dic1)
        return dic1

    # ======================

def third_section_triverse(third_section,dic4):
        fun_div = third_section.find('div' , {'class': 'three-one-left'})
        fun_div_2nd = fun_div.find_all('section', {'class': 'section-highlight'})

        counter = dic4.__len__()
        for div_loopi  in fun_div_2nd:
            fun_div_3rd = div_loopi.find('div', {'class': 'section-highlight-content'})
            fun_div_4th = fun_div_3rd.find('div', {'class': 'section-feature'})
            fun_div_5th = fun_div_4th.find('article' )
            fun_div_6th = fun_div_5th.find('div',{'class':  'article-info'})
            fun_div_7th = fun_div_6th.find('header')
            fun_div_8th = fun_div_7th.find('h3')
            fun_div_9th = fun_div_8th.find('a')
            fun_div_10th = fun_div_9th.find("span").text #####title
            # print(fun_div_9th.get("href"))
            div_link = fun_div_9th.get('href')##### link
            dic2=iterate(div_link)
            temp3 = dic2[0];
            img_t = dic2[1]
            new_dic2 = {
                "tilte": fun_div_10th,
                "link": div_link,
                "img": img_t,
                "discription": temp3
            }
            dic4[counter] = new_dic2
            counter = counter + 1
            #print(dic3)
            # break
        return dic4

    # ======================
def fun_second_Section(second_Section_div,dic1):
        inner_div_5th = second_Section_div.find_all('div', {'class': 'landing-item'})
        counter = dic1.__len__()
        counter=counter+1
        for element1 in inner_div_5th:
            if not element1.find('section', {'class': 'section-highlight'}):
                continue
            element2 = element1.find('section', {'class': 'section-highlight'})
            element3 = element2.find('div', {'class': 'section-highlight-content'})
            element3b = element3.find('div', {'class': 'section-feature'})
            element4 = element3b.find('article')
            element5 = element4.find('div', {'class': 'article-info'})
            element6 = element5.find('h2')
            element7 = element6.find('a')
            element8 = element7.find("span").text  ##### title
            link_section3 = element7.get('href') ### link
            linkk= element7.get('href')
            # print(element7.get('href'))
            dic2= iterate(link_section3)
            temp4 = dic2[0];
            img_t = dic2[1]
            new_dic3 = {
                "tilte": element8,
                "link": linkk,
                "img": img_t,
                "discription": temp4
            }
            dic1[counter] = new_dic3
            counter = counter + 1
            #print(dic4)

        return dic1

    # =====================
def fun_1st_section_buttom (first_section,dic1):
        dic1bb={}
        dic2=dic1
        fun_div_temp = first_section.find('div', {'class': 'feature-wrapper'})
        fun_div_temp2 = fun_div_temp.find('div', {'class': 'feature-top'})
        # div
        fun_div_temp2b = fun_div_temp2.find('div', {'class': 'feature-right'})
        fun_div_temp3 = fun_div_temp2b.find_all('article')
        for ele22 in fun_div_temp3:
            fun_article_tag(ele22,dic1)
        # ARTICLE
        fun_div_temp3b = fun_div_temp2.find('article')
        dic1bb = fun_article_tag(fun_div_temp3b,dic2)
        # print("----------------")

        # print("----------------")
        return dic1bb
class locala:
    linktt = ""
    file = ""

    def __init__(self, link, file):
        self.linktt = link
        self.file = file

    def mainPro(self):
        # print(linktt)
        response = requests.get(self.linktt)

        data = response.text
        soup = BeautifulSoup(data, 'html.parser')
        main_body = soup.find('body')
        inner_div_1st = main_body.find('div', {'id': 'page'})
        inner_div_2nd = inner_div_1st.find('div', {'id': 'content'})
        inner_div_3rd = inner_div_2nd.find('div', {'class': 'content-area'})
        inner_div_4th = inner_div_3rd.find('main')
        inner_div_5th = inner_div_4th.find('div', {'class': 'homepage section'})
        dic = {}

        # ========== 111

        first_section = inner_div_5th.find('section', {'class': 'feature-section'})
        # --------function calls first section---------
        if inner_div_5th.find('section', {'class': 'feature-section'}):
            # print("======11 top========")
            dic1 = fun_first_section(first_section)

            # print(dic1)

            # print("=======11 buttom=======")
            dic1 = fun_1st_section_buttom(first_section, dic1)
            # print(dic1)


        # else:
            # print("=======11========")
            # print('1st section not exist')

        # ------------------------------

        # ========== 2222
        #
        # --------function calls 2nd section---------
        second_section_div = inner_div_5th.find('div', {'class': 'landing-row landing-four-up'})
        if inner_div_5th.find('div', {'class': 'landing-row landing-four-up'}):
            dic3 = fun_second_Section(second_section_div, dic1)

            # print("=======22=======")
            # print(dic3)

        # else:
            # print("=======22=======")
            # print('2nd section not exist')
        # ------------------------------

        # ========== 3333
        third_section = inner_div_5th.find('div', {'class': 'landing-three-one landing-row'})
        if inner_div_5th.find('div', {'class': 'landing-three-one landing-row'}):
            # --------function calls 3rd section---------
            # print("=======33=======")
            dic3 = third_section_triverse(third_section, dic3)
            # print(dic3)
        # else:
            # print("=======33=======")
            # print('section not exist')
        # print(third_section)

        client = pymongo.MongoClient("mongodb+srv://hussnainkhilgi1:" + urllib.parse.quote(
            "Pakistan@123") + "@cluster0-011rc.mongodb.net/Newsbuzz?retryWrites=true&w=majority")

        db = client.get_database("Newsbuzz")

        if (self.file == "DailySports"):
            Scholarship_collection = db.sports
        elif(self.file == "DailyBussinesss"):
            Scholarship_collection = db.bussinesses
        elif (self.file == "DailylocalNews"):
            Scholarship_collection = db.dawns
        else:
            Scholarship_collection = db.dawns
        tempDic = {}
        for member in dic3.keys():
            tempDic.update(dic3[member])
            insert_post = Scholarship_collection.update(dic3[member], dic3[member], upsert=True)
            print(insert_post)
        # dataframe = pd.DataFrame.from_dict(dic3)
        # dataframe.to_json('F:\FYP files\scrapping/'+self.file+'.json')


    # =================


    # ======================

    print("*********")
