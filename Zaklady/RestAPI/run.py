from waitress import serve
from RestAPI import app
import os

# pip install Flask waitress

if __name__ == '__main__':
    # host='127.0.0.1'
    host='10.55.1.84'
    port=8080
    os.system("cls")
    print("Server start ", host , ":",  port )
    serve(app, host=host, port=port)