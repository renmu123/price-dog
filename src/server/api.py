from ..parser import MasadoraSuruga, Suruga, parserFactory
from ..scheduler import scheduler

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/parser/list")
def list_parser():
    return [MasadoraSuruga.name, Suruga.name]


class Job(BaseModel):
    name: str
    goods_id: str


@app.post("/job/add")
def add_job(job: Job):
    parser = parserFactory(job.name)
    scheduler.add_job(parser.parse, "interval", minutes=1, args=[job.goods_id])
