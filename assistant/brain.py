from assistant.tools import *
from assistant.llm import ask_llm
from assistant.memory import *
from assistant.internet import *
from assistant.search import web_search

# ==========================================
# COMMANDS
# ==========================================

COMMANDS = {

    # Identity
    "who are you": who_are_you,
    "who created you": who_created_you,
    "who is your owner": who_is_your_owner,
    "tell me about yourself": tell_about_amna,

    # Applications
    "open notepad": open_notepad,
    "open calculator": open_calculator,
    "open chrome": open_chrome,
    "open vscode": open_vscode,
    "open vs code": open_vscode,
    "open pycharm": open_pycharm,
    "open command prompt": open_cmd,
    "open cmd": open_cmd,
    "open powershell": open_powershell,
    "open file explorer": open_file_explorer,

    # Folders
    "open downloads": open_downloads,
    "open documents": open_documents,
    "open desktop": open_desktop,

    # Websites
    "open google": open_google,
    "open youtube": open_youtube,
    "open github": open_github,
    "open chatgpt": open_chatgpt,

    # System
    "shutdown": shutdown_pc,
    "restart": restart_pc,
    "cancel shutdown": cancel_shutdown,
    "lock pc": lock_pc,
}

# ==========================================
# MAIN BRAIN
# ==========================================

def reply(user):

    command = user.lower().strip()

    # ==========================================
    # SMART MEMORY
    # ==========================================

    if command.startswith("my name is "):
        name = user[11:].strip()
        remember("name", name)
        return f"Nice to meet you, {name}. I'll remember your name."

    if command.startswith("i study at "):
        college = user[11:].strip()
        remember("college", college)
        return f"I'll remember that you study at {college}."

    if command.startswith("i live in "):
        city = user[10:].strip()
        remember("city", city)
        return f"I'll remember that you live in {city}."

    if command.startswith("my favourite language is "):
        language = user[25:].strip()
        remember("favourite language", language)
        return f"I'll remember your favourite language is {language}."

    if command.startswith("my favorite language is "):
        language = user[24:].strip()
        remember("favourite language", language)
        return f"I'll remember your favourite language is {language}."

    if command.startswith("my favourite ide is "):
        ide = user[20:].strip()
        remember("favourite ide", ide)
        return f"I'll remember your favourite IDE is {ide}."

    if command.startswith("my favorite ide is "):
        ide = user[19:].strip()
        remember("favourite ide", ide)
        return f"I'll remember your favourite IDE is {ide}."

    # ==========================================
    # MANUAL MEMORY
    # ==========================================

    if command.startswith("remember"):

        text = command.replace("remember", "", 1).strip()

        if " is " in text:

            key, value = text.split(" is ", 1)

            key = key.replace("my", "").strip()

            return remember(key, value)

        return "Please say something like Remember my name is Amit."

    # ==========================================
    # RECALL MEMORY
    # ==========================================

    if command.startswith("what is my "):

        key = command.replace("what is my", "").replace("?", "").strip()

        value = recall(key)

        if value:
            return f"Your {key} is {value}."

        return f"I don't remember your {key}."

    # ==========================================
    # FORGET MEMORY
    # ==========================================

    if command.startswith("forget my "):

        key = command.replace("forget my", "").strip()

        return forget(key)

    # ==========================================
    # SHOW MEMORY
    # ==========================================

    if command == "show my memory":
        return show_all_memory()

    if command == "clear memory":
        return clear_memory()

    # ==========================================
    # TIME
    # ==========================================

    if "time" in command:
        return f"The current time is {get_time()}."

    # ==========================================
    # DATE
    # ==========================================

    if "date" in command:
        return f"Today's date is {get_date()}."

    # ==========================================
    # IP ADDRESS
    # ==========================================

    if "ip address" in command:
        return f"Your IP address is {get_ip()}."

    # ==========================================
    # WEATHER
    # ==========================================

    if command.startswith("weather in "):

        city = user[11:].strip()

        return get_weather(city)

    if command == "weather":

        return get_weather("Delhi")

    # ==========================================
    # INTERNET SEARCH (DDGS)
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

    if "ipl points table" in command:

        return web_search("latest IPL points table")

    if "football score" in command:

        return web_search("live football score")

    # ==========================================
    # PROGRAMMING SEARCH
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

    # ==========================================
    # YOUTUBE SEARCH
    # ==========================================

    if command.startswith("youtube "):

        query = user[8:].strip()

        return youtube_search(query)

    # ==========================================
    # OPEN WEBSITE
    # ==========================================

    if command.startswith("open website "):

        website = user[13:].strip()

        return open_website(website)

    # ==========================================
    # OLD SEARCH COMMANDS
    # ==========================================

    if command.startswith("search google for"):

        query = command.replace("search google for", "").strip()

        return google_search(query)

    if command.startswith("search youtube for"):

        query = command.replace("search youtube for", "").strip()

        return youtube_search(query)

    # ==========================================
    # BUILT-IN COMMANDS
    # ==========================================

    for keyword, function in COMMANDS.items():

        if keyword in command:

            return function()

    # ==========================================
    # AI FALLBACK
    # ==========================================

    return ask_llm(user)

