from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
from graph import app

app = FastAPI(description="Whatsapp Api")


@app.post("/")
def welcome():
    return{
        "message" : "Welcome to the home"
    }

@app.post("/whatsapp")
async def whatsapp_webhook(request: Request):
    form = await request.form()
    user_number = form.get("From")
    user_message = form.get("Body")

    if not user_message:
        body_bytes = await request.body()
        decoded = body_bytes.decode()
        print("Raw body:", decoded)
        return PlainTextResponse("<Response><Message>Invalid request</Message></Response>", media_type="application/xml")

    print(f"Incoming from {user_number}: {user_message}")

    result = gf_graph.invoke(
        {"message": [{"role": "user", "content": user_message}]},
        config={"thread_id": user_number}
    )

    ai_reply = result["message"][-1].content
    print(f"AI Reply: {ai_reply}")

    twiml = f"""<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Message>{ai_reply}</Message>
</Response>
"""

    return PlainTextResponse(twiml, media_type="application/xml")
