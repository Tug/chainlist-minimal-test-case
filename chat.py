import time
from uuid import uuid4

import chainlit as cl
from chainlit.types import ThreadDict


def setup_runnable():
    conversation_id = uuid4().hex
    cl.user_session.set("conversation_id", conversation_id)


@cl.on_chat_start
async def on_chat_start():
    current_timestamp = time.time()
    cl.user_session.set("last_updated", current_timestamp)
    setup_runnable()


@cl.on_chat_resume
async def on_chat_resume(thread: ThreadDict):
    setup_runnable()


@cl.on_message
async def on_message(message: cl.Message):
    cl.user_session.set("last_updated", time.time())
    msg = cl.Message(content="Received")

    await msg.send()
