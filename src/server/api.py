from ..parser import MasadoraSuruga, Suruga, parserFactory
from ..scheduler import scheduler

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/parser/list")
def list_parser():
    return [MasadoraSuruga.name, Suruga.name]


class Job(BaseModel):
    site: str
    goods_id: str


@app.post("/job/add")
def add_job(job: Job):
    parser = parserFactory(job.site)
    job = scheduler.add_job(parser.parse, "cron", minute="1", hour="0", day="*/1", args=[job.goods_id])
    return {"id": job.id}


@app.get("/job/list")
def list_job():
    return scheduler.get_jobs()


@app.post("/job/remove")
def remove_job(job_id: str):
    scheduler.remove_job(job_id)
    return {"id": job_id}
