from pydantic import BaseModel
from typing import List


class ComplianceViolation(BaseModel):
    section: str
    violation: str
    recommendation: str


class ComplianceResponse(BaseModel):
    violations: List[ComplianceViolation]
    summary: str
