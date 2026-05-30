from guardrails.safety import is_safe
import streamlit as st

from assistants.oss_assistant import generate_response as oss_response
from assistants.frontier_assistant import generate_response as frontier_response

from memory.vector_store import (
    store_memory,
    retrieve_memory
)

st.set_page_config(
    page_title="AI Assistant Comparison"
)

st.title("🤖 AI Assistant Comparison")

assistant_type = st.sidebar.selectbox(
    "Choose Model",
    ["OSS", "Frontier"]
)

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.write(msg["content"])

prompt = st.chat_input(
    "Ask something..."
)

if prompt:
    if not is_safe(prompt):
        st.error(
            "Unsafe request detected."
        )
        st.stop()

    memories = retrieve_memory(prompt)

    context = "\n".join(memories)

    enhanced_prompt = prompt

    st.session_state.messages.append(
        {
            "role": "user",
            "content": enhanced_prompt
        }
    )

    with st.chat_message("user"):
        st.write(prompt)

    if assistant_type == "OSS":

        answer = oss_response(
            st.session_state.messages
        )

    else:

        answer = frontier_response(
            st.session_state.messages
        )

    store_memory(prompt)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    with st.chat_message("assistant"):
        st.write(answer)