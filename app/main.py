from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(
    title="AI DevOps Automation Platform",
    description="Starter API for the AI DevOps portfolio project.",
    version="0.1.0",
)


class AskRequest(BaseModel):
    question: str


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/ask")
def ask_question(request: AskRequest) -> dict[str, str]:
    return {
        "question": request.question,
        "answer": "This is a placeholder response. AI integration will be added later.",
    }
