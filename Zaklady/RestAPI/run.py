from waitress import serve
from app import app
import os

# pip install Flask waitress

os.system("cls")

# Získání názvu počítače
hostname = os.environ['COMPUTERNAME']
print(f"Název počítače: {hostname}")

host = "10.55.1.84"
if(hostname == "MARTIN"):
    host = "192.168.1.32"
    # host = "127.0.0.1"
port = 80

print("Server start ", host , ":",  port )
serve(app, host=host, port=port)