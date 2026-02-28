from fastapi import FastAPI
from pydantic import BaseModel
from pathlib import Path

from content_pipeline import generate_post, repurpose, plan_week

app = FastAPI(title="Content Pipeline API", version="0.2.0")


class GenerateRequest(BaseModel):
    topic: str


class RepurposeRequest(BaseModel):
    text: str
    platform: str


class PlanRequest(BaseModel):
    topics: list[str]


@app.get("/health")
def health():
    return {"ok": True}


@app.post("/generate")
def generate(req: GenerateRequest):
    return {"post": generate_post(req.topic)}


@app.post("/repurpose")
def repurpose_api(req: RepurposeRequest):
    return {"post": repurpose(req.text, req.platform)}


@app.post("/plan-week")
def plan(req: PlanRequest):
    tmp_topics = Path("output/tmp_topics.txt")
    tmp_topics.parent.mkdir(parents=True, exist_ok=True)
    tmp_topics.write_text("\n".join(req.topics), encoding="utf-8")

    out = Path("output/week-plan.md")
    plan_week(req.topics, out)
    return {"path": str(out), "content": out.read_text(encoding="utf-8")}
