from ddgs import DDGS


def web_search(query):

    try:
        with DDGS() as ddgs:

            results = list(ddgs.text(query, max_results=3))

            if not results:
                return "I couldn't find anything."

            answer = ""

            for result in results:

                title = result.get("title", "")
                body = result.get("body", "")

                answer += f"{title}\n{body}\n\n"

            return answer.strip()

    except Exception as e:

        print("Search Error:", e)

        return "Unable to search the internet."