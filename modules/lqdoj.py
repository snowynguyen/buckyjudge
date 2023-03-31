import os
import pandas
from requests import session
import mechanize
from modules import dmoj_interface

lqdoj = dmoj_interface.DMOJ(name="lqdoj", rootURL="https://lqdoj.edu.vn/", loginURL="https://lqdoj.edu.vn/accounts/login/?next=/")

def loadCredentialsFromCSV(filepath): 
    return lqdoj.loadCredentialsFromCSV(filepath=filepath)

def login(): 
    return lqdoj.login()