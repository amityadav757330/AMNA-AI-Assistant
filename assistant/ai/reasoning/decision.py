"""
=========================================
AMNA AI Assistant
Decision Model
=========================================
"""

from dataclasses import dataclass, field
from typing import List


@dataclass
class Decision:
    """
    Stores the result of the reasoning process.
    """

    goal: str

    intent: str

    use_tool: bool

    tool_name: str = ""

    confidence: float = 1.0

    reasoning: List[str] = field(default_factory=list)