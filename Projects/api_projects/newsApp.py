
# Author: Maab
# Date: 2025-06-15
# Description: Fetches and displays the latest news articles based on user input using NewsAPI.


import requests       # For sending HTTP requests to the API

import json            # For working with JSON response data
query=input("What type of info you are interested in: ")
url=f"https://newsapi.org/v2/everything?q={query}&from=2025-05-16&sortBy=publishedAt&apiKey=da9e0dcf5a0f41c8a788d9987b2d6930"

# Send GET request to the News API
r=requests.get(url)

# Convert JSON response text into a Python dictionary
news=json.loads(r.text)

for article in news["articles"]:
    print (article["title"])               #print article
    print(article["description"])            #print short summary
    print("-------------------------")       #for formatting 
