"""
=========================================
AMNA AI Assistant
Agent Pipeline
=========================================
"""

from assistant.agent.planner import AgentPlanner
from assistant.agent.executor import AgentExecutor


class AgentPipeline:

    def __init__(self):

        self.planner = AgentPlanner()

        self.executor = AgentExecutor()

    def run(self, user_message, context=None):

        # ==========================================
        # Create Execution Plan
        # ==========================================

        plan = self.planner.create_plan(user_message)

        print("\n========== EXECUTION PLAN ==========")

        print(f"Goal: {plan.goal}")

        for task in plan.tasks:

            print(
                f"[{task.id}] "
                f"{task.description} "
                f"-> Tool: {task.tool}"
            )

        print("====================================\n")

        # ==========================================
        # Execute Plan
        # ==========================================

        response = self.executor.execute(
            plan=plan,
            context=context
        )

        return response