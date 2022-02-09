import requests  # python library보다 더 강력한 기능, url 가져오기
from bs4 import BeautifulSoup  # HTML or XML에서 데이터 추출

LIMIT = 50
INDEED_URL = f"https://kr.indeed.com/jobs?q=python&limit={LIMIT}"


def get_last_page():
    result = requests.get(INDEED_URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find("div", {"class": "pagination"})  # 웹 페이지 숫자 부분 코드 추출
    links = pagination.find_all('a')  # 링크 가져오기
    pages = []
    for link in links[:-1]:
        pages.append(int(link.string))
    max_page = pages[-1]
    return max_page


def extract_job(html):
    # find: 조건에 처음으로 부합하는 것 찾기
    title = html.find("span", title=True).text
    company = html.find("span", {"class": "companyName"}).string
    # location=html.find("div",{"class": "recJobLoc"})["data-rc-loc"]: class이름에 recJobLoc이 존재하는 div로 변환 후 그 안에 있는 data-rc-Loc에 접근
    location = html.find("div", {"class": "companyLocation"}).text
    job_id = html["data-jk"]
    return {'title': title, 'company': company, 'location': location, 'link': f"https://www.indeed.com/viewjob?jk={job_id}&from=serp&vjs=3"}


def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping page {page+1}")
        result = requests.get(f"{INDEED_URL}&start={page*LIMIT}")
        soup = BeautifulSoup(result.text, "html.parser")
        # find_all: 조건에 맞는 모든 것 찾기
        results = soup.find_all('a', {"class": "fs-unmask"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs


def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs
