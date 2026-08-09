from assistant.services.internet_service import (
    google_search,
    youtube_search,
    open_website,
    wiki_search,
    get_weather,
    latest_news,
)

from assistant.services.search_service import web_search


class SearchIntent:

    def handle(self, command, user):

        command = command.lower().strip()

        # ==========================================
        # WEATHER
        # ==========================================

        if command.startswith("weather in "):

            city = user[11:].strip()

            return get_weather(city)

        if command == "weather":

            return get_weather("Delhi")

        # ==========================================
        # WHO / WHAT
        # ==========================================

        if command.startswith("who is "):

            topic = user[7:].strip()

            return web_search(topic)

        if command.startswith("what is "):

            topic = user[8:].strip()

            return web_search(topic)

        if command.startswith("tell me about "):

            topic = user[14:].strip()

            return web_search(topic)

        # ==========================================
        # NEWS
        # ==========================================

        if "latest news" in command:
            return web_search("latest news")

        if "ai news" in command:
            return web_search("latest artificial intelligence news")

        if "technology news" in command:
            return web_search("latest technology news")

        # ==========================================
        # FINANCE
        # ==========================================

        if "bitcoin price" in command:
            return web_search("current bitcoin price")

        if "ethereum price" in command:
            return web_search("current ethereum price")

        if "gold price" in command:
            return web_search("today gold price")

        if "dollar rate" in command:
            return web_search("USD to INR exchange rate")

        # ==========================================
        # SPORTS
        # ==========================================

        if "cricket score" in command:
            return web_search("live cricket score")

        if "football score" in command:
            return web_search("live football score")

        if "ipl points table" in command:
            return web_search("latest IPL points table")

        # ==========================================
        # SEARCH
        # ==========================================

        if command.startswith("search "):

            query = user[7:].strip()

            return web_search(query)

        # ==========================================
        # GOOGLE SEARCH
        # ==========================================

        if command.startswith("google "):

            query = user[7:].strip()

            return google_search(query)

        if command.startswith("search google for"):

            query = command.replace("search google for", "").strip()

            return google_search(query)

        # ==========================================
        # YOUTUBE SEARCH
        # ==========================================

        if command.startswith("youtube "):

            query = user[8:].strip()

            return youtube_search(query)

        if command.startswith("search youtube for"):

            query = command.replace("search youtube for", "").strip()

            return youtube_search(query)

        # ==========================================
        # OPEN WEBSITE
        # ==========================================

        if command.startswith("open website "):

            website = user[13:].strip()

            return open_website(website)

        return None