#Imports
from bottle import get, post, request, route, run
import jwt


@route('/login/<token>')
def login(token):
    try:
        user = jwt.decode(token, 'secret', algorithms=['HS256'])
        print(user['email'])
        return user
    except jwt.DecodeError as err:
        print(err)
        return ("Your token is invalid")

run(host='localhost', port=9000, debug=0, reloader=1)