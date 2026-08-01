from assistant.brain import reply

print("=" * 40)
print("       Welcome to AMNA AI")
print("Type 'exit' to quit")
print("=" * 40)

while True:
    user = input("\nYou : ")

    if user.lower() == "exit":
        print("AMNA: Goodbye!")
        break

    response = reply(user)

    print("AMNA:", response)