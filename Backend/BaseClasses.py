from typing import TypedDict
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages
from typing import Annotated,List


class GfState(TypedDict):
  messages : Annotated[List[BaseMessage],add_messages]