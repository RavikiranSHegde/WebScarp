import pandas as pd
import requests
from bs4 import BeautifulSoup
P_name=[]
Prise=[]
Description=[]
Reviews=[]


url="https://www.flipkart.com/search?q=mobile+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(2)

r = requests.get(url)
# print(r)

soup = BeautifulSoup(r.text, "lxml")
box=soup.find("div",class_ = "DOjaWF gdgoEp")

names = box.findAll("div",class_ = "KzDlHZ")
print(names)
for i in names:
    name=i.text
    P_name.append(name)
print(P_name)
print(len(P_name))

prices =box.findAll("div",class_ = "Nx9bqj _4b5DiR")
print(prices)

for i in prices:
    name=i.text
    Prise.append(name)
print(Prise)
print(len(Prise))

desc =box.findAll("ul",class_ = "G4BRas")

for i in desc:
    name=i.text
    Description.append(name)
print(Description)
print(len(Description))

reviews=box.findAll("div",class_ = "XQDdHH")

for i in reviews:
    name=i.text
    Reviews.append(name)
print(Reviews)
print(len(Reviews))

df=pd.DataFrame({"PRODUCT NAME":P_name,"PRISE":Prise,"DESCRIPTION":Description,"REVIEWS":Reviews})
print(df)

df.to_csv("C:/Users/Ravikiran S Hegde/Desktop/mobles_under_50000.csv")