from assistant.ai.reasoning.reasoner import Reasoner

reasoner = Reasoner()

tests = [
    "open google",
    "google python decorators",
    "remember my name is Amit",
    "what is my name",
    "what is the weather today",
    "explain polymorphism"
]

for query in tests:

    decision = reasoner.think(query)

    print("=" * 60)
    print("User:", query)
    print("Goal:", decision.goal)
    print("Intent:", decision.intent)
    print("Use Tool:", decision.use_tool)
    print("Tool:", decision.tool_name)
    print("Confidence:", decision.confidence)
    print("Reasoning:")

    for step in decision.reasoning:
        print(" -", step)