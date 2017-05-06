from matplotlib import pyplot as plt
from bs4 import BeautifulSoup
import requests


url = "http://store.nike.com/tw/zh_tw/pw/%E7%94%B7%E6%AC%BE-%E9%9E%8B%E6%AC%BE/7puZoi3?ipp=120"
soup = BeautifulSoup(requests.get(url).text, 'html5lib')
"""
div = soup('div', 'grid-item fullSize')
print len(div)
"""

def Nike_info(div):
 title = div.find("p", "product-display-name nsg-font-family--base edf-font-size--regular nsg-text--dark-grey").text
 price = div.find('span', 'local nsg-font-family--base').text
 return {
 "title" : title,
 "price" : price
 }

Nikes=[]
for div in soup("div","grid-item-content"):
 Nikes.append(Nike_info(div))



prices=[]
for i in Nikes:
  prices.append(int(i["price"][4:9].replace(",","")))
#print len(prices)

titles=[]
for i in Nikes:
  titles.append(i["title"])
#print titles

"""
xs = [i for i, _ in enumerate(titles)]
plt.plot(xs, prices, color='green', marker='o', linestyle='solid')
plt.xticks([i  for i, _ in enumerate(titles)],titles)
plt.title("Nike")
plt.xlabel("Title")
plt.ylabel("Price")
plt.show()
"""
price6=[]
title6=[]

for i in range(6):
 price6.append(prices[i])
 title6.append(titles[i])
#print title10,price10

xa = [i for i, _ in enumerate(title6)]
plt.plot(xa, price6, color='green', marker='o', linestyle='solid')
plt.xticks([i  for i, _ in enumerate(title6)],title6)
plt.title("Nike")
plt.xlabel("Title")
plt.ylabel("Price")
plt.show()