import os
from flask import Flask, request, make_response
from slack_sdk.web import WebClient
from slack_sdk.errors import SlackApiError
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
SLACK_SIGNING_SECRET = os.getenv("SLACK_SIGNING_SECRET")
SLACK_CHANNEL_ID = os.getenv("SLACK_CHANNEL_ID")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Slack & Gemini setup
slack_client = WebClient(token=SLACK_BOT_TOKEN)
genai.configure(api_key=GEMINI_API_KEY)
gemini_model = genai.GenerativeModel("gemini-1.5-pro")

app = Flask(__name__)

def fetch_recent_messages(channel_id, limit=50):
    try:
        response = slack_client.conversations_history(channel=channel_id, limit=limit)
        messages = [msg['text'] for msg in response['messages'] if 'text' in msg and not msg.get("bot_id")]
        return "\n".join(messages)
    except SlackApiError as e:
        return f"Slack API Error: {e}"

def summarize_with_gemini(text):
    try:
        prompt = f"Summarize the following Slack group chat:\n{text}"
        response = gemini_model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Gemini API Error: {e}"

def post_to_slack(channel_id, summary):
    try:
        slack_client.chat_postMessage(channel=channel_id, text=f"*🔎 Summary of recent conversation:*\n{summary}")
    except SlackApiError as e:
        print(f"Slack post error: {e}")

@app.route("/summarize", methods=["POST"])
def summarize_slack_chat():
    data = request.form
    user_id = data.get("user_id")

    conversation = fetch_recent_messages(SLACK_CHANNEL_ID)
    if conversation:
        summary = summarize_with_gemini(conversation)
        post_to_slack(SLACK_CHANNEL_ID, summary)
        return make_response("📌 Summary generated and posted to the channel!", 200)
    else:
        return make_response("No recent messages found.", 200)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
