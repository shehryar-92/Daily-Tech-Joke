import urllib.request
import json

try:
    url = "https://jokeapi.dev"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urllib.request.urlopen(req, timeout=10)
    data = json.loads(response.read().decode())
    
    if data.get("type") == "single":
        content = f"💻 Tech Joke: {data['joke']}"
    else:
        content = f"💻 Tech Joke:\nSetup: {data['setup']}\nDelivery: {data['delivery']}"
        
    with open("tech_jokes.txt", "a", encoding="utf-8") as file:
        file.write(f"\n=========================\n{content}\n")
    print("Successfully updated tech_jokes.txt")
    
except Exception as e:
    print(f"Error fetching joke: {e}")
