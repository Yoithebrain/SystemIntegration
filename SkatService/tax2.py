#Imports
#Bottle library used for the server to handle requests and running the server
from bottle import get, post, request, route, run
#SQLITE3 library for the SQLITE Database
import sqlite3 as sqlite
#Python-Jose library thats used for verifying and decoding JWT
import jose.jws as jws
import jose.jwt as jwt
#Json Library to return a json object in the response
import json as js
#connection variable
con = None
        
#Route for the server - to login and get data with the token
@route('/login/<token>')
def login(token):
    try:
        #Decode token into a variable
        user = jwt.decode(token, 'secret', algorithms=['HS256'])
        #print(user)
        #Variable to keep the email from the dictionary
        name = user['email']
        if (user['status'] == "Authenticated"):
            try:
                con = sqlite.connect("data.db")
                cur = con.cursor()
                #Statement to execute, using string formatting to automatically input our variable
                #instead of concatting the string later
                sql = f"SELECT balance FROM taxes WHERE name = '{name}'"
                #Cursor executes sql statement
                cur.execute(sql)
                #Cursor fetches one row from the resultset and we then make a Json object out of 
                #this
                balance = js.dumps(cur.fetchone()[0])
                #print(balance)
                return balance
            except ConnectionError as err:
                print(err)
        else:
            return ("Token is not authentic")
    except Exception as err:
        print(err)
        return (err)
    
    

run(host='localhost', port=9000, debug=0, reloader=1)