import urllib.request as req
import bs4

def get_page(url):
    headers = {}
    request = req.Request(url=url, headers=headers)
    with req.urlopen(request) as respone:
        data = respone.read().decode("utf-8")
        return data

def parse_list_page(data):
    root = bs4.BeautifulSoup(data,"html.parser")
    titles = root.find_all("p", class_="product-summary__name")

    return list(map(lambda title: {'name': title.a.string, 'url': title.a['href']}, titles))

def parse_item_page(data):
    root = bs4.BeautifulSoup(data,"html.parser")
    product_detail = root.find("div", class_="product-details")
    title = product_detail.find("div", class_="product-details__name")
    number = product_detail.find("p", class_="product-details__id")
    price = product_detail.find("p", class_="product-prices__price")

    price_str = price.span.string.replace("\n", "")

    return title.h1.string, number.span.string, price_str

data = get_page("https://www.andymark.com/products/5-16-18-nylock-nut?via=Z2lkOi8vYW5keW1hcmsvV29ya2FyZWE6OkNhdGFsb2c6OkNhdGVnb3J5LzVhZjhkZmQxYmM2ZjZkNWUzNmYyMzdlYQ")

for item in parse_list_page(data):
    url = item['url']
    data = get_page(f'https://www.andymark.com{url}')
    print(parse_item_page(data))
