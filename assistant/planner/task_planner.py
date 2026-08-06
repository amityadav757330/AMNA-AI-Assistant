"""
=========================================
AMNA AI Assistant
Task Planner
=========================================
"""

from assistant.planner.task import Plan, Task


class TaskPlanner:

    def create_plan(self, user_message):

        command = user_message.lower().strip()

        plan = Plan()

        # ----------------------------------
        # Split Multiple Commands
        # ----------------------------------

        commands = (
            command
            .replace(" then ", "|")
            .replace(" and then ", "|")
            .replace(",", "|")
            .split("|")
        )

        for cmd in commands:

            cmd = cmd.strip()

            if not cmd:
                continue

            # ------------------------------
            # Open Applications
            # ------------------------------

            if cmd.startswith("open "):

                app = cmd.replace("open ", "").strip()

                plan.add(
                    Task(
                        name=f"Open {app}",
                        task_type="system",
                        data={
                            "action": "open",
                            "target": app
                        }
                    )
                )

                continue

            # ------------------------------
            # Google Search
            # ------------------------------

            if cmd.startswith("google "):

                query = cmd.replace("google ", "").strip()

                plan.add(
                    Task(
                        name="Google Search",
                        task_type="search",
                        data={
                            "engine": "google",
                            "query": query
                        }
                    )
                )

                continue

            # ------------------------------
            # YouTube Search
            # ------------------------------

            if cmd.startswith("youtube "):

                query = cmd.replace("youtube ", "").strip()

                plan.add(
                    Task(
                        name="YouTube Search",
                        task_type="search",
                        data={
                            "engine": "youtube",
                            "query": query
                        }
                    )
                )

                continue

            # ------------------------------
            # Weather
            # ------------------------------

            if cmd.startswith("weather in "):

                city = cmd.replace("weather in ", "").strip()

                plan.add(
                    Task(
                        name="Weather",
                        task_type="search",
                        data={
                            "weather": city
                        }
                    )
                )

                continue

            # ------------------------------
            # AI Task
            # ------------------------------

            plan.add(
                Task(
                    name="AI Response",
                    task_type="ai",
                    data={
                        "prompt": cmd
                    }
                )
            )

        return plan