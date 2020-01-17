from bottle import route, run, request
import csv
import jwt

@route('/tax/<token>')
def bank(token):    
    try:
       user = jwt.decode(token, 'secret', algorithms=['HS256'])
       with open('usersTaxes.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if (row[0] == username):
                myString = row[1]
                checkedString = myString.startswith('-')
                if(checkedString == True):
                    return ("User " + row[0] + " owes the state: " + row[1])
                else:
                    return ("User " + row[0] + " is owned " + row[1] + " by the state")
    except jwt.DecodeError as err:
        print(err)
        return ("Your token is invalid")


run(host='localhost', port=2244, debug=0, reloader=1)