import requests
from bs4 import BeautifulSoup
import csv

#key = input('please enter the term:')

url = 'https://www.hallogsm.com/hp/apple/'#.format(key)
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'

}

datas = []
#count_page = 0
#for page in range(1, 9):
    #count_page+=1
    #print('scraping page :',count_page)
req = requests.get(url, headers=headers)
soup = BeautifulSoup(req.text, 'html.parser')
items = soup.findAll('div', 'aps-product-box')

for item in items:
        nama = item.find('h2', 'aps-product-title').text.strip()
        harga = item.find('span', 'aps-price-value').text
        link_image = item.find('div', 'aps-product-thumb').find('img')['data-lazy-src']
        print(link_image)
        alt_item = item.find('div', 'aps-product-thumb').find('img')['alt']
        alt_item = str(alt_item).replace(' ', '-').replace('/', '').replace('*', '') + '.jpg'
        print(alt_item)
        datas.append([nama, harga, link_image])

head = ['Nama', 'Harga', 'Link Gambar']
write = csv.writer(open('iphone.csv', 'w', newline=''))
write.writerow(head)
for d in datas: write.writerow(d)
