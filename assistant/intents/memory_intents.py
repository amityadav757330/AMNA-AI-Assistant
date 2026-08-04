from assistant.services.memory_service import MemoryService

memory = MemoryService()


class MemoryIntent:

    def handle(self, command: str, user: str):

        command = command.lower().strip()

        # -------------------------
        # Smart Memory
        # -------------------------

        if command.startswith("my name is "):

            name = user[11:].strip()

            memory.remember("name", name)

            return f"Nice to meet you, {name}. I'll remember your name."

        if command.startswith("i study at "):

            college = user[11:].strip()

            memory.remember("college", college)

            return f"I'll remember that you study at {college}."

        if command.startswith("i live in "):

            city = user[10:].strip()

            memory.remember("city", city)

            return f"I'll remember that you live in {city}."

        if command.startswith("my favourite language is "):

            language = user[25:].strip()

            memory.remember("favourite language", language)

            return f"I'll remember your favourite language is {language}."

        if command.startswith("my favorite language is "):

            language = user[24:].strip()

            memory.remember("favourite language", language)

            return f"I'll remember your favourite language is {language}."

        if command.startswith("my favourite ide is "):

            ide = user[20:].strip()

            memory.remember("favourite ide", ide)

            return f"I'll remember your favourite IDE is {ide}."

        if command.startswith("my favorite ide is "):

            ide = user[19:].strip()

            memory.remember("favourite ide", ide)

            return f"I'll remember your favourite IDE is {ide}."

        # -------------------------
        # Manual Memory
        # -------------------------

        if command.startswith("remember"):

            text = command.replace("remember", "", 1).strip()

            if " is " in text:

                key, value = text.split(" is ", 1)

                key = key.replace("my", "").strip()

                return memory.remember(key, value)

            return "Please say something like Remember my name is Amit."

        # -------------------------
        # Recall
        # -------------------------

        if command.startswith("what is my "):

            key = command.replace("what is my", "").replace("?", "").strip()

            value = memory.recall(key)

            if value:

                return f"Your {key} is {value}."

            return f"I don't remember your {key}."

        # -------------------------
        # Forget
        # -------------------------

        if command.startswith("forget my "):

            key = command.replace("forget my", "").strip()

            return memory.forget(key)

        # -------------------------
        # Show Memory
        # -------------------------

        if command == "show my memory":

            return memory.show_all_memory()

        if command == "clear memory":

            return memory.clear_all_memory()

        return None