import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent
from agent.tools import tools
load_dotenv()
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    api_key=os.getenv("GROQ_API_KEY")
)
agent = create_react_agent(
    model=llm,
    tools=tools,
    prompt=(
        "You are an AI assistant for a life sciences CRM system. "
        "You help pharmaceutical field representatives manage "
        "interactions with Healthcare Professionals (HCPs). "
        "Use the available tools whenever required. "
        "You can search HCPs, log interactions, edit interactions, "
        "view interaction history, and schedule follow-ups. "
        "Before logging an interaction, make sure all required "
        "information is available."
    )
)


def run_agent(message: str):
    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": message
                }
            ]
        }
    )

    return result["messages"][-1].content