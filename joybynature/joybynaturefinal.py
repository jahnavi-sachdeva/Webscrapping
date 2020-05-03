from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome("C:/chromedriver")
driver.get("https://www.joybynature.com/collections/joybynature")
content = driver.page_source
soup = BeautifulSoup(content,"html.parser")

dict1={}
prices=[]
products=[]
lis=[]


ul=soup.find("ul",attrs={'class':"site-nav"})
for li in ul.findAll('li',attrs={'class':'dropdown mega-menu'}):
    div=li.find("div",attrs={'class',"site-nav-dropdown"})
    divinner=div.find("div",attrs={'class',"inner"})
    dropdown=divinner.find("ul",attrs={'class',"dropdown"})
    for li in dropdown.findAll("li"):
        a=li.find("a")
        ref=a["href"]
        brand=li.text
        brand=brand.replace("\n","")
        dict1[brand]=ref
print(dict1)
print(len(dict1))

for brand in dict1:
    #link="https://www.joybynature.com/collections/pavitra"
    link=dict1[brand]
    driver.execute_script("window.open('{}');".format(link))
    driver.switch_to.window(driver.window_handles[-1])
    content = driver.page_source
    soup = BeautifulSoup(content)
    
    main=soup.find("main")
    row=main.find("div",attrs={'class':"row"})
    col=row.find("div",attrs={'class':"block-row col-xs-9 col-main"})
    try:
        grid=col.find("div",attrs={'class':"products-grid"})
    except Exception as identifier:
        continue
    
    for div in grid.findAll("div",attrs={'class':"inner-top"}):
        #print(div)
        div1=div.find("div",attrs={'class':"product-bottom"})
        #print(div1)
        p=div1.find("span")
        #print(p.text)
        prices.append(p.text)
        div2=div.find("div",attrs={'class':"product-image"})
        a=div2.find("a")
        img=a.find("img")
        #print(img["alt"])
        products.append(img["alt"])
    #print(prices)
    print(brand,len(products),len(prices))
    df = pd.DataFrame({'Category':brand,'Products':products,"price":prices}) 
    df.to_csv('joybynature.csv',mode='a',index=False,header=False ,encoding='utf-8')
    products=[]
    prices=[]
