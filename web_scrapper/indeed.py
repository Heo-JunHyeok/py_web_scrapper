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
    #for page in range(last_page):
    result=requests.get(f"{INDEED_URL}&start={0*LIMIT}")
    soup=BeautifulSoup(result.text,"html.parser")
    results=soup.find_all('a',{"class": "fs-unmask"}) # find_all: 조건에 맞는 모든 것 찾기
    for result in results:
        title=result.find("span",title=True).text # find: 조건에 처음으로 부합하는 것 찾기
        company=result.find("span",{"class": "companyName"}).string
        print(title,company)
    return jobs