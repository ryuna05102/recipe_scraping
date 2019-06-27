#coding: UTF-8

import requests
import pandas as ps
from bs4 import BeautifulSoup as bs4

def scaping(URL):
        #scraping url

        url = "http://cookpad.com"+URL
        response = requests.get(url)
        #
        response.encoding = response.apparent_encoding 
        bs = bs4(response.content,'lxml')
        
        #
        #
        someRecipe = bs.find_all("div",attrs={'id':'recipe'})

        txt = rmTag(someRecipe)
        print(txt)


def getRecipesURL():
        url = 'https://cookpad.com/search/'
        for words in searchWords:
                response = requests.get(url+words)

                response.encoding = response.apparent_encoding 
                bs = bs4(response.content,'lxml')


                someURLs = bs.find_all("a",attrs={"class":"recipe-title font13"})
                # txt = rmTag(someURLs)
                # print(txt)

                # someURLs = bs.find_all("a").get("href")
                
                print(someURLs)


        return someURLs

#remove tag 
def rmTag(someRecipe):
        recipe = [x.text for x in someRecipe] #many \n in text
        for line in recipe:
                line.strip() ##\n --> indention
                lines = line.splitlines()#indention --> '' 
                text="\n".join(line for line in lines if line) #remove ''
        return text

        
if __name__ == "__main__":
        searchWords = [

                '鶏肉',
                '豚肉',
                '牛肉',
                'パスタ',
                'うどん',
        ]
        URLS = getRecipesURL()
        # scaping(URLS)