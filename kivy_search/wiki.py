import wikipedia
import requests

page = wikipedia.page("chocolate")
link = page.images[0]

req = requests.get(link)
req.content

with open("chocolate.jpg", "wb") as file:
    file.write(req.content)
