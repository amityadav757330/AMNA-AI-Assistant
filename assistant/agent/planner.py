"""
=========================================
AMNA AI Assistant
Agent Planner
=========================================
"""

from assistant.agent.task import Plan, Task


class AgentPlanner:

    def create_plan(self, user_message):

        command = user_message.lower().strip()

        plan = Plan(goal=user_message)

        task_id = 1

        # ---------------------------------
        # Split multiple commands
        # ---------------------------------

        parts = command.replace(" then ", ",").split(",")

        for part in parts:

            part = part.strip()

            if not part:
                continue

            # -----------------------------
            # Open Application
            # -----------------------------

            if part.startswith("open "):

                app = part.replace("open ", "").strip()

                plan.add_task(
                    Task(
                        id=task_id,
                        description=f"Open {app}",
                        tool="system",
                        parameters={
                            "action": "open",
                            "target": app
                        }
                    )
                )

                task_id += 1
                continue

            # -----------------------------
            # Google Search
            # -----------------------------

            if part.startswith("google "):

                query = part.replace("google ", "").strip()

                plan.add_task(
                    Task(
                        id=task_id,
                        description=f"Google {query}",
                        tool="search",
                        parameters={
                            "engine": "google",
                            "query": query
                        }
                    )
                )

                task_id += 1
                continue

            # -----------------------------
            # YouTube Search
            # -----------------------------

            if part.startswith("youtube "):

                query = part.replace("youtube ", "").strip()

                plan.add_task(
                    Task(
                        id=task_id,
                        description=f"YouTube {query}",
                        tool="search",
                        parameters={
                            "engine": "youtube",
                            "query": query
                        }
                    )
                )

                task_id += 1
                continue

            # -----------------------------
            # Weather
            # -----------------------------

            if "weather" in part:

                city = (
                    part.replace("weather in", "")
                    .replace("weather", "")
                    .strip()
                )

                plan.add_task(
                    Task(
                        id=task_id,
                        description=f"Weather {city}",
                        tool="weather",
                        parameters={
                            "city": city
                        }
                    )
                )

                task_id += 1
                continue

            # -----------------------------
            # Default AI Task
            # -----------------------------

            plan.add_task(
                Task(
                    id=task_id,
                    description=part,
                    tool="ai",
                    parameters={
                        "prompt": part
                    }
                )
            )

            task_id += 1

        return plan