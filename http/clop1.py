import requests
from bs4 import BeautifulSoup
import lxml

url1 = 'https://cataas.com/cat?type=original'
url2 = 'https://cataas.com/cat?type=original'
original_pik1 = requests.get(url1)
original_pik2 = requests.get(url2)
url3 = 'https://cataas.com/cat'
url4 = 'https://cataas.com/cat'
random_cat1 = requests.get(url3)
random_cat2 = requests.get(url4)
url5 = 'https://cataas.com/cat?filter=pixel'
url6 = 'https://cataas.com/cat?filter=pixel'
pixel_cat1 = requests.get(url5)
pixel_cat2 = requests.get(url6)
print(original_pik1, original_pik1, random_cat1, random_cat2, pixel_cat1, pixel_cat2)