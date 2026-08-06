"""
=========================================
AMNA AI Assistant
AI Service
=========================================
"""

from assistant.planner.pipeline import PlanningPipeline


class AIService:

    def __init__(self):

        self.pipeline = PlanningPipeline()

    def ask(self, text, context=None):

        return self.pipeline.run(
            user_message=text,
            context=context
        )