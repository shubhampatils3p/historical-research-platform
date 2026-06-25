"""
base_agent.py

Version : 1.0.0

Base class for all agents in the Historical Research Platform.

Every future agent MUST inherit from BaseAgent.

Author:
Chief Architect
"""

from abc import ABC, abstractmethod
from datetime import datetime
from enum import Enum
from typing import Any, Dict, Optional

from pydantic import BaseModel, ConfigDict


# ==========================================================
# AGENT STATUS
# ==========================================================

class AgentStatus(str, Enum):
    CREATED = "created"
    INITIALIZED = "initialized"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"


# ==========================================================
# AGENT RESULT
# ==========================================================

class AgentResult(BaseModel):

    model_config = ConfigDict(extra="forbid")

    agent_name: str

    status: AgentStatus

    started_at: datetime

    finished_at: Optional[datetime] = None

    execution_time: Optional[float] = None

    records_processed: int = 0

    success: bool = True

    message: str = ""

    data: Dict[str, Any] = {}

    errors: list[str] = []


# ==========================================================
# BASE AGENT
# ==========================================================

class BaseAgent(ABC):

    """
    Every production agent must inherit this class.
    """

    def __init__(self):

        self.agent_name = self.__class__.__name__

        self.status = AgentStatus.CREATED

        self.started_at = None

        self.finished_at = None

    # -----------------------------------------------------

    def initialize(self):

        self.started_at = datetime.now()

        self.status = AgentStatus.INITIALIZED

        print(f"[{self.agent_name}] Initialized")

    # -----------------------------------------------------

    @abstractmethod
    def execute(self) -> AgentResult:
        """
        Main business logic.

        Must be implemented by every agent.
        """
        pass

    # -----------------------------------------------------

    def validate(self):

        """
        Optional validation.

        Override if required.
        """

        return True

    # -----------------------------------------------------

    def report(self, result: AgentResult):

        """
        Standard reporting.

        Override if required.
        """

        print("=" * 60)

        print(f"Agent : {result.agent_name}")

        print(f"Status : {result.status}")

        print(f"Success : {result.success}")

        print(f"Message : {result.message}")

        print("=" * 60)

    # -----------------------------------------------------

    def cleanup(self):

        self.finished_at = datetime.now()

        self.status = AgentStatus.COMPLETED

    # -----------------------------------------------------

    def run(self):

        """
        Standard execution pipeline.

        DO NOT override unless absolutely necessary.
        """

        self.initialize()

        self.validate()

        result = self.execute()

        self.report(result)

        self.cleanup()

        return result