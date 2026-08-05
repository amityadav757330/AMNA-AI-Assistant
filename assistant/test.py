from assistant.extractor import Extractor

extractor = Extractor()

tests = [
    "My name is Amit",
    "I'm from Meerut",
    "I study at GL Bajaj",
    "I love Python",
    "My favorite language is Python"
]

for text in tests:
    print(text)
    print(extractor.extract(text))
    print("-" * 40)