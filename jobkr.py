import requests
from bs4 import BeautifulSoup

PERIOD = 4
URL = f'https://www.jobkorea.co.kr/Search/?stext=%ED%94%84%EB%A1%A0%ED%8A%B8%EC%97%94%EB%93%9C&tabType=recruit&period={PERIOD}'


def get_last_page():
    result = requests.get(URL)

    soup = BeautifulSoup(result.text, 'html.parser')

    pagination = soup.find(
        'div', class_='tplPagination newVer wide').find('ul').find_all('li')

    pages = []

    for page in pagination[1:]:
        anchor = page.find('a')
        pages.append(int(anchor['page-no']))

    max_page = pages[-1]
    return max_page


def extract_job(html):
    title = html.find(
        'div', class_='post-list-info').find('a', class_="title dev_view")
    company = html.find(
        'div', class_='post-list-corp').find('a', class_='name dev_view')
    location = html.find('span', class_='loc long')
    job_id = html['data-gno']
    if title != None and company != None and location != None:
        title = title['title']
        company = company.string
        location = location.string
        return {'title': title, 'company': company, 'location': location, 'link': f'https://www.jobkorea.co.kr/Recruit/GI_Read/{job_id}'}


def extract_jobs(last_pages=0):
    jobs = []
    for page in range(last_pages):
        # print(f'scrapping page {page+1}')
        result = requests.get(f'{URL}&Page_No={page + 1}')
        soup = BeautifulSoup(result.text, 'html.parser')

        results = soup.find_all('li', class_='list-post')
        for result in results:
            job = extract_job(result)
            if job != None:
                jobs.append(job)
    return jobs


def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs
