import os
from fastapi import FastAPI
from chainlit.utils import mount_chainlit

app = FastAPI(title="app")

mount_chainlit(
    app=app,
    target=os.path.join(os.path.dirname(__file__), "chat.py"),
    path="/chat",
)
