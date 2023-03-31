import os
import pandas
from requests import session
import mechanize
from modules import dmoj_interface

vnoj = dmoj_interface.DMOJ(name="vnoj", rootURL="https://oj.vnoi.info/", loginURL="https://oj.vnoi.info/accounts/login/?next=/")

def loadCredentialsFromCSV(filepath): 
    return vnoj.loadCredentialsFromCSV(filepath=filepath)

def login(): 
    return vnoj.login()