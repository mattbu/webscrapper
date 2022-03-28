from jobkr import extract_jobkr_pages, extract_jobkr_jobs

last_jobkr_page = extract_jobkr_pages()
print(last_jobkr_page, '라스트페이지')

jobkr_jobs = extract_jobkr_jobs(last_jobkr_page)

print(jobkr_jobs)
