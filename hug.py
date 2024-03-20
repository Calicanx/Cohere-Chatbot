from dotenv import load_dotenv
from langchain_community.chat_models import ChatCohere
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv(".env")

llm = ChatCohere()

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are world class technical documentation writer."),
    ("user", "{input}")
])

output_parser = StrOutputParser()

chain = prompt | llm | output_parser

result = chain.invoke({"input": "Can you please tell me about Pavlov's experiment?"})
print(result)