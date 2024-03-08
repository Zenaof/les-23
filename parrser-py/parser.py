import requests
from bs4 import BeautifulSoup

url = 'https://dedmorozural.ru/'

resp = requests.get(url)
print(resp.status_code)
#print(resp.text)

soup = BeautifulSoup(resp.text, 'html.parser')
#print(soup.title)
#print(soup.a)
print(soup.a.string)

# images_tags = soup.find_all('img')
# for images_tag in images_tags:
#     print(images_tag)
#
# a_tags = soup.find.all('a')
# for a_tag in a_tags:
#     print(a_tag)

big_body_div = soup.find('div', class_ = 'modulebody1')
print(big_body_div)