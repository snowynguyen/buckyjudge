from modules import hnoj
import os 

cwd = os.getcwd()
credentials_path = cwd + "/credentials.csv"
hnoj.loadCredentialsFromCSV(credentials_path) 
hnoj.login()
