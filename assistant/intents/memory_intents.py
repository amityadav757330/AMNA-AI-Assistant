from assistant.services.memory_service import MemoryService

memory = MemoryService()


class MemoryIntent:

    def handle(self, command: str, user: str):

        command = command.lower().strip()

        # ==========================================
        # MANUAL PROFILE UPDATE
        # ==========================================

        if command.startswith("my name is "):

            name = user[11:].strip()

            memory.update_profile({
                "name": name
            })

            return f"Nice to meet you, {name}. I'll remember your name."

        if command.startswith("i study at "):

            college = user[11:].strip()

            memory.update_profile({
                "college": college
            })

            return f"I'll remember that you study at {college}."

        if command.startswith("i live in "):

            city = user[10:].strip()

            memory.update_profile({
                "city": city
            })

            return f"I'll remember that you live in {city}."

        if command.startswith("i'm from "):

            city = user[9:].strip()

            memory.update_profile({
                "city": city
            })

            return f"I'll remember that you are from {city}."

        if command.startswith("my favourite language is "):

            language = user[25:].strip()

            memory.update_profile({
                "favorite_language": language
            })

            return f"I'll remember your favourite language is {language}."

        if command.startswith("my favorite language is "):

            language = user[24:].strip()

            memory.update_profile({
                "favorite_language": language
            })

            return f"I'll remember your favorite language is {language}."

        if command.startswith("my favourite ide is "):

            ide = user[20:].strip()

            memory.update_profile({
                "favorite_ide": ide
            })

            return f"I'll remember your favourite IDE is {ide}."

        if command.startswith("my favorite ide is "):

            ide = user[19:].strip()

            memory.update_profile({
                "favorite_ide": ide
            })

            return f"I'll remember your favorite IDE is {ide}."

        if command.startswith("i love "):

            interest = user[7:].strip()

            memory.update_profile({
                "interest": interest
            })

            return f"I'll remember that you like {interest}."

        # ==========================================
        # PROFILE LOOKUP
        # ==========================================

        if command == "what is my name":

            profile = memory.get_profile()

            if profile.name:
                return f"Your name is {profile.name}."

            return "I don't know your name yet."

        if command == "where do i live":

            profile = memory.get_profile()

            if profile.city:
                return f"You live in {profile.city}."

            return "I don't know where you live."

        if command == "where do i study":

            profile = memory.get_profile()

            if profile.college:
                return f"You study at {profile.college}."

            return "I don't know where you study."

        if command == "what is my favourite language" or command == "what is my favorite language":

            profile = memory.get_profile()

            if profile.favorite_language:
                return f"Your favorite language is {profile.favorite_language}."

            return "I don't know your favorite language."

        if command == "what is my favourite ide" or command == "what is my favorite ide":

            profile = memory.get_profile()

            if profile.favorite_ide:
                return f"Your favorite IDE is {profile.favorite_ide}."

            return "I don't know your favorite IDE."

        if command == "show my profile":

            profile = memory.get_profile()

            return str(profile.to_dict())

        return None