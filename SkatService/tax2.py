#Imports
from bottle import get, post, request, route, run
import sqlite3 as sqlite
import jose.jws as jws
import jose.jwt as jwt

con = None

def getTaxBalance(name):
    try:
        con = sqlite.connect('data.db')
        cur = con.cursor()
        sql = f"SELECT balance FROM taxes WHERE name = '{name}'"
        cur.execute(sql)
        balance = cur.fetchone()[0]
        #print(f"Taxes: {balance}")
        return balance
    except Exception as error:
        return error
        

@route('/login/<token>')
def login(token):
    try:
        user = jwt.decode(token, 'secret', algorithms=['HS256'])
        print(user)
        name = user['email']
        #userBalance = getTaxBalance(user['email'])
        #print(userBalance)
        try:
            con = sqlite.connect("data.db")
            cur = con.cursor()
            sql = f"SELECT balance FROM taxes WHERE name = '{name}'"
            cur.execute(sql)
            balance = cur.fetchone()[0]
            print(balance)
            return str(balance)
        except ConnectionError as err:
            print(err)
    except Exception as err:
        print(err)
        return (err)
    
    

run(host='localhost', port=9000, debug=0, reloader=1)