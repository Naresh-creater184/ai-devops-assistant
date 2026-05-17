import streamlit as st
import requests
import os

# Page setup
st.set_page_config(page_title="DevOps AI Assistant", page_icon="🤖")

st.title("🤖 DevOps AI Assistant")
st.write("Ask me anything about AWS, Terraform, Kubernetes, Docker, Jenkins, and Linux.")

# Ollama URL (works for both local + Docker)
OLLAMA_URL = os.getenv("OLLAMA_HOST", "http://ollama:11434")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
question = st.chat_input("Ask your DevOps question...")

if question:
    # Save user message
    st.session_state.messages.append({"role": "user", "content": question})

    with st.chat_message("user"):
        st.markdown(question)

    # System prompt
    system_prompt = """
You are a Senior DevOps Engineer.

You are an expert in:
- AWS
- Terraform
- Kubernetes
- Docker
- Jenkins
- Ansible
- Linux
- CI/CD

Give concise and practical answers with examples.
"""

    full_prompt = system_prompt + "\n\nUser Question:\n" + question

    # Assistant response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = requests.post(
                    f"{OLLAMA_URL}/api/generate",
                    json={
                        "model": "phi3",
                        "prompt": full_prompt,
                        "stream": False,
                        "options": {
                            "num_predict": 100
                        }
                    },
                    timeout=300
                )

                if response.status_code != 200:
                    st.error(response.text)
                answer = response.json().get("response", "No response received.")

                st.markdown(answer)

                # Save assistant response
                st.session_state.messages.append(
                    {"role": "assistant", "content": answer}
                )

            except Exception as e:
                st.error(f"Error: {e}")