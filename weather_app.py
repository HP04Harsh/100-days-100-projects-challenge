import requests

city = input("Enter city: ")
url = f"https://wttr.in/{city}?format=3"

res = requests.get(url)
print(res.text)