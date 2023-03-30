import os
import pandas
from requests import session
import mechanize

path = os.path.dirname(__file__)
user_data_directory = path + os.sep + "cookies"
username = str() 
password = str() 
loggedIn = False
br = mechanize.Browser()
loginURL = "https://lqdoj.edu.vn/accounts/login/?next="
rootURL = "https://lqdoj.edu.vn/"

def loadCredentialsFromCSV(filepath): 
    df = pandas.read_csv(filepath)
    global username
    global password 
    for i in range(len(df)):
        if df.loc[i, 'Judge'] == 'lqdoj':
            username = df.loc[i, 'Handle'] 
            password = df.loc[i, 'Password'] 
            return 0 
    return -1 

def login(): 
    global loggedIn
    br.open(loginURL)
    if (res.url == rootURL):
        print ('Already logged in (probably).')
        loggedIn = True 
        return 0
    print(f'Logging in (detail: username="{username}", password="'+ ('*'*len(password)) +'")...')
    br.select_form(nr=0) 
    br.form['username'] = username 
    br.form['password'] = password
    res = br.submit()
    if res.url == rootURL:
        loggedIn = True
        print ('Logged in successfully.') 
        return 0
    print ('Loggin failed.')
    return -1