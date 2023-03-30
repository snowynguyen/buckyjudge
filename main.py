from modules import ntucoder, lqdoj
import os 

cwd = os.getcwd()
credentials_path = cwd + "/credentials.csv"
lqdoj.loadCredentialsFromCSV(credentials_path) 
lqdoj.login()
