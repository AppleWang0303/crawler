# 取得網頁原始碼
import urllib.request as req
url = "https://www.revrobotics.com/"
with req.urlopen(url) as respone:
    data=respone.read().decode("utf-8")
# 取得每篇文章標題
import bs4
root = bs4.BeautifulSoup(data,"html.parser")
product = root.find_all("div",class_="card-section card-section--body")
titles = root.find_all("h4" ,class_="card-title")
number = root.find_all("p",class_="card-text card-text--sku")
# print(number ,"\n", titles)
print(product,"\n")