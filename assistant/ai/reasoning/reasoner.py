"""
=========================================
AMNA AI Assistant
Reasoner
=========================================
"""

from assistant.ai.reasoning.intent_classifier import IntentClassifier
from assistant.ai.reasoning.decision import Decision


class Reasoner:

    def __init__(self):

        self.classifier = IntentClassifier()

    def think(self, user_message: str):

        intent = self.classifier.classify(user_message)

        reasoning = []

        reasoning.append(f"Detected intent: {intent}")

        use_tool = False

        tool_name = ""

        # ==========================================
        # Browser
        # ==========================================

        if intent == "browser":

            use_tool = True

            tool_name = "BrowserTool"

            reasoning.append("Browser Tool selected.")

        # ==========================================
        # Memory
        # ==========================================

        elif intent == "memory":

            use_tool = True

            tool_name = "MemoryTool"

            reasoning.append("Memory Tool selected.")

        # ==========================================
        # System
        # ==========================================

        elif intent == "system":

            use_tool = True

            tool_name = "SystemTool"

            reasoning.append("System Tool selected.")

        # ==========================================
        # Weather
        # ==========================================

        elif intent == "weather":

            use_tool = True

            tool_name = "WeatherTool"

            reasoning.append("Weather Tool selected.")

        # ==========================================
        # Chat
        # ==========================================

        else:

            reasoning.append("LLM response required.")

        return Decision(

            goal=user_message,

            intent=intent,

            use_tool=use_tool,

            tool_name=tool_name,

            confidence=0.95,

            reasoning=reasoning

        )