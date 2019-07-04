#coding: UTF-8

import requests
import pandas as ps
import csv
import time
from bs4 import BeautifulSoup as bs4

def scraping(urls):
        #scraping url
        Date=[]
        space = "\n"
        for search in urls:
                url = "http://cookpad.com"+search
                response = requests.get(url)
                #
                response.encoding = response.apparent_encoding 
                bs = bs4(response.content,'lxml')
                #
                #
                someRecipe = bs.find_all("div",attrs={'id':'recipe'})
                for someRecipes in someRecipe:
                        Date.extend([
                                someRecipes.select('#recipe-title')[0].text,
                                someRecipes.select('.description_text')[0].text,
                                someRecipes.select('#ingredients_list')[0].text,
                                someRecipes.select('#steps')[0].text,
                                someRecipes.select('#advice')[0].text
                        ])
                        time.sleep(1)
                        txt = [rmTag(Date)+space,''] 
                        with open('test9.csv','a') as f:
                                writer = csv.writer(f,lineterminator='\n')
                                writer.writerow(txt)


        
def getRecipesURL():
        url = 'https://cookpad.com/search/'
        urls = []
        for words in searchWords:
                response = requests.get(url+words)
                response.encoding = response.apparent_encoding 
                bs = bs4(response.content,'lxml')

                someURLs = bs.find_all("a",attrs={"class":"recipe-title font13"})
                # i = 0
                for u in someURLs:
                        
                        urls.append(u.get('href'))
                        # print(urls[i])
                        # i+=
        return urls

#remove tag 
def rmTag(someRecipe):
        text=""
        for line in someRecipe:
                line.strip() ##\n --> indention
                lines = line.splitlines()#indention --> '' 
                text+="\n".join(line for line in lines if line) #remove ''
        return text
       
if __name__ == "__main__":
        searchWords = [
                '鶏肉'#,
                # '豚肉',
                # '牛肉',
                # 'パスタ',
                # 'うどん',
        ]
        URLS = getRecipesURL()
        scraping(URLS)
        
        # scraping("/recipe/5712000")