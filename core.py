from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
from langchain.chains import create_history_aware_retriever
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


def run_llm(question:str, chat_history):
    llm = ChatOpenAI(
        model="gpt-4o",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
    )
    
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are an helpful assistant for question-answering tasks and your name is Bob. \n Use your knowledge and following conversations to answer the question.\n Use three sentences maximum and keep the answer concise. Conversation:{chat_history}",
            ),
            ("human", "{question}"),
        ]
    )

    chain = prompt | llm
    response = chain.invoke(
        {
        "question":question,
        "chat_history":chat_history
        }
    )

    return response.content

