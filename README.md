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
- Keeps session-based conversation history
- Loads API keys and endpoints securely from a `.env` file

---

## 🧱 Project Structure

qa-chatbot/
├── chatbot.py # Main Streamlit app
├── .env # API secrets (not tracked by git)
├── .gitignore # Ignores .env and cache
└── README.md # You’re reading it!

yaml
Copy
Edit

---

## ⚙️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/qa-chatbot.git
cd qa-chatbot
2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
Or install manually:

bash
Copy
Edit
pip install streamlit requests python-dotenv
3. Add a .env File
Create a .env file in the root folder:

env
Copy
Edit
OPENAI_KEY=your_azure_openai_api_key
OPENAI_ENDPOINT_URL=https://your-resource-name.openai.azure.com/openai/deployments/your-deployment-name/chat/completions?api-version=2023-05-15
MODEL=gpt-35-turbo
📌 Ensure your endpoint includes deployment name and API version.

4. Run the Chatbot
bash
Copy
Edit
streamlit run chatbot.py
📦 Sample .gitignore
gitignore
Copy
Edit
.env
__pycache__/
*.pyc
.streamlit/
🛠 Future Enhancements
File upload (PDF, CSV) with embedding-based QA

Persistent chat history using database

User login support (multi-user)

📄 License
This project is open-source under the MIT License.

🙋‍♂️ Author
Built with ❤️ using OpenAI and Streamlit
