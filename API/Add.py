# Pridat zaznamy
import APIrequests as Api

for i in range(10):
    data = {"name": Api.randomSlovo(5), "popis": Api.randomSlovo(10)}
    Api.apiPost("http://localhost/api/elektro", data)

url = "http://localhost/api/elektro"
Pole = Api.apiAll(url)
for data in Pole:
    Api.apiDelete(url,data.id)
