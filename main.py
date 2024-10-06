from typing import Set
from core import run_llm
import streamlit as st
from streamlit_chat import message

st.header("🦜🔗 ChatBOT Prototype")
if (
    "chat_answers_history" not in st.session_state
    and "user_prompt_history" not in st.session_state
    and "chat_history" not in st.session_state
):
    st.session_state["chat_answers_history"] = []
    st.session_state["user_prompt_history"] = []
    st.session_state["chat_history"] = []


prompt = st.text_input("Question", placeholder="Enter your message here...") or st.button(
    "Submit"
)




if prompt:
    with st.spinner("Generating response..."):
        generated_response = run_llm(
            question=prompt, chat_history=st.session_state.chat_history
        )

        st.session_state.chat_history.append((prompt, generated_response))
        st.session_state.user_prompt_history.append(prompt)
        st.session_state.chat_answers_history.append(generated_response)


if st.session_state["chat_answers_history"]:
    for generated_response, user_query in zip(
        st.session_state["chat_answers_history"],
        st.session_state["user_prompt_history"],
    ):
        message(
            user_query,
            is_user=True,
        )
        message(generated_response)