import requests
from bs4 import BeautifulSoup
import os

path_folder = os.path.join(os.getcwd())

#key = input('please enter the term:')

url = 'https://www.hallogsm.com/hp/xiaomi/'#.format(key)
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'

}

try:
    os.makedirs('hasil_scraping') # folder create caranya
except:
    pass


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
        image = item.find('div', 'aps-product-thumb').find('img')['data-lazy-src']
        alt_item = item.find('div', 'aps-product-thumb').find('img')['alt']
        alt_item = str(alt_item).replace(' ', '-').replace('/', '').replace('*', '') + '.jpg'

        image = 'https://www.hallogsm.com/hp/xiaomi/{}'.format(image)

        with open('hasil_scraping/' + alt_item, 'wb') as f: #folder create caranya
            images = requests.get(image)
            print(f'Ambil Gambar dari Item {alt_item} Status Web:  {images.status_code}')
            f.write(images.content)
            f.close()
        print('Selesai')
