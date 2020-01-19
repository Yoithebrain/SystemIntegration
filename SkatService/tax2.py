#Imports
from bottle import get, post, request, route, run
import jwt
import sqlite3 as sqlite

con = None

def getTaxBalance(name):
    try:
        con = sqlite.connect('data.db')
        cur = con.cursor()
        sql = f"SELECT balance FROM taxes WHERE name = '{name}';"
        cur.execute(sql)
        balance = cur.fetchone()[0]
        print(f"Taxes: {balance}")
        return balance
    except ConnectionError as error:
        return error
        

@route('/login/<token>')
def login(token):
    try:
        user = jwt.decode(token, 'secret', algorithms=['HS256'])
        name = user['email']
        userBalance = getTaxBalance(name)
        #print(userBalance)
        return userBalance
    except jwt.DecodeError as err:
        print(err)
        return ("Your token is invalid")

run(host='localhost', port=9000, debug=0, reloader=1)