from dotenv import load_dotenv
from .parser import MasadoraSuruga, Suruga
from .task import Task
from .scheduler import scheduler
from .server import server, app

load_dotenv()
