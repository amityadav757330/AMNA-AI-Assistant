import re


class Extractor:

    def extract(self, text):

        text = text.strip()

        data = {}

        # My name is Amit
        match = re.search(r"my name is (.+)", text, re.IGNORECASE)
        if match:
            data["name"] = match.group(1).strip()

        # I'm from Meerut
        match = re.search(r"i(?: am|'m) from (.+)", text, re.IGNORECASE)
        if match:
            data["city"] = match.group(1).strip()

        # I study at GL Bajaj
        match = re.search(r"i study at (.+)", text, re.IGNORECASE)
        if match:
            data["college"] = match.group(1).strip()

        # I love Python
        match = re.search(r"i love (.+)", text, re.IGNORECASE)
        if match:
            data["interest"] = match.group(1).strip()

        # My favourite language is Python
        match = re.search(
            r"my (?:favorite|favourite) language is (.+)",
            text,
            re.IGNORECASE,
        )
        if match:
            data["favorite_language"] = match.group(1).strip()

        return data