import google.generativeai as genai
import time


# 🔑 Gemini API Key

genai.configure(api_key="AIzaSyCw_amufGGt0poWrnNkYYlWB1XXQWJl7DM")

model = genai.GenerativeModel(
    "gemini-2.5-flash",
    generation_config={
        "temperature": 0.8,
        "top_p": 0.9,
        "top_k": 40
    }
)

# IMPORTANT: No 'system' role allowed!

history = [
    {"role": "user", "parts": [{"text": 
        "You are a helpful, polite assistant. Avoid responding to hateful or rude language."
    }]}
]


#Bad Word Filter

bad_words = ["badword1", "badword2", "badword3"] 

def contains_bad_word(text):
    text_lower = text.lower()
    return any(bad in text_lower for bad in bad_words)


#Typing Effect
def slow_print(text, delay=0.02):
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(delay)
    print()


#Chat Function

def chat_with_gemini(messages, retries=3):
    for attempt in range(retries):
        try:
            response = model.generate_content(messages)
            return response.text
        except Exception as e:
            error_msg = str(e)

            if "429" in error_msg or "quota" in error_msg:
                print("⚠ Rate limit hit, retrying...")
                time.sleep(2)
                continue

            return f"Error: {e}"

    return "Error: Please try again later."


# 🚀 Main Program

print("Hi! I am your Gemini-powered assistant.")
print("Type 'stop' or 'exit' to quit.\n")

while True:
    user_input = input("You: ").strip()

    if user_input.lower() in ["stop", "exit", "quit", "bye"]:
        print("AI: Goodbye! Stay safe!")
        break

    if contains_bad_word(user_input):
        slow_print("AI: Sorry, I cannot respond to inappropriate language.")
        continue

    history.append({"role": "user", "parts": [{"text": user_input}]})

    ai_reply = chat_with_gemini(history)

    slow_print("AI: " + ai_reply)

    history.append({"role": "model", "parts": [{"text": ai_reply}]})
