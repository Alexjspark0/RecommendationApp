import os
import google.generativeai as genai
from dotenv import load_dotenv
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
)

history = []
while True:
    message = input()
    chat_session = model.start_chat(
        history=history
    )
    response = chat_session.send_message(message)
    respond = response.text
    print(respond)
    print()
    history.append({"role":"user","parts":[message]})
    history.append({"role":"model","parts":[respond]})
