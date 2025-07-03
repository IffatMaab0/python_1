
# Description: Fetches and displays the latest news articles based on user input using NewsAPI.


import requests       
import json  
import os
from dotenv import load_dotenv

load_dotenv()    
api_key = os.getenv("NEWS_API_KEY")      
query=input("What type of info you are interested in: ")
url=f"https://newsapi.org/v2/everything?q={query}&from=2025-05-16&sortBy=publishedAt&apiKey={api_key}"

print("API Key:", api_key)  

r=requests.get(url)

# Convert JSON response text into a Python dictionary
news=json.loads(r.text)
print(json.dumps(news, indent=4))


for article in news["articles"]:
    print (article["title"])               
    print(article["description"])            
    print("-------------------------")       
