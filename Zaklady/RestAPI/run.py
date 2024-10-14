from waitress import serve
from RestAPI import app
import os

if __name__ == '__main__':
    host='127.0.0.1'
    os.system("cls")
    print("Server start ", host )
    serve(app, host=host, port=8080)