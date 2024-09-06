import time
from uuid import uuid4

import chainlit as cl
from chainlit.types import ThreadDict


def setup_runnable():
    conversation_id = uuid4().hex
    cl.user_session.set("conversation_id", conversation_id)


# @cl.set_chat_profiles
# async def set_chat_profiles():
#     return [
#         cl.ChatProfile(
#             name="GPT-4o / ReAct / Prompt v1",
#             markdown_description="GPT4o + simple prompt",
#             icon="https://picsum.photos/200",
#         ),
#         cl.ChatProfile(
#             name="GPT-4o / ReAct / Prompt v2",
#             markdown_description="GPT-4o ZS + more complex prompt",
#             icon="https://picsum.photos/250",
#         ),
#         cl.ChatProfile(
#             name="GPT-4o / Multi-Agent v0",
#             markdown_description="GPT-4o ZS in a multi-agent system (experimental)",
#             icon="https://picsum.photos/300",
#         ),
#     ]


@cl.on_chat_start
async def on_chat_start():
    chat_profile = cl.user_session.get("chat_profile")
    await cl.Message(content=f'Profile de chat chargé: "{chat_profile}"').send()
    current_timestamp = time.time()
    cl.user_session.set("last_updated", current_timestamp)
    setup_runnable()


@cl.on_chat_resume
async def on_chat_resume(thread: ThreadDict):
    setup_runnable()


@cl.on_message
async def on_message(message: cl.Message):
    app_user = cl.user_session.get("user")
    cl.user_session.set("last_updated", time.time())
    conversation_id = cl.user_session.get("conversation_id")
    runnable = cl.user_session.get("runnable")
    msg = cl.Message(content="")

    await msg.send()
