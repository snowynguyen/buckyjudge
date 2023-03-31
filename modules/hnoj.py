import os
import pandas
from requests import session
import mechanize
from modules import dmoj_interface

vnoj = dmoj_interface.DMOJ(name="hnoj", rootURL="https://hnoj.edu.vn/", loginURL="https://hnoj.edu.vn/accounts/login/?next=/")

def loadCredentialsFromCSV(filepath): 
    return vnoj.loadCredentialsFromCSV(filepath=filepath)

def login(): 
    return vnoj.login()