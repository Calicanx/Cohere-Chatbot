from dotenv import load_dotenv
from langchain_community.chat_models import ChatCohere
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from fastapi import FastAPI
import uvicorn

app = FastAPI()

load_dotenv(".env")

llm = ChatCohere()


@app.get("/input")
def access_chatbot(question):

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are world class technical documentation writer."),
        ("user", "{input}")
    ])

    output_parser = StrOutputParser()

    chain = prompt | llm | output_parser

    result = chain.invoke({"input":question})
    return result

if __name__ == '__main__':
    uvicorn(app, host = '127.0.0.1', port = 8000)
