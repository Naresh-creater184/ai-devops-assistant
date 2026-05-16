# 🤖 AI-Powered DevOps Assistant

An AI chatbot that answers DevOps questions and generates infrastructure code using:

* Python
* Streamlit
* Ollama
* Llama 3

The assistant can answer questions related to:

* AWS
* Terraform
* Kubernetes
* Docker
* Jenkins
* Ansible
* Linux
* CI/CD

---

## 🚀 Features

* ChatGPT-style interface
* Local LLM execution using Ollama
* No API cost
* DevOps-focused prompt engineering
* Generates Terraform, Dockerfile, Kubernetes YAML, and Jenkins pipelines
* Maintains chat history

---

## 🛠️ Tech Stack

| Layer       | Technology |
| ----------- | ---------- |
| Frontend    | Streamlit  |
| Backend     | Python     |
| LLM Runtime | Ollama     |
| LLM Model   | Llama 3    |
| HTTP Client | requests   |

---

## 🏗️ Architecture

```text
User
  ↓
Streamlit UI
  ↓
Python Application
  ↓
Ollama API (localhost:11434)
  ↓
Llama 3
  ↓
AI Response
```

---

## 📂 Project Structure

```text
ai-devops-assistant/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── venv/
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Naresh-creater184/ai-devops-assistant.git
cd ai-devops-assistant
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

**Windows:**

```powershell
venv\Scripts\activate
```

**Linux/macOS:**

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Install Ollama

Download from: [https://ollama.com](https://ollama.com)

### 6. Download Llama 3

```bash
ollama pull llama3
```

### 7. Run the Application

```bash
streamlit run app.py
```

---

## 💬 Sample Questions

* What is Terraform?
* Generate Terraform code for an EC2 instance.
* Explain Kubernetes Deployment vs StatefulSet.
* Create a Dockerfile for a Python application.
* Write a Jenkins pipeline for CI/CD.
* Explain Ansible inventory.

---

## 🧠 Example Resume Bullet

Built an AI-powered DevOps Assistant using Python, Streamlit, Ollama, and Llama 3 to answer AWS, Terraform, Kubernetes, and CI/CD questions and generate infrastructure-as-code templates.

---

## 📸 Suggested Screenshots

Add screenshots of:

1. Chat interface
2. Terraform code generation
3. Kubernetes explanation

---

## 🔮 Future Enhancements

* RAG with AWS and Terraform documentation
* Dockerize the application
* Deploy to AWS EC2
* Authentication and user login
* Export chat history

---

## 🐳 Docker Support (Future)

```bash
docker build -t ai-devops-assistant .
docker run -p 8501:8501 ai-devops-assistant
```

---

## ☁️ Deployment Options

* Amazon EC2
* Docker
* Kubernetes
* Streamlit Community Cloud (for UI only)

---

## 📝 requirements.txt

```txt
streamlit
requests
```

---

## 🚫 .gitignore

```gitignore
venv/
__pycache__/
.env
```

---

## 👨‍💻 Author

Naresh Kumar

---

## ⭐ Why This Project Matters

This project combines two high-demand skills:

* DevOps
* Generative AI

It demonstrates practical experience in:

* LLM integration
* Prompt engineering
* Python development
* Infrastructure automation
* Developer tooling

---

## 📌 Recommended GitHub Repository Name

```text
ai-devops-assistant
```

---

## 🏆 Interview Talking Points

Be prepared to explain:

* What is an LLM?
* Why use Ollama?
* Why choose Llama 3?
* How Streamlit communicates with the model
* How you would add RAG
* How you would deploy the application to AWS

---

## 🎯 Project Summary

This project is a locally hosted AI assistant specialized in DevOps and cloud infrastructure. It uses Llama 3 running through Ollama and a Streamlit-based web interface to provide real-time technical explanations and code generation.
