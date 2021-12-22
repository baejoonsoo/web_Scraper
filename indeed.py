import requests
from bs4 import BeautifulSoup
from requests.api import request

LIMIT=50
URL=f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"

def extract_indeed_pages():
  result=requests.get(URL)
  soup=BeautifulSoup(result.text,"html.parser")
  pagination=soup.find('div',{"class":"pagination"})
  links=pagination.find_all('a')

  pages=[]
  for link in links[:-1]:
    # pages.append(link.find('span').string)
    pages.append(int(link.string))

  max_page=pages[-1]

  return max_page

def extract_indeed_jobs(last_page):
  for page in range(last_page):
    res=requests.get(f'{URL}&start={page*LIMIT}')
    soup=BeautifulSoup(res.text,"html.parser")
    results=soup.find_all('div',{"class":"slider_container"})
    
    titleList=[]
    for result in results:
      title=result.find("h2",{"class":"jobTitle"}).string
      if title:
        # titleList.append(title)
        print(title)

    # for title in titleList:
    #   print(title)
    print(f'===================================================== Page : {page}')