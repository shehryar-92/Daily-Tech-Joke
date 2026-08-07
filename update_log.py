import urllib.request
import json
import datetime
import random

# Clean, safe backup jokes if the internet database fails
backup_jokes = [
    "💻 Tech Joke: There are 10 types of people: those who understand binary, and those who don't.",
    "💻 Tech Joke: Why do programmers wear glasses? Because they can't C#!",
    "💻 Tech Joke: ['hip', 'hip'] -> (hip hip array!)",
    "💻 Tech Joke: Clean code always looks like it was written by someone who cares."
]

try:
    # NOTE: the previous URL (https://jokeapi.dev) is the landing page, not
    # the API — it returns HTML, which always failed json.loads() and sent
    # every run into the backup-joke branch. This is the real API endpoint.
    url = "https://v2.jokeapi.dev/joke/Programming?blacklistFlags=nsfw,racist,sexist&type=single"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urllib.request.urlopen(req, timeout=10)

    raw_data = response.read().decode('utf-8')
    data = json.loads(raw_data)

    if data.get("error"):
        raise ValueError("JokeAPI returned an error response")

    if data.get("type") == "single":
        content = f"💻 Tech Joke: {data['joke']}"
    else:
        content = f"💻 Tech Joke:\nSetup: {data['setup']}\nDelivery: {data['delivery']}"

except Exception as e:
    content = f"{random.choice(backup_jokes)}\n[Note: Auto-recovered via local backup pool on {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} — reason: {e}]"

# This safely appends or creates the file
with open("tech_jokes.txt", "a", encoding="utf-8") as file:
    file.write(f"\n=========================\n{content}\n")

print("Successfully managed log entry generation workflow pipeline execution.")
