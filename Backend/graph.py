from langgraph.graph import StateGraph,START,END
from BaseClasses import GfState
from langgraph.checkpoint.memory import MemorySaver
from langchain_google_genai import ChatGoogleGenerativeAI
from Nodes import ChatNode
import os
from dotenv import load_dotenv


load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

Google = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key=GOOGLE_API_KEY
)

checkpointer = MemorySaver()

graph = StateGraph(GfState)
graph.add_node("chat", ChatNode)
graph.set_entry_point("chat")
graph.set_finish_point("chat")

gf_graph= graph.compile(checkpointer=checkpointer)

if __name__ == "__main__":
    state = {
        "messages": [],
        "response": ""
    }

    config = {"configurable": {"thread_id": "00"}}
    result =gf_graph.invoke(
        {"messages": [{"type": "human", "content": "Do you know about my name?"}]},config=config
    )

    print(result['messages'])