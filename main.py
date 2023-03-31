from modules import ntucoder, vnoj
import os 

cwd = os.getcwd()
credentials_path = cwd + "/credentials.csv"
vnoj.loadCredentialsFromCSV(credentials_path) 
vnoj.login()
