import requests
import jwt
import json

easyID_url = 'http://localhost:80/login'
bank_url = 'http://localhost:8081/login'
skat_url = 'http://localhost:9000/login'

email = input("Enter email: ")
password = input("Enter password: ")
payload = {'email': email, 'password': password}

# EASYID REQUEST
easyID_token = requests.get(easyID_url, params=payload)

if easyID_token.status_code != 404:
    print('Token: ' + easyID_token.text)
    print()
    token_json = { 'token': easyID_token.text }

    # BANK REQUEST
    #bank_balance = requests.get(bank_url, params=token_json)    
    #print('Balance: ' + bank_balance.text + "DKK")

    # SKAT REQUEST
    skat_debt = requests.get(f"http://localhost:9000/login/{easyID_token.text}")
    print('Debt: ' + skat_debt.text + "DKK")
else:
    print("404 ERROR")
