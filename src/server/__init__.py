from .api import app
import uvicorn


def server(host="127.0.0.1", port=9393):
    uvicorn.run(app, host=host, port=port)
