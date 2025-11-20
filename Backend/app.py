from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
from dotenv import load_dotenv
import os
from graph import gf_graph
from twilio.twiml.messaging_response import MessagingResponse


load_dotenv()

TWILIO_SID = os.getenv("Twillio_Account_sid")
TWILIO_AUTH = os.getenv("Twillio_Account_Auth_Token")

app = FastAPI(title="AI Girlfriend WhatsApp API")

@app.get("/")
def root():
    return {"message": "WhatsApp AI Girlfriend Bot is running!"}


@app.post("/whatsapp")
async def whatsapp_webhook(request: Request):
    form = await request.form()

    user_number = form.get("From")
    user_message = form.get("Body")
    if not user_message:
        return PlainTextResponse(
            "<Response><Message>Invalid request. No message found.</Message></Response>",
            media_type="application/xml",
        )
    print(f"Incoming from {user_number}: {user_message}")
    result = gf_graph.invoke(
        {"messages": [{"role": "user", "content": user_message}]},
        config={"thread_id": user_number}
    )

    ai_reply = result["messages"][-1].content
    print(f"AI Reply: {ai_reply}")
    resp = MessagingResponse()
    resp.message(ai_reply)

    return PlainTextResponse(str(resp), media_type="application/xml")
