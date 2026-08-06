"""
=========================================
AMNA AI Assistant
Tool Result
=========================================
"""

from dataclasses import dataclass
from typing import Any


@dataclass
class ToolResult:

    success: bool

    output: Any = None

    error: str = ""

    metadata: dict = None

    @classmethod
    def ok(cls, output=None, metadata=None):

        return cls(
            success=True,
            output=output,
            metadata=metadata or {}
        )

    @classmethod
    def fail(cls, error):

        return cls(
            success=False,
            error=error,
            metadata={}
        )