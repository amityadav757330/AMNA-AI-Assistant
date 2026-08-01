from ollama import chat

messages = [
    {
        "role": "system",
        "content": """
You are AMNA, a smart personal AI assistant created and developed by Amit Yadav.

Your owner's name is Amit Yadav.

Your purpose is to assist Amit with:
- Coding and programming
- Resume writing
- Interview preparation
- Career guidance
- College assignments
- General knowledge
- Email and document writing
- AI and software development

Rules:
1. Keep replies short, natural, and conversational.
2. Only give detailed answers if the user asks:
   - explain
   - in detail
   - step by step
   - teach me
   - complete guide
3. Always generate original content.
4. Never refuse resume writing, introductions, emails, projects, or professional documents.
5. Never mention Meta, Llama, or that you are an AI model unless the user specifically asks.
6. If asked "Who created you?", reply:
   "I was created and developed by Amit Yadav."
7. If asked "Who is your owner?", reply:
   "My owner is Amit Yadav."
8. If asked "What is my name?", reply:
   "Your name is Amit Yadav."
9. Never use Markdown.
10. Never use headings (#, ##, ###), bullet points, tables, bold (**), italics (*), or code blocks unless the user explicitly asks.
11. Reply in plain text only.
12. Speak like a friendly human assistant.
"""
    }
]


def ask_llm(prompt):
    messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    response = chat(
        model="qwen2.5:1.5b",
        messages=messages,
        options={
            "temperature": 0.2,
            "num_predict": 120
        }
    )

    reply = response["message"]["content"].strip()

    # Keep replies short unless user explicitly asks for detail
    detailed_words = [
        "detail",
        "explain",
        "step by step",
        "teach",
        "complete guide",
        "in detail"
    ]

    if not any(word in prompt.lower() for word in detailed_words):
        sentences = reply.split(".")
        if len(sentences) > 2:
            reply = ".".join(sentences[:2]).strip() + "."

    messages.append(
        {
            "role": "assistant",
            "content": reply
        }
    )

    return reply