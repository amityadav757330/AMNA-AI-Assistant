"""
=========================================
AMNA AI Assistant
Planning Pipeline
=========================================
"""

from assistant.planner.task_planner import TaskPlanner
from assistant.planner.executor import Executor


class PlanningPipeline:

    def __init__(self):

        self.planner = TaskPlanner()

        self.executor = Executor()

    # ==========================================
    # Plan + Execute
    # ==========================================

    def run(self, user_message, context=None):

        plan = self.planner.create_plan(user_message)

        response = self.executor.execute(
            plan=plan,
            context=context
        )

        return response