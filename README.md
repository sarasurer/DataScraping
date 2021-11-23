# DataScraping
 Junior Software Developer Application Case Study
 
 In this project, reading an excel file that contains URL's of data to be scraped and product name, stock, current price, non-discounted price, and discount rate are prepared to be written next to the excel file.
 
 
 
 #pip install pandas
 #pip install BeautifulSoup
 #pip install requests
 #pip install FileManager
 #pip install xlsx
 
 
The above-mentioned libraries are downloaded

Firstly, I defined the dataset of the links which is links.xlsx, then the program read it. After that I defined my user agent it should be written since web scrapping uses it. Then I started to write my data into an excel file. I defined a for loop to write all of them nearby the links cell and do the scrapping of entire links in the excel file. Then if statement comes here. I used beautifulsoup module to do web scrapping and get requests to pull data that I want. I used search.find() function to program find the necessary value and take them from the HTML file of the web page. After that, since I have the required data, I need to add them to the excel file and print them. df.loc[] and worksh.write() functions are required for it. In print sections, I just want to see if it is working in the console or not and I checked. Then I closed the excel file.



 
