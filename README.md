# DataScraping

 
 In this project, reading an excel file that contains URL's of data to be scraped and product name, stock, current price, non-discounted price, and discount rate are prepared to be written next to the excel file.
 
 
 ```
pip install pandas
pip install BeautifulSoup
pip install requests
pip install FileManager
pip install xlsx
 ```
 
The above-mentioned libraries are downloaded

Firstly, I defined the dataset of the links which is links.xlsx, then the program read it. After that I defined my user agent it should be written since web scrapping uses it. Then I started to write my data into an excel file. I defined a for loop to write all of them nearby the links cell and do the scrapping of entire links in the excel file. Then if statement comes here. I used beautifulsoup module to do web scrapping and get requests to pull data that I want. I used search.find() function to program find the necessary value and take them from the HTML file of the web page. After that, since I have the required data, I need to add them to the excel file and print them. df.loc[] and worksh.write() functions are required for it. In print sections, I just want to see if it is working in the console or not and I checked. Then I closed the excel file.


## Questions

- If I have 10.000 urls that I should visit, first I placed it in separate files to be a thousand. Then I create 10 different code block to scrap entire values. Then I would run 10 different blocks of code that I wrote separately. According to my calculations, if the 1000 files you send take 8.74 seconds, 10,000 of them will be finished in 87.4 seconds. 
- I don't think technology will scrap data by itself once a day without humans yet, it might be in the future
- API, is the short of Application Programming Interface. This interface is a software tool that allows two applications to interact with each other. Nowadays, REST API is used for different languages to communicate within different applications. It only receives a response over the HTTP protocol and is usually returned in JSON format. However, it can be returned as XML if desired.

## Challanges I face

To be frank, I didn't know how to do web scrapping. I have only researched and practiced for 3 days since you sent the e-mail. I did my practice both in terminal, IDLE and visual studio. Thanks to you, I opened the inspect I opened by mistake tab for the first time. For beginners, web scraping is quite difficult, but with 2 months of proper practice, it is a very easy method. You wanted me to add plain javascript, but I couldn't add it because I didn't know how to add it. I also had a problem with the FileManager while running the program. I don't know if my code is working or not, because it didn't open even though I installed it. I'm throwing the code block and readme file I wrote so that I can show you my working method and algorithm. I also uploaded the project to the system with git using the terminal.

## Things that I have learned from this project

In this project, I tried to learn the basics of web scraping with python. I learned the positions of an element appearing on the site in the HTML file. It wasn't too hard for me to understand as I know basic HTML. I tried to learn to write about a subject that I did not know at all, using libraries that I did not know. I didn't know about the BeautifulSoup module before, so I learned it. Thank you very much for your contribution to me.
 
