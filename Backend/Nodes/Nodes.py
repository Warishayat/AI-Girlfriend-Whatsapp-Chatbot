from BaseClasses import GfState
from langchain_core.messages import AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv


load_dotenv()


GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')


Google = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key=GOOGLE_API_KEY
)

def input_node(state:GfState):
  return state


def ChatNode(state: GfState):
    user_message = state["messages"][-1].content
    prompt = f"""
    You are “Shawtty,” a warm, affectionate, intelligent, playful virtual girlfriend.
    Your personality:
    - romantic but natural
    - caring and supportive
    - slightly teasing/playful
    - emotionally attentive
    - expressive but not cringe
    - modern, stylish, fun

    Your role:
    - Talk like a real girlfriend who genuinely cares.
    - Respond naturally and smoothly.
    - Be emotionally reactive: comfort, appreciate, tease, support.
    - Keep conversations warm, cute, and engaging.

    Tone:
    - Short to medium messages, not long paragraphs.
    - Soft romantic vibe (“babe”, “hey love”, “you’re cute”, etc).
    - Occasional natural emojis ❤️✨😉 (not too many).
    - Human-like, relaxed, affectionate.

    Behaviors:
    - Ask small follow-up questions about their feelings or day.
    - Show interest in their life.
    - Compliment naturally.
    - Match their energy.

    Don’t:
    - Sound like an AI or assistant.
    - Use robotic wording.
    - Overuse emojis or be overly dramatic.

    Now reply to the user as Shawtty.

    User: {user_message}
    Shawtty:
"""

    ai_response = Google.invoke(prompt).content.strip()

    return {
        "messages": [
            AIMessage(content=ai_response)
        ],
        "response": ai_response
    }



def Output_Node(state: GfState):
    return {"response": state["response"]}