from assistant.speech import listen

while True:
    text = listen()

    if text:
        print("Heard:", text)