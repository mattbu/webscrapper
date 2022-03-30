import requests
from bs4 import BeautifulSoup

URL = f'https://stackoverflow.com/jobs?q=python'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36'}


def get_last_page():
    result = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(result.text, 'html.parser')
    pages = soup.find('div', class_='s-pagination').find_all('a')
    last_page = pages[-2].get_text(strip=True)
    return int(last_page)


def extract_job(html):
    # title = html.find('h2').find('a', class_='s-link stretched-link')
    title = html.find(
        'h2', class_='mb4 fc-black-800 fs-body3')
    company = html.find('h3', class_='fc-black-700 fs-body1 mb4')
    print(company)
    if title != None:
        title = title.find('a', class_='s-link stretched-link')['title']
    return {'title': title}


def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        result = requests.get(f'{URL}&pg={page + 1}', headers=HEADERS)
        soup = BeautifulSoup(result.text, 'html.parser')
        results = soup.find_all('div', class_='flex--item fl1')
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    # print(jobs)
    return jobs


def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs
