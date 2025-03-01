from fastapi import FastAPI
from app.schemas import LLMResponse
from app.run_deepseek import run_deepseek

app = FastAPI()

@app.post('/generate_feedback', response_model=LLMResponse)
def generate_feedback_route(problem_data: dict, user_submission: str) -> LLMResponse:
    return run_deepseek(problem_data, user_submission)
