import os
import google.generativeai as genai

# ── Config ────────────────────────────────────────────────────────────────────
MODEL = "gemini-2.5-flash"          # Free tier — current stable model (Apr 2026)
SYSTEM_PROMPT = "You are a helpful assistant. Be concise and friendly."
# ──────────────────────────────────────────────────────────────────────────────


def chat():
    api_key = os.environ.get("AIzaSyALyPoivUj_4fSzRNKhKuFaKhSvXmN7S18")
    if not api_key:
        raise EnvironmentError(
            "GEMINI_API_KEY is not set.\n"
            "Get a FREE key at: https://aistudio.google.com/app/apikey\n"
            "Then run:  export GEMINI_API_KEY="
        )

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(
        model_name=MODEL,
        system_instruction=SYSTEM_PROMPT,
    )
    chat_session = model.start_chat(history=[])   # keeps full conversation

    print("=" * 50)
    print("  Free Chatbot (Gemini 2.5 Flash)  —  type 'quit' to exit")
    print("=" * 50)

    while True:
        # ── Get user input ────────────────────────────────────────────────────
        try:
            user_input = input("\nYou: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if not user_input:
            continue
        if user_input.lower() in {"quit", "exit", "q"}:
            print("Goodbye!")
            break

        # ── Send message & display reply ──────────────────────────────────────
        try:
            response = chat_session.send_message(user_input)
            print(f"\nBot: {response.text}")
        except Exception as exc:
            print(f"\n[Error] {exc}")


if __name__ == "__main__":
    chat()
