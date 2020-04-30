import json
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import os
# pageno=2
# driver = webdriver.Chrome("C:/chromedriver")
# driver.get('https://www.purplle.com')
# time.sleep(10)
# x=driver.find_elements_by_xpath("//a[@class='mg-mn-li-a shpcat']")[0]
# x.click()
# brand_list=['4-step','a-fragrance-story','a-by-bom','aadi','abercrombie-fitch','acnes','adidas','ads','agaro','aloeveda','alpecin','alps-goodness','anaya','anchor','ancient-living','arama','aramis','arata-zero-chemicals','arezia','armaf','aroma-magic','aromagic','aromamusk','audreys','australis','avene','avnii-organics','avon','axe','ay','aya','azzaro','baby-dove','bajaj','bare-essentials','batiste','bblunt','be-o-man','beardo-beard','bebe-nature','bella','bella-voste','bentley','berina','berkowits','beth-bender-beauty','beverly-hills-polo-club','beyu','bi-feather','bio-luxe','bio-oil','bioayurveda','biotique','bling-bag','blue-heaven','blue-nectar','body-cupid','bodyherbals','bonjour-paris','borren','brush-it','brut','brylcreem','burberry','bvlgari','calvin-klein','cameleon','carmesi','carolina-herrera','cartier','cemera','cetaphil','cettua','chaoba','cheryls','chopard','christian-dior','clamy','clinic-plus','coccoon','color-fever','colorbar','colour-me','dalan','darling-isabella','david-beckham','davidoff','deemark','dermdoc','dettol','dexe','diana-of-london','diesel','divo','dkny','dolce-gabbana','dolphin','dove','dr-ortho','dr-sheth-s','dr-vaidya-s','dunhill','durex','dyna','elizabeth-arden','elle18','enega','enfagrow','enfamil','enn-s-closet','essence','estee-lauder','eti','everteen','everyuth','faces','fair-lovely','ferrari','flawless','floh','focallure','foltene','foxmen','fruttini','garnier','gemei','gillette','gillette-venus','giorgio-armani','givenchy','glamveda','globus','good-vibes','gorgio-professional','gravitale','greenberry-organics','gucci','guess','guy-laroche','hair-care','hair4real','head-and-shoulders','herbal-essences','herbalife','himalaya','hiphop','hot-ice','htc','hugo-boss','i-heart-revolution','i-amsterdamn','iceberg','ikkai','inatur-herbals','incolor','india-grooming-club','indulekha','inlife','innisfree','institute-karite-paris','issey-miyake','it-s-skin','itch-guard','jaguar','jennifer-lopez','joop','jungle-magic','just-herbs','jysuper','kaiv','kama-ayurveda','kaya','kaya-youth','kent','kenzo','khadi-natural','khadi-pure','khadi-suddha','kiss-beauty','kiyome','klairs','loreal','loreal-professionnel','l-a-colors','l-a-girl','la-organo','lacoste','lacto-calamine','lais-ayurveda','lakme','lalique-','lancome','layerr','limese','lip-smacker','little-s','livon','loewe','london-facial-wipes','lotus','lotus-organics','louis-cardin','love-beauty-planet','make-up-for-life','makeprem','makeup-revolution-london','mamaearth','man-arden','manipol','marc-anthony','mary','matrix','matrix-hair-color','matrix-opticare','maxel','maybelline','mcaffeine','meilin','michel-mercier-by-kampalook','micio','milani','miss-claire','miss-nails','miss-rose','mixnsell','moda-cosmetics','mom-and-world','mond-sub','mont-blanc','moov','morpheme-remedies','musclexp','music-flower','myglamm','namyaa','narciso-rodriguez','natio','natural-vibes','nautica','neutriderm','nicka-k','nisha','nivea','note','nourishvitals','nova','ny-bae','nyassa','nycil','o3','organix','olay','old-spice','olivia','organic-harvest','organic-india','oriental-botanics','oxy','pac','paco-rabanne','palladio','palmer','palmolive','pantene','parachute','park-avenue','pears','petal-fresh','phy','physicians-formula','pilaten','playboy','plum','police','pollution-safe','ponds','pp','prada','prem-dulhan','purplle','purplle-membership','qraa','qraa-men','queenbe','qvs','ralph-lauren','remove','resme','revlon','richfeel','ring-guard','roberto-cavalli','roop-mantra','rude-cosmetic','s-t-dupont','saint-beard','salon-palette','salvatore-ferragamo','sandook-sutras','sara','schwarzkopf','schwarzkopf-professional','sergio-tacchini','set-wet','shany','simple','simply-straight','skincode','skinn','skore','specifix','st-d-venc','st-botanica','star-struck','statz','stay-quirky','sugar','sunsilk','swiss-beauty','swiss-image','thank-you-farmer','the-body-shop','the-moms-co','the-natures-co','thyme-organic','titan','tomford','tommy-hilfiger','toni-guy','tresemme','true-roots','ts','urban-swagger','ustraa','v-and-g','vaadi-herbals','vakola','vaseline','vayam','verdure-vegan-fragrances','versace','vipera','vit-citrus','vlcc','w.o.w','welocity','wet-n-wild','when','whisper','wow','ylg-institut','zenvista','zovi']
brand_list=['ny-bae','nyassa','nycil','o3','organix','olay','old-spice','olivia','organic-harvest','organic-india','oriental-botanics','oxy','pac','paco-rabanne','palladio','palmer','palmolive','pantene','parachute','park-avenue','pears','petal-fresh','phy','physicians-formula','pilaten','playboy','plum','police','pollution-safe','ponds','pp','prada','prem-dulhan','purplle','purplle-membership','qraa','qraa-men','queenbe','qvs','ralph-lauren','remove','resme','revlon','richfeel','ring-guard','roberto-cavalli','roop-mantra','rude-cosmetic','s-t-dupont','saint-beard','salon-palette','salvatore-ferragamo','sandook-sutras','sara','schwarzkopf','schwarzkopf-professional','sergio-tacchini','set-wet','shany','simple','simply-straight','skincode','skinn','skore','specifix','st-d-venc','st-botanica','star-struck','statz','stay-quirky','sugar','sunsilk','swiss-beauty','swiss-image','thank-you-farmer','the-body-shop','the-moms-co','the-natures-co','thyme-organic','titan','tomford','tommy-hilfiger','toni-guy','tresemme','true-roots','ts','urban-swagger','ustraa','v-and-g','vaadi-herbals','vakola','vaseline','vayam','verdure-vegan-fragrances','versace','vipera','vit-citrus','vlcc','w.o.w','welocity','wet-n-wild','when','whisper','wow','ylg-institut','zenvista','zovi']
count_safety=0
for brand in brand_list:
    driver = webdriver.Chrome("C:/chromedriver")
    driver.get('https://www.purplle.com')
    count_safety+=1
    time.sleep(2)
    for pageno in range(1,100):
        # if pageno==1:
            # driver.get("https://www.purplle.com/api/shop/itemsv3?list_type=category&custom=&list_type_value={}&page={}&sort_by=rel&elite=0".format('makeup/face/bb-cc-cream',pageno))
        # else:
        #https://www.purplle.com/api/shop/itemsv3?list_type=brand&custom=&list_type_value=a-fragrance-story&page=1&sort_by=rel&elite=0
        driver.execute_script("window.open('https://www.purplle.com/api/shop/itemsv3?list_type=brand&custom=&list_type_value={}&page={}&sort_by=rel&elite=0');".format(brand,pageno))
        driver.switch_to.window(driver.window_handles[-1])
        # time.sleep(2)
        content = driver.page_source
        soup=BeautifulSoup(content)
        # if (soup.find('span',attrs={'class':'objectBox objectBox-string'}))!=None:
        #     if (soup.find('span',attrs={'class':'objectBox objectBox-string'})).text=='Error':
        #         break
        # print(soup.text)
        count_safety+=1
        if count_safety%40==1:
            time.sleep(10)
        dict1=json.loads(str(soup.text))
        if dict1['status']=='Error':
            break
        print(type(dict1))
        pth_new='C:\\Users\\bhara\\Desktop\\WebScraper\\Purplle\\{}'.format(brand)
        # os.mkdir(pth_new)
        # cwd=os.getcwd()
        # os.chdir(pth_new)
        with open(brand+str(pageno)+".json", "w") as write_file:
            json.dump(dict1, write_file)
        # os.chdir(cwd)
    driver.quit()
# print(x)