import requests
from bs4 import BeautifulSoup

URL = f'https://stackoverflow.com/jobs/companies?q=python'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36'}


def get_last_page():
    result = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(result.text, 'html.parser')
    pages = soup.find('div', class_='s-pagination').find_all('a')
    last_page = pages[-2].get_text(strip=True)
    return int(last_page)


def remove_special_text(title):
    splited_title = title.split()
    new_titles = []
    for t in splited_title:
        new_titles.append(''.join(filter(str.isalnum, t)))
    return new_titles


def extract_job(html):
    title = html.find(
        'h2', class_='fs-body2 mb4')
    if title != None:
        title = title.find('a', class_='s-link').string
    location, company = html.find(
        'div', class_='d-flex gs12 gsx ff-row-wrap fs-body1').find_all('div')
    location = location.get_text(strip=True)
    company = company.get_text(strip=True)

    removed_spcial_text_job_id = remove_special_text(title)
    job_id = '-'.join(removed_spcial_text_job_id)
    return {'title': title, 'location': location, 'company': company, 'link': f'https://stackoverflow.com/jobs/companies/{job_id}'}


def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        # print(f'scrapping so: page: {page}')
        result = requests.get(f'{URL}&pg={page + 1}', headers=HEADERS)
        soup = BeautifulSoup(result.text, 'html.parser')
        results = soup.find_all('div', class_='flex--item fl1 text mb0')
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs


def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs
