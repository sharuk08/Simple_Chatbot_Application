import streamlit  as st
import requests
from dotenv import load_dotenv
import os


load_dotenv()

#API Configuration
url=os.getenv("OPENAI_ENDPOINT_URL")
api_key=os.getenv("OPENAI_KEY")
model=os.getenv("MODEL")

headers= {
    "Content-type":"application/json",
    "Authorization":api_key
}

st.title("Q&A Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages=[]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
if prompt:=st.chat_input("Ask me anything...."):
    st.session_state.messages.append({"role":"user","content":prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        try:
            data={
                "model":model,
                "messages":[{"role":m["role"],"content":m["content"]}
                            for m in st.session_state.messages],
                "temperature":0.7,
                "max_tokens":500
            }
            response=requests.post(url,headers=headers,json=data,verify=False)

            if response.status_code==200:
                answer=response.json()["choices"][0]["message"]["content"]
                st.markdown(answer)
                st.session_state.messages.append({"role":"assistant","content":answer})
            else:
                st.error(f"API Error: {response.status_code}")
                st.error(response.text)
        except Exception as e:
            st.error(f"Connection Error : {str(e)}")
