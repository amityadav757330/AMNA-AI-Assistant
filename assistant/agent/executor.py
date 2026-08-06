"""
=========================================
AMNA AI Assistant
Agent Executor
=========================================
"""

from assistant.agent.tool_registry import ToolRegistry


class AgentExecutor:

    def __init__(self):

        self.registry = ToolRegistry()

    def execute(self, plan, context=None):

        responses = []

        while not plan.is_finished():

            task = plan.next_task()

            if task is None:
                break

            print(f"[Agent] Executing -> {task.description}")

            result = self.execute_task(
                task,
                context
            )

            task.status = "completed"

            if result:
                responses.append(result)

        return "\n".join(responses)

    # ==========================================
    # Execute One Task
    # ==========================================

    def execute_task(self, task, context):

        tool = self.registry.get(task.tool)

        if tool is None:
            return f"No tool registered for '{task.tool}'."

        # -----------------------------
        # System Tool
        # -----------------------------

        if task.tool == "system":

            command = f"open {task.parameters['target']}"

            return tool.handle(command)

        # -----------------------------
        # Search Tool
        # -----------------------------

        if task.tool == "search":

            engine = task.parameters["engine"]

            query = task.parameters["query"]

            command = f"{engine} {query}"

            return tool.handle(command, command)

        # -----------------------------
        # Memory Tool
        # -----------------------------

        if task.tool == "memory":

            command = task.parameters["command"]

            return tool.handle(command.lower(), command)

        # -----------------------------
        # Information Tool
        # -----------------------------

        if task.tool == "info":

            command = task.parameters["command"]

            return tool.handle(command)

        # -----------------------------
        # AI Tool
        # -----------------------------

        if task.tool == "ai":

            return tool.handle(
                user=task.parameters["prompt"],
                context=context
            )

        return None