import requests
from bs4 import BeautifulSoup

PERIOD = 3
URL = f'https://www.jobkorea.co.kr/Search/?stext=%ED%94%84%EB%A1%A0%ED%8A%B8%EC%97%94%EB%93%9C&tabType=recruit&period={PERIOD}'


def extract_jobkr_pages():
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


def extract_jobkr_jobs(last_pages=0):
    jobs = []
    # for page in range(last_pages):
    result = requests.get(f'{URL}&Page_No={0 + 1}')
    soup = BeautifulSoup(result.text, 'html.parser')

    job_list = soup.find_all('div', class_='post')
    for job in job_list:
        job_name = job.find(
            'div', class_='post-list-info').find('a', class_="title dev_view")
        if job_name != None:
            jobs.append(job_name['title'])
    return jobs
