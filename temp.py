import requests
from bs4 import BeautifulSoup

indeed_result = requests.get(
    'https://www.jobkorea.co.kr/Search/?stext=%ED%94%84%EB%A1%A0%ED%8A%B8%EC%97%94%EB%93%9C&period=3&tabType=recruit&Page_No=1')

# indeed_result = requests.get(
#     'https://kr.indeed.com/%EC%B7%A8%EC%97%85?as_and=python&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&salary=&radius')

indeed_soup = BeautifulSoup(indeed_result.text, 'html.parser')

# pagination = indeed_soup.find('div', {'class': 'pagination'})

pagination = indeed_soup.find(
    'div', class_='tplPagination newVer wide').find('ul').find_all('li')
# links = pagination.find_all('a')
# pages = pagination('a')
pages = []
for page in pagination[1:]:
    anchor = page.find('a')
    pages.append(int(anchor['page-no']))

# for link in links[0:-1]:
#     # pages.append(link.find('span').string)
#     pages.append(int(link.string))
#     # 앵커 안 요소에 string이 오직 하나 있다면 바로 .string으로 찾을 수 있다.

max_page = pages[-1]

for n in range(max_page):
    print(f'Page_No={n + 1}')
