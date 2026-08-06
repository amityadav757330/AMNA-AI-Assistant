"""
=========================================
AMNA AI Assistant
Professional Browser Tool
=========================================
"""

import webbrowser
import urllib.parse

from assistant.tools.base import BaseTool


class BrowserTool(BaseTool):

    def execute(self, command):

        command = command.strip().lower()

        # ==========================================
        # Open Website
        # ==========================================

        if command.startswith("open "):

            website = command.replace("open ", "").strip()

            return self.open_website(website)

        # ==========================================
        # Google Search
        # ==========================================

        if command.startswith("google "):

            query = command.replace("google ", "").strip()

            return self.google_search(query)

        if command.startswith("search "):

            query = command.replace("search ", "").strip()

            return self.google_search(query)

        # ==========================================
        # YouTube Search
        # ==========================================

        if command.startswith("youtube "):

            query = command.replace("youtube ", "").strip()

            return self.youtube_search(query)

        # ==========================================
        # Wikipedia
        # ==========================================

        if command.startswith("wiki "):

            query = command.replace("wiki ", "").strip()

            return self.wikipedia_search(query)

        return "Browser Tool couldn't understand the command."

    # =====================================================
    # Open Website
    # =====================================================

    def open_website(self, website):

        websites = {

            "google": "https://www.google.com",

            "youtube": "https://www.youtube.com",

            "github": "https://github.com",

            "chatgpt": "https://chat.openai.com",

            "stackoverflow": "https://stackoverflow.com",

            "linkedin": "https://linkedin.com",

            "gmail": "https://mail.google.com",

            "facebook": "https://facebook.com",

            "instagram": "https://instagram.com",

            "x": "https://x.com",

            "twitter": "https://x.com"

        }

        if website in websites:

            url = websites[website]

        else:

            if "." not in website:

                website += ".com"

            if not website.startswith("http"):

                url = "https://" + website

            else:

                url = website

        webbrowser.open(url)

        return f"Opening {url}"

    # =====================================================
    # Google Search
    # =====================================================

    def google_search(self, query):

        url = (
            "https://www.google.com/search?q="
            + urllib.parse.quote(query)
        )

        webbrowser.open(url)

        return f"Searching Google for '{query}'."

    # =====================================================
    # YouTube Search
    # =====================================================

    def youtube_search(self, query):

        url = (
            "https://www.youtube.com/results?search_query="
            + urllib.parse.quote(query)
        )

        webbrowser.open(url)

        return f"Searching YouTube for '{query}'."

    # =====================================================
    # Wikipedia Search
    # =====================================================

    def wikipedia_search(self, query):

        url = (
            "https://en.wikipedia.org/wiki/Special:Search?search="
            + urllib.parse.quote(query)
        )

        webbrowser.open(url)

        return f"Searching Wikipedia for '{query}'."