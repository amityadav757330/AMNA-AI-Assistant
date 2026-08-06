"""
=========================================
AMNA AI Assistant
Task Executor
=========================================
"""

from assistant.intents.memory_intents import MemoryIntent
from assistant.intents.system_intents import SystemIntent
from assistant.intents.search_intents import SearchIntent
from assistant.intents.info_intents import InfoIntent
from assistant.intents.ai_intents import AIIntent


class Executor:

    def __init__(self):

        self.memory = MemoryIntent()
        self.system = SystemIntent()
        self.search = SearchIntent()
        self.info = InfoIntent()
        self.ai = AIIntent()

    def execute(self, plan, context=None):

        responses = []

        while not plan.finished():

            task = plan.next_task()

            if task is None:
                break

            result = self.execute_task(
                task=task,
                context=context
            )

            task.completed = True

            if result:
                responses.append(result)

        return "\n".join(responses)

    # ==========================================
    # Execute Individual Task
    # ==========================================

    def execute_task(self, task, context=None):

        # -----------------------------
        # System
        # -----------------------------

        if task.task_type == "system":

            target = task.data.get("target", "")

            return self.system.handle(
                command=f"open {target}"
            )

        # -----------------------------
        # Google Search
        # -----------------------------

        if (
            task.task_type == "search"
            and task.data.get("engine") == "google"
        ):

            return self.search.handle(
                command=f"google {task.data['query']}",
                user=f"google {task.data['query']}"
            )

        # -----------------------------
        # YouTube Search
        # -----------------------------

        if (
            task.task_type == "search"
            and task.data.get("engine") == "youtube"
        ):

            return self.search.handle(
                command=f"youtube {task.data['query']}",
                user=f"youtube {task.data['query']}"
            )

        # -----------------------------
        # Weather
        # -----------------------------

        if (
            task.task_type == "search"
            and "weather" in task.data
        ):

            city = task.data["weather"]

            return self.search.handle(
                command=f"weather in {city}",
                user=f"weather in {city}"
            )

        # -----------------------------
        # Memory
        # -----------------------------

        if task.task_type == "memory":

            command = task.data.get("command", "")

            return self.memory.handle(
                command=command.lower(),
                user=command
            )

        # -----------------------------
        # Info
        # -----------------------------

        if task.task_type == "info":

            command = task.data.get("command", "")

            return self.info.handle(
                command=command.lower()
            )

        # -----------------------------
        # AI
        # -----------------------------

        if task.task_type == "ai":

            return self.ai.handle(
                user=task.data["prompt"],
                context=context
            )

        return None