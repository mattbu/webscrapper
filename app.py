from jobkr import get_jobs as get_jobkr_jobs
from so import get_jobs as get_so_jobs

jobkr_jobs = get_jobkr_jobs()
so_jobs = get_so_jobs()
jobs = jobkr_jobs + so_jobs

print(jobs)
