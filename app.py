from distutils.spawn import spawn
import requests
from bs4 import BeautifulSoup

indeed_result = requests.get(
    'https://kr.indeed.com/%EC%B7%A8%EC%97%85?as_and=python&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&salary=&radius')

indeed_soup = BeautifulSoup(indeed_result.text, 'html.parser')

# pagination = indeed_soup.find('div', {'class': 'pagination'})
pagination = indeed_soup.find('div', class_='pagination')
pages = pagination.find_all('a')
# pages = pagination('a')
spans = []


for page in pages:
    spans.append(page.find('span'))

spans = spans[:-1]
print(spans)
