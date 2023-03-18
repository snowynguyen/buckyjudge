import bs4
import requests
import numpy
from collections import defaultdict

def getSolvedByUser(username):
    url = "http://ntucoder.net/Submission/CoderProblemSolved/" + username
    pageData = requests.get(url) 
    soup = bs4.BeautifulSoup(pageData.text, "lxml")
    elements = soup.find_all("tr")

    acprob = []
    for i,e in enumerate(elements):
        if i == 0: continue 
        cells = e.find_all("td")
        acprob.append(str(cells[3]).split("/")[3].split('"')[0])
    ans = [] 
    counted = defaultdict(str) 
    for p in acprob: 
        if p not in counted: 
            counted[p] = True 
            ans.append(p)
    return ans