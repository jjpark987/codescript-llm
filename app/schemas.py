from pydantic import BaseModel, Field
from typing import List

class LLMResponse(BaseModel):
    analysis: str
    suggestions: List[str]
    score: int = Field(..., ge=1, le=3)
