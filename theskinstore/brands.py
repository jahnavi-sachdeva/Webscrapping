from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome("C:/chromedriver")
driver.get("https://www.theskinstore.in/abbott")
content = driver.page_source
soup = BeautifulSoup(content,"html.parser")

dict1={}
prices=[]
products=[]



for inner in soup.findAll('div', attrs={'class':'col-md-3 col-12 col-xs-12 m-b-15'}):
    for a in inner.findAll('a'):
        n=a.text
        ref=a["href"]
        dict1[n]=ref
i=0
print(len(dict1))
i=i+1
for brand in dict1:
    link=dict1[brand]
    #driver.open(link)
    driver.execute_script("window.open('{}');".format(link))
    driver.switch_to.window(driver.window_handles[-1])
    content = driver.page_source
    soup = BeautifulSoup(content)

    for prod_name in soup.findAll("span",attrs={'class':"tss_pro_title black font-500"}):
        print(prod_name.text)
        products.append(prod_name.text)

    for price in soup.findAll("span",attrs={'class':"price"}):
        print(price.text)
        prices.append(str("Rs")+price.text)

    df = pd.DataFrame({'Brand Name':brand,'Products':products,"price":prices}) 
    df.to_csv('theskinstore.csv',mode='a',index=False,header=False ,encoding='utf-8')a