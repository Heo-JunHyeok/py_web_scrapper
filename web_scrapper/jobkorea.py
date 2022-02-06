import requests # python library보다 더 강력한 기능, url 가져오기
from bs4 import BeautifulSoup # HTML or XML에서 데이터 추출

JOBKOREA_URL="https://www.jobkorea.co.kr/Search/?stext=python"

def extract_jobkorea_pages():
    result=requests.get(JOBKOREA_URL)

    soup=BeautifulSoup(result.text,"html.parser")

    pagination=soup.find("div", {"class": "tplPagination newVer wide"}) # 웹 페이지 숫자 부분 코드 추출

    links=pagination.find_all('a')#링크 가져오기
    pages=[]

    for link in links[:-1]:
        pages.append(int(link.string)) # link.get('page-no')

    max_page=pages[-1]

    return max_page