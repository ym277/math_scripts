import requests
from bs4 import BeautifulSoup
import csv
import time

root_url = "http://ccdl.libraries.claremont.edu/"

# pg_url = "http://ccdl.libraries.claremont.edu/cdm/search/collection/fpc/page/21"
pg_url = "http://ccdl.libraries.claremont.edu/cdm/search/collection/fpc/order/title/page/2/display/200"
# pg_url = "http://ccdl.libraries.claremont.edu/cdm/search/collection/fpc/order/title/page/2/display/200"
# pg_url = "http://ccdl.libraries.claremont.edu/cdm/search/collection/fpc/page/2/order/title/ad/asc"
# title_1_url = "http://ccdl.libraries.claremont.edu/cdm/search/collection/fpc/order/title/ad/desc"
# title_2_url = "http://ccdl.libraries.claremont.edu/cdm/search/collection/fpc/order/title/ad/desc/page/2"
page = requests.get(pg_url)

pg_soup = BeautifulSoup(page.content, 'html.parser')
print(pg_soup.prettify())
    # print("\n\n")
    # continue

rows = pg_soup.find_all('li', class_='listItem')
# print(rows)
rows.pop(0)


    # out = open("attributes_txt/attributes"+"_"+str(pg)+".txt", "w")

for row in rows:
    ul = list(row.children)[1]
    blocks = list(ul.children)
    fst = blocks[1]
    snd = blocks[3]


    result = dict()

        # get image url
    a1 = fst.find('a', href=True)
    img_url = root_url + a1['href']
    segs = img_url.split('/')
    idx = segs[9]
    result["idx"] = idx
    print(idx)