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

        # ==========================================
        # Split Multiple Commands
        # ==========================================

        commands = (
            command
            .replace(" and then ", "|")
            .replace(" then ", "|")
            .replace(",", "|")
            .split("|")
        )

        for cmd in commands:

            cmd = cmd.strip()

            if not cmd:
                continue

            # ==========================================
            # Open Applications / System
            # ==========================================

            if cmd.startswith("open "):

                app = cmd.replace("open ", "", 1).strip()

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

            # ==========================================
            # Shutdown
            # ==========================================

            if "shutdown" in cmd:

                plan.add(
                    Task(
                        name="Shutdown",
                        task_type="system",
                        data={
                            "command": cmd
                        }
                    )
                )

                continue

            # ==========================================
            # Restart
            # ==========================================

            if "restart" in cmd:

                plan.add(
                    Task(
                        name="Restart",
                        task_type="system",
                        data={
                            "command": cmd
                        }
                    )
                )

                continue

            # ==========================================
            # Google Search
            # ==========================================

            if cmd.startswith("google "):

                query = cmd.replace("google ", "", 1).strip()

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

            # ==========================================
            # YouTube Search
            # ==========================================

            if cmd.startswith("youtube "):

                query = cmd.replace("youtube ", "", 1).strip()

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

            # ==========================================
            # Weather
            # ==========================================

            if cmd.startswith("weather in "):

                city = cmd.replace("weather in ", "", 1).strip()

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

            # ==========================================
            # Information
            # ==========================================

            if (
                cmd == "time"
                or cmd == "date"
                or "what is the time" in cmd
                or "what time is it" in cmd
                or "current time" in cmd
                or "what is the date" in cmd
                or "today's date" in cmd
                or "todays date" in cmd
                or "current date" in cmd
                or "who are you" in cmd
                or "who created you" in cmd
                or "who is your owner" in cmd
                or "tell me about yourself" in cmd
            ):

                plan.add(
                    Task(
                        name="Information",
                        task_type="info",
                        data={
                            "command": cmd
                        }
                    )
                )

                continue

            # ==========================================
            # Memory
            # ==========================================

            if (
                cmd.startswith("remember")
                or cmd.startswith("forget")
                or cmd.startswith("my name is")
                or cmd.startswith("i live in")
                or cmd.startswith("i study at")
            ):

                plan.add(
                    Task(
                        name="Memory",
                        task_type="memory",
                        data={
                            "command": cmd
                        }
                    )
                )

                continue

            # ==========================================
            # AI
            # ==========================================

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