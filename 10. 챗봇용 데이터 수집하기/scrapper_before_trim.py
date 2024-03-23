from bs4 import BeautifulSoup
import requests
import re
# https://www.musinsa.com/categories/item/001005?d_cat_cd=001005&brand=&list_kind=small&sort=pop_category&sub_sort=&page=1&display_cnt=90&exclusive_yn=&sale_goods=&timesale_yn=Y&ex_soldout=&plusDeliveryYn=&kids=&color=&price1=&price2=&shoeSizeOption=&tags=&campaign_id=&includeKeywords=&measure=
# (\w+)=[^\w+]

url = "https://www.musinsa.com/categories/item/001005"


params = {
# (\w+)=(\w+)&?
# "$1": "$2", \n
# 이후 url 마지막 ? 삭제
    "d_cat_cd": "001005", 
    "list_kind": "small", 
    "sort": "pop_category", 
    "page": "1", 
    "display_cnt": "90", 
    "timesale_yn": "Y", 

}

# 보기 - 개발자도구 - console - navigator.userAgent
# 200 응답
headers = {
    "user-agent": "'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'"
}

response = requests.get(url, params=params, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
list_box = soup.find("div", class_="list-box")
item_boxes = list_box.find_all("li", class_="li_box")
price_pattern = re.compile(r'[\d,]+원')


for item_box in item_boxes:
    item_title = item_box.find("p", class_="item_title").findChild("a")
    brand = item_title.text

    item_link = item_box.find("p", class_="list_info").findChild("a")
    #print(item_link.text.strip())
    name = item_link.text.strip()
    url = item_link["href"]

    item_price = item_box.find("p", class_="price")
    #print(item_price.text)
    prices = price_pattern .findall(item_price.text)

    img_box = item_box.find("div", class_="list_img").find("img")
    #print(img_box["data-original"])
    #prices = re.findall(r'[\d,]+원', item_price.text) 컴파일로(33줄)
    #print(prices)

    item = {
        "brand": brand,
        "name": name,
        "url": "https:" + url,
        "original_price": prices[0],
        "sale_price": prices[1],
        "image": img_box["data-original"]
    }
    #print(item)
#    print(item)
    print(item)
#print(len(item_boxes))

#print(list_box)

#print(response.status_code)
#print(response.text)

