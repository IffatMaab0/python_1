import requests
import json
query=input("What type of info you are interested in: ")
url=f"https://newsapi.org/v2/everything?q={query}&from=2025-05-16&sortBy=publishedAt&apiKey=da9e0dcf5a0f41c8a788d9987b2d6930"
r=requests.get(url)

news=json.loads(r.text)
for article in news["articles"]:
    print (article["title"])
    print(article["description"])
    print("-------------------------")
