# 取得網頁原始碼
import urllib.request as req
# url = "https://www.ptt.cc/bbs/movie/index.html"
# url = "https://www.andymark.com/categories/gearboxes"
# url = "https://www.andymark.com/"
url = "https://www.revrobotics.com/"
with req.urlopen(url) as respone:
    data=respone.read().decode("utf-8")
# 取得每篇文章標題
import bs4
root = bs4.BeautifulSoup(data,"html.parser")
titles = root.find_all("h4" ,class_="product-summary__name")
print(titles,end="\n")