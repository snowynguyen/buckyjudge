import bs4
import requests
import numpy
import pandas
from collections import defaultdict
import mechanize 
import http.cookiejar

username = str() 
password = str()

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
    return sorted(ans)

loginURL = "http://ntucoder.net/Account/LogIn"

def loadCredentialsFromCSV(filepath): 
    df = pandas.read_csv(filepath)
    global username
    global password 
    for i in range(len(df)):
        if df.loc[i, 'Judge'] == 'ntucoder':
            username = df.loc[i, 'Handle'] 
            password = df.loc[i, 'Password'] 
            return 0 
    return -1 
