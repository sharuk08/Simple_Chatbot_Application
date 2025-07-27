# 💬 Q&A Chatbot using Azure OpenAI and Streamlit

This is a lightweight Question-Answering chatbot built using:

- **Azure OpenAI Service** (GPT models)
- **Streamlit** for the user interface
- **Python `requests`** for API calls
- **`.env` file** for secure API configuration

---

## 🚀 Features

- Chat interface using `streamlit.chat`
- Uses Azure OpenAI's Chat Completion API
- Maintains session-based conversation history
- Loads API keys and endpoints securely from a `.env` file

---

## 🧱 Project Structure

```
qa-chatbot/
├── chatbot.py          # Main Streamlit app
├── .env                # API secrets (not tracked by Git)
├── .gitignore          # Ignores .env and cache
└── README.md           # You're reading it!
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/qa-chatbot.git
cd qa-chatbot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install streamlit requests python-dotenv
```

---

### 3. Add a `.env` File

Create a `.env` file in the root folder with the following:

```env
OPENAI_KEY=your_azure_openai_api_key
OPENAI_ENDPOINT_URL=https://your-resource-name.openai.azure.com/openai/deployments/your-deployment-name/chat/completions?api-version=2023-05-15
MODEL=gpt-35-turbo
```

> 📌 Ensure your endpoint includes the correct deployment name and API version.

---

### 4. Run the Chatbot

```bash
streamlit run chatbot.py
```

This will launch the chatbot in your browser (usually at `http://localhost:8501`).

---

## 📦 Sample `.gitignore`

```gitignore
.env
__pycache__/
*.pyc
.streamlit/
```

---

## 📦 Sample `requirements.txt`

```txt
streamlit
requests
python-dotenv
```

---

## 🛠 Future Enhancements

- File upload (PDF, CSV) with embedding-based QA
- Persistent chat history using a database
- User login support (multi-user sessions)

---

## 📄 License

This project is open-source under the **MIT License**.

---

## 🙋‍♂️ Author

Built with ❤️ using OpenAI and Streamlit  
Maintained by [Your Name](https://github.com/your-username)
