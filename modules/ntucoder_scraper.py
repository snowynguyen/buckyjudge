import bs4
import requests
import numpy

def getSolvedByUser(username):
    url = "http://ntucoder.net/Submission/CoderProblemSolved/" + username
    pageData = requests.get(url) 
    soup = bs4.BeautifulSoup(pageData.text, "lxml")
    elements = soup.find_all("tr")

    ans = []
    for i,e in enumerate(elements):
        if i == 0: continue 
        cells = e.find_all("td")
        ans.append(str(cells[3]).split("/")[3].split('"')[0])

    return ans