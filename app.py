import os

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from agent_workflow import run_assurance


app = FastAPI(title="Agentic Motor Finance Remediation Assurance")


class CaseInput(BaseModel):
    agreement_details: str
    commission_evidence: str
    arrangement_classification: str
    disclosure_customer_evidence: str
    proposed_outcome: str
    reviewer_rationale: str


@app.get("/", response_class=HTMLResponse)
async def home():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()


@app.get("/health")
async def health():
    return {"status": "ok", "agentic_mode": bool(os.getenv("OPENAI_API_KEY"))}


@app.post("/api/review")
async def review_case(case: CaseInput):
    if not os.getenv("OPENAI_API_KEY"):
        raise HTTPException(
            status_code=503,
            detail="OPENAI_API_KEY is not set. Add it as an environment variable to run the live agentic workflow.",
        )

    try:
        result = await run_assurance(case.model_dump())
        return result.model_dump()
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Agentic review failed: {exc}") from exc
