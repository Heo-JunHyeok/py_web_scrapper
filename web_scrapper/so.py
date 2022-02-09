from genericpath import exists
from operator import truediv
import requests  # python library보다 더 강력한 기능, url 가져오기
from bs4 import BeautifulSoup  # HTML or XML에서 데이터 추출

# 1. 페이지 가져오기
# 2. request 만들기
# 3. job 추출하기

URL = f"https://stackoverflow.com/jobs?q=python"


def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find("div", {"class": "s-pagination"}).find_all("a")
    last_page = pages[-2].get_text(strip=True)  # strip으로 whiteblock지우기
    return int(last_page)


def extract_job(html):
    title = html.find(
        "h2", {"class": "mb4 fc-black-800 fs-body3"}).find("a")["title"]
    company, location = html.find(
        "h3", {"class": "fc-black-700 fs-body1 mb4"}).find_all("span", recursive=False)
    company = company.get_text(strip=True)
    location = location.get_text(strip=True)
    job_id = html["data-jobid"]
    return {'title': title, 'company': company, 'location': location, 'apply_link': f"https://stackoverflow.com/jobs/{job_id}"}


def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f"Scarapping SO: Page: {page+1}")
        result = requests.get(f"{URL}&pg={page+1}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "-job"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs


def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs
