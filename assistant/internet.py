import webbrowser
from urllib.parse import quote
import requests


# ==========================================
# GOOGLE SEARCH
# ==========================================

def google_search(query):

    webbrowser.open(
        f"https://www.google.com/search?q={quote(query)}"
    )

    return f"Searching Google for {query}."


# ==========================================
# YOUTUBE SEARCH
# ==========================================

def youtube_search(query):

    webbrowser.open(
        f"https://www.youtube.com/results?search_query={quote(query)}"
    )

    return f"Searching YouTube for {query}."


# ==========================================
# OPEN WEBSITE
# ==========================================

def open_website(name):

    websites = {

        "google": "https://google.com",
        "youtube": "https://youtube.com",
        "github": "https://github.com",
        "chatgpt": "https://chat.openai.com",
        "gmail": "https://mail.google.com",
        "amazon": "https://amazon.in",
        "linkedin": "https://linkedin.com",
        "leetcode": "https://leetcode.com",
        "geeksforgeeks": "https://www.geeksforgeeks.org",
        "wikipedia": "https://wikipedia.org",

    }

    name = name.lower()

    if name in websites:

        webbrowser.open(websites[name])

        return f"Opening {name}."

    return "Website not found."


# ==========================================
# WIKIPEDIA
# ==========================================

def wiki_search(topic):

    try:

        url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{quote(topic)}"

        response = requests.get(url, timeout=5)

        if response.status_code != 200:
            return "I couldn't find information."

        data = response.json()

        if "extract" in data:
            return data["extract"]

        return "I couldn't find information."

    except Exception as e:

        print(e)

        return "Unable to connect to Wikipedia."


# ==========================================
# WEATHER
# ==========================================

def get_weather(city):

    try:

        response = requests.get(
            f"https://wttr.in/{quote(city)}?format=3",
            timeout=5
        )

        return response.text

    except:

        return "Unable to fetch weather."


# ==========================================
# NEWS
# ==========================================

def latest_news():

    webbrowser.open("https://news.google.com")

    return "Opening Google News."