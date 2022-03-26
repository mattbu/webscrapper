import requests
from bs4 import BeautifulSoup

indeed_result = requests.get(
    'https://kr.indeed.com/%EC%B7%A8%EC%97%85?as_and=python&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&salary=&radius')

indeed_soup = BeautifulSoup(indeed_result.text, 'html.parser')

# pagination = indeed_soup.find('div', {'class': 'pagination'})
pagination = indeed_soup.find('div', class_='pagination')
links = pagination.find_all('a')
# pages = pagination('a')
pages = []

for link in links[0:-1]:
    # pages.append(link.find('span').string)
    pages.append(int(link.string))
    # 앵커 안 요소에 string이 오직 하나 있다면 바로 .string으로 찾을 수 있다.

max_page = pages[-1]
