#!/usr/bin/env python
# coding: utf-8



import requests
from bs4 import BeautifulSoup
import smtplib
import re
import time
from urllib.request import Request


# ## PART 1.2
# 

# ### (a)


url_sold = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=amazon+gift+card&_sacat=0&LH_Sold=1&rt=nc&_pgn=1" # URL for sold "amazon gift card"
header = {'User-agent': 'Mozilla/5.0'} 
response = requests.get(url_sold, headers=header) #Send a GET request to sold "amazon gift card" URL
webcontent_sold = response.content #Returns the content of the 'response', named as "webcontent_sold"
f = open(f'amazon_gift_card_01.htm','wb') # Open a file called "amazon_gift_card_01.htm" and write it in Binary mode 
f.write(webcontent_sold) # wite "webcontent_sold" in the file
f.close() #Close the opening file


# ### (b)


for i in range(1,11):
    url_sold_pn = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=amazon+gift+card&_sacat=0&LH_Sold=1&rt=nc&_pgn=" + str(i) #str(i) refer to the page number
    header = {'User-agent': 'Mozilla/5.0'} 
    response_pn = requests.get(url_sold_pn, headers=header)
    webcontent_sold_pn = response_pn.content
    f = open(f'amazon_gift_card_{i}.htm','wb') 
    f.write(webcontent_sold_pn) 
    f.close()
    time.sleep(10)# make sure each page request is followed by a 10 second pause


# ### (c)


for i in range (1,11):
    with open (f'amazon_gift_card_{i}.htm') as file:
        soup = BeautifulSoup(file, 'lxml')
        
        


# ### (d)


for i in range (1,11):
    with open (f'amazon_gift_card_{i}.htm') as file:
        soup = BeautifulSoup(file, 'lxml')
        lists = soup.find_all('li', class_='s-item')
        for j in lists:
            title = j.find('div', class_='s-item__title')
            price = j.find('span', class_='s-item__price')
            shipping = j.find('span', class_='s-item__shipping s-item__logisticsCost')
            if shipping:
                shipping = shipping.text
            else:
                shipping = 'Free Shipping'
            if 'Shop on eBay' not in title.text:
                print("Item title:",title.text,'\n'+"Pice:",price.text+'\n'+"Shipping price:"+shipping)


# ### (e)

for i in range (1,11):
    with open (f'amazon_gift_card_{i}.htm') as file:
        soup = BeautifulSoup(file, 'lxml')
        lists = soup.find_all('li', class_='s-item')
        for j in lists:
            title = j.find('div', class_='s-item__title')
            price = j.find('span', class_='s-item__price')
            shipping = j.find('span', class_='s-item__shipping s-item__logisticsCost')
            if shipping:
                shipping = shipping.text
            else:
                shipping = 'Free Shipping'
            if 'Shop on eBay' not in title.text:
                title_num = re.findall(r'\d+',title.text)
                if len(title_num) > 0:
                    face_value = max(title_num)
                else:
                    face_value = 0
                    
                price_num = re.findall(r'\d+.\d+',price.text)
                if len(price_num) > 0:
                    price_num = max(price_num)
                else:
                    price_num = 0
                    
                if len(shipping) >0 :
                    shipping = shipping
                else:
                    shipping = 0
                shipping_num = re.findall(r'\d+.\d+',shipping)
                if len(shipping_num) > 0:
                    shipping_num = max(shipping_num)
                else:
                    shipping_num = 0   
                    
                selling_price = float(price_num) + float(shipping_num)
                if float(face_value) < selling_price:
                    print("face price:" , face_value, "selling price:", selling_price, "price:", price_num, "shipping:",  shipping_num)
                
                
# ### (f)
print("Gift card with face value under 100 are more possible to be sold above face value."+'\n'+
      "I think the reason might be people might have a eBay gift card, but they think things in Amazon are better than eBay."+'\n'+
      "Hencen, they would like to use the eBay gift card to buy a Amazon one, and people are might be more likely to have a under $100 eBay gift card")

# ## Part 2.2

# ### (a)


url_fctable = "https://www.fctables.com/user/login/"
page1 = requests.get(url_fctable)
header={"User-Agent": "Mozilla/5.0"}
payload = {"login_action" : "1",
           "login_username" : "Edith",
           "login_password" : "a123456",
           "user_remeber":"1",
           "submit":"1"}
session_requests = requests.session()

response = session_requests.post(url_fctable,headers = header, data =payload)
i = session_requests.cookies.get_dict()

print(i)
print(response)


# ### (b) 

url_2 ="https://www.fctables.com/tipster/my_bets/"
header={"User-Agent": "Mozilla/5.0"}
response_2 = session_requests.get(url_2, headers = header, cookies=i)
doc2 = BeautifulSoup(response_2.content, 'html.parser')


if "Wolfsburg" in response_2.text:
    print("Yes,'Wolfsburg' appears on the page")
else:
    print("Failed")




