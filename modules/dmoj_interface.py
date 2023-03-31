import os
import pandas
from requests import session
import mechanize

class DMOJ:
    path = os.path.dirname(__file__)
    user_data_directory = path + os.sep + "cookies"
    username = str() 
    password = str() 
    loggedIn = False
    br = mechanize.Browser()
    loginURL = ""
    rootURL = ""
    name = ""

    def __init__(self, name = "", rootURL = "", loginURL = "") -> None:
        self.name = name 
        self.rootURL = rootURL 
        self.loginURL = loginURL
        pass

    def loadCredentialsFromCSV(self, filepath): 
        df = pandas.read_csv(filepath)
        for i in range(len(df)):
            if df.loc[i, 'Judge'] == self.name:
                self.username = df.loc[i, 'Handle'] 
                self.password = df.loc[i, 'Password'] 
                return 0 
        return -1 

    def login(self): 
        global loggedIn
        self.br.open(self.loginURL)
        if (res.url == self.rootURL):
            print ('Already logged in (probably).')
            loggedIn = True 
            return 0
        print(f'Logging in (detail: username="{self.username}", password="'+ ('*'*len(self.password)) +'")...')
        self.br.select_form(nr=0) 
        self.br.form['username'] = self.username 
        self.br.form['password'] = self.password
        res = self.br.submit()
        if res.url == self.rootURL:
            loggedIn = True
            print ('Logged in successfully.') 
            return 0
        print ('Loggin failed.')
        return -1