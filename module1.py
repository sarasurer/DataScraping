
import pandas as pd
from bs4 import BeautifulSoup
import requests as requests
import urllib
from FileManager import ExcelParser
import xlsxwriter


#defined excel file of our links
datasetLocation = "links.xlsx";
df = pd.reaf_excel(datasetLocation, "Sheet1") #reading  excel file
userAgent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}
#defined user agent

work = xlsxwriter.work('links.xlsx')
worksh = work.add_worksh()

searchURL= "https://www.markastok.com"; #base url


for x in range(0, len(df.index)): #i did a for loop 0 to lenght of urls
    if str(df.iloc[x,5]) is None: #i have five variables
        print(str(df.iloc[x,0]) + " | " + str(df.iloc[x,1]) + " | "  + str(df.iloc[x,2]) + " | " + str(df.iloc[x,3]) + " | " +str(df.iloc[x,4]) + " | "  +str(df.iloc[x,5]))
    else:
        #not the links starts here
        links = df.iloc[x,0]
        #i searched  variables which are name, stock, current price, discount price, and the discount rate of the product
        search0 = BeautifulSoup (requests.get(searchURL + urllib.parse.quote_plus(links) + 'name', headers = userAgent).text, 'html.parser')
        name = search0.find('a', href = True) #location of the name in the html of web

        search1 = BeautifulSoup(requests.get(searchURL + urllib.parse.quote_plus(links) + 'stock', headers=userAgent).text, 'html.parser')
        stock = search1.find('input', {"class": "liste-stock"}).get_text()#location of the stcok in the html of web

        search2 = BeautifulSoup(requests.get(searchURL + urllib.parse.quote_plus(stock) + 'currentPrice', headers=userAgent).text, 'html.parser')
        currentPrice = search2.find('span', {"class": "currentPrice"}).get_text()#location of the current price in the html of web

        search3 = BeautifulSoup(requests.get(searchURL + urllib.parse.quote_plus(currentPrice) + 'discountPrice', headers = userAgent).text, 'html.parser')
        discountedPrice = search3.find('span', {"class": "discountedPrice"}).get_text()#location of the discount price in the html of web

        search5 = BeautifulSoup(requests.get(searchURL + urllib.parse.quote_plus(discountedPrice) + 'discount' , headers = userAgent).text, 'html.parser')
        discount = search5.find('div', {"class": "product-item-discount"}).get_text()#location of the discount rate in the html of web

        df.loc[x, 'name'] = name; #it append to the our links excel file one by one
        df.loc[x, 'stock'] = stock;
        df.loc[x, 'currentPrice'] = currentPrice;
        df.loc[x, 'discountedPrice'] = discountedPrice;
        df.loc[x, 'discount'] = discount;



        worksh.write('name', name) #write to the excel file
        worksh.write('stock', stock)
        worksh.write('currentPrice', currentPrice)
        worksh.write('discountedPrice', discountedPrice)
        worksh.write('discount', discount)
        



        print(df.iloc[x,0] + " | " + "name" + " | " + 'stock' + " | " + 'currentPrice' + " | " + 'discountedPrice' + " | " + 'discount') #i juts want to see if it working or not
        df.to_excel(datasetLocation, index = False) #checking
      #  return name, stock, currentPrice, discountedPrice, discount


work.close() #closed excel file





    
