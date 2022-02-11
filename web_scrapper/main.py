from indeed import get_jobs as get_indeed_jobs
from so import get_jobs as get_so_jobs
from save import save_to_file
from jobkorea import get_jobs as get_jobkorea_jobs

jobkorea_jobs = get_jobkorea_jobs()
so_jobs = get_so_jobs()
indeed_jobs = get_indeed_jobs()
jobs = so_jobs+indeed_jobs+jobkorea_jobs
save_to_file(jobs)
