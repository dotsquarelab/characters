import os

import streamlit as st
from dotenv import load_dotenv

from characters.utils import chat, get_model

CHARACTERS = ["Willy Wonka", "Jack Sparrow", "Gandalf"]
VERBOSE = os.getenv("VERBOSE", "0") == "1"


def main():
    st.title("AI Role Play")

    if "selected_character" not in st.session_state:
        st.session_state.selected_character = None

    if "chains" not in st.session_state:
        st.session_state.chains = {c: get_model(c, verbose=VERBOSE) for c in CHARACTERS}

    st.session_state.selected_character = st.selectbox(
        "Choose the character you are talking to:",
        CHARACTERS,
        placeholder="Select your character!",
    )
    st.write(f"You're now chatting with {st.session_state.selected_character}.")

    if "histories" not in st.session_state:
        initial_message = "Hi"
        st.session_state.histories = {
            c: [{"role": "User", "content": initial_message}] for c in CHARACTERS
        }

    # Display chat history
    for message in st.session_state.histories[st.session_state.selected_character]:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # User-provided prompt
    if prompt := st.chat_input(placeholder="Your message", disabled=False):
        st.session_state.histories[st.session_state.selected_character].append(
            {"role": "User", "content": prompt}
        )
        with st.chat_message("User"):
            st.write(prompt)

    last_message = st.session_state.histories[st.session_state.selected_character][-1]

    # AI response to user
    if last_message["role"] == "User":
        prompt = last_message["content"]

        with st.chat_message("Character"):
            with st.spinner("Thinking..."):
                response = chat(
                    st.session_state.chains[st.session_state.selected_character],
                    prompt,
                )
                st.write(response)

            st.session_state.histories[st.session_state.selected_character].append(
                {"role": "Character", "content": response}
            )


if __name__ == "__main__":
    load_dotenv()
    main()
