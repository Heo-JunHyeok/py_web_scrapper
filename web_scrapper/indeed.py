import requests # python library보다 더 강력한 기능, url 가져오기
from bs4 import BeautifulSoup # HTML or XML에서 데이터 추출

LIMIT=50
INDEED_URL=f"https://kr.indeed.com/jobs?q=python&limit={LIMIT}"

def extract_indeed_pages():
    result=requests.get(INDEED_URL)
    soup=BeautifulSoup(result.text,"html.parser")
    pagination=soup.find("div", {"class": "pagination"}) # 웹 페이지 숫자 부분 코드 추출
    links=pagination.find_all('a')#링크 가져오기
    pages=[]
    for link in links[:-1]:
        pages.append(int(link.string))
    max_page=pages[-1]
    return max_page

def extract_indeed_jobs(last_page):
    jobs=[]
    for page in range(last_page):
        result=requests.get(f"{INDEED_URL}&start={page*LIMIT}")
        print(result.status_code)
    return jobs