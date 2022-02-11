import requests  # python library보다 더 강력한 기능, url 가져오기
from bs4 import BeautifulSoup  # HTML or XML에서 데이터 추출

URL = f"https://www.jobkorea.co.kr/Search/?stext=python"


def get_last_pages():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    last_page = soup.find(
        "div", {"class": "tplPagination newVer short clear"}).find("span", {"class": "pgTotal"}).string  # 웹 페이지 숫자 부분 코드 추출
    return int(last_page)
    # jobkorea는 페이지 소스에 total page가 명시되어 있어 그것만 추출하면 된다.


def extract_job(html):
    title = html.find("div", {"class": "post-list-info"}).find("a")["title"]
    company = html.find("div", {"class": "post-list-corp"}).find("a")["title"]
    location = html.find(
        "div", {"class": "post-list-info"}).find("span", {"class": "loc long"}).string
    job_id = html["data-gno"]
    return {'title': title, 'company': company, 'location': location, 'apply_link': f"https://www.jobkorea.co.kr/Recruit/GI_Read/{job_id}"}


def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping JobKorea: Page: {page+1}")
        result = requests.get(f"{URL}&tabType=recruit&Page_No={page+1}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find(
            "div", {"class": "list-default"}).find_all("li", {"class": "list-post"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs


def get_jobs():
    last_page = get_last_pages()
    jobs = extract_jobs(last_page)
    return jobs
