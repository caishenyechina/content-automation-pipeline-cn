from pathlib import Path
import logging
import time

from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel, Field, field_validator

from src.content_pipeline import generate_post, repurpose, plan_week
from src.settings import LOG_LEVEL

logging.basicConfig(level=getattr(logging, LOG_LEVEL.upper(), logging.INFO))
logger = logging.getLogger("content-pipeline-api")

app = FastAPI(title="Content Pipeline API", version="0.3.1")


@app.middleware("http")
async def log_requests(request: Request, call_next):
    start = time.perf_counter()
    response = await call_next(request)
    cost_ms = (time.perf_counter() - start) * 1000
    logger.info("%s %s -> %s (%.2fms)", request.method, request.url.path, response.status_code, cost_ms)
    return response


class GenerateRequest(BaseModel):
    topic: str = Field(..., min_length=1, max_length=200)

    @field_validator("topic")
    @classmethod
    def topic_not_blank(cls, v: str):
        if not v.strip():
            raise ValueError("topic must not be blank")
        return v


class RepurposeRequest(BaseModel):
    text: str = Field(..., min_length=1, max_length=5000)
    platform: str = Field(..., min_length=1, max_length=50)


class PlanRequest(BaseModel):
    topics: list[str] = Field(default_factory=list)


@app.get("/health")
def health():
    return {"ok": True, "service": "content-pipeline", "version": "0.3.1"}


@app.post("/generate")
def generate(req: GenerateRequest):
    try:
        return {"post": generate_post(req.topic)}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"generate failed: {e}")


@app.post("/repurpose")
def repurpose_api(req: RepurposeRequest):
    try:
        return {"post": repurpose(req.text, req.platform)}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"repurpose failed: {e}")


@app.post("/plan-week")
def plan(req: PlanRequest):
    try:
        out = Path("output/week-plan.md")
        out.parent.mkdir(parents=True, exist_ok=True)
        plan_week(req.topics, out)
        return {"path": str(out), "content": out.read_text(encoding="utf-8")}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"plan-week failed: {e}")
