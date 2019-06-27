#coding: UTF-8

import requests
import pandas as ps
from bs4 import BeautifulSoup as bs4

def scaping():
        url = 'https://cookpad.com/recipe/5712060'

        response = requests.get(url)
        response.encoding = response.apparent_encoding
        bs = bs4(response.content,'lxml')

        someRecipe = bs.find_all("div",attrs={'id':'recipe'})
        txt = rmTag(someRecipe)
        print(txt)


def rmTag(someRecipe):
        recipe = [x.text for x in someRecipe] #\ n??????????
        for line in recipe:
                line.strip() 
                lines = line.splitlines()
                text="\n".join(line for line in lines if line)
        return text

        
if __name__ == "__main__":
    scaping()