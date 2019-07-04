#coding: UTF-8

import requests
import pandas as ps
import csv
import time
from bs4 import BeautifulSoup as bs4
#get information
def scraping(urls):
        #scraping url
        Date=[]
        space = "\n\n"
        for search in urls:
                url = cookpad+search
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
                        time.sleep(3)
                        txt = [rmTag(Date)+space,''] 
                        with open('test9.csv','a') as f:
                                writer = csv.writer(f,lineterminator='\n')
                                writer.writerow(txt)
        time.sleep(3)
#get recipesURL
def getRecipesURL(someOne):
        urls = []
        for words in someOne:
                response = requests.get(cookpad+words)
                response.encoding = response.apparent_encoding 
                bs = bs4(response.content,'lxml')
                someURLs = bs.find_all("a",attrs={"class":"recipe-title font13"})
                for u in someURLs:
                        urls.append(u.get('href'))
                time.sleep(3)
        return urls
#get pagingURL
def getpagingURL(someOne):
        page = []
        for words in someOne:
                response = requests.get(cookpad+words)
                response.encoding = response.apparent_encoding 
                bs = bs4(response.content,'lxml')

                paging   = bs.find_all("div",attrs={"class":"center paginate"})
                for p in paging:
                        page.append(p.select('a:nth-child(1)'))
                        page.append(p.select('a:nth-child(2)'))
                        page.append(p.select('a:nth-child(3)'))
                        page.append(p.select('a:nth-child(4)'))
                        page.append(p.select('a:nth-child(5)'))

                page [1]= str(page[1])[10:65]
                page [2]= str(page[2])[10:65]
                page [3]= str(page[3])[10:65]
                page [4]= str(page[4])[10:65]
                page [0]= str(page[1]).replace("page=2","page=1")
        return page
#remove tag 
def rmTag(someRecipe):
        text=""
        for line in someRecipe:
                line.strip() ##\n --> indention
                lines = line.splitlines()#indention --> '' 
                text+="\n".join(line for line in lines if line) #remove ''
        return text
#list print_all
def print_list(some):
        if type(some) == list:
                print("print start \n")
                for p in some:
                  print(p)
                return
        if type(some) == str:
                print("print start \n")
                print(some)
                return
        else :
                try:
                        print(some,type(some))
                except TypeError:
                        print("例外です",type(some))
                

if __name__ == "__main__":
        searchWords = [
                '/search/鶏肉'
                #,'/search/豚肉'
                #,'/search/牛肉'
                #,'/search/パスタ'
                #,'/search/うどん'
        ]
        cookpad = 'https://cookpad.com'
        pagingURLs = getpagingURL(searchWords)
        URLS = getRecipesURL(pagingURLs)
        #scraping(recipes)
        