

# 🔎 Slack Chat Summarizer with Gemini API

This is a Flask-based application that fetches recent messages from a Slack channel, summarizes them using Google Gemini's Generative AI model, and posts the summary back to the same channel. Ideal for keeping team members in sync by providing concise conversation summaries.

---

## 🚀 Features

- 🧠 Summarizes the latest 50 messages from a Slack channel using Gemini 1.5 Pro.
- 🤖 Posts the generated summary back to the same channel.
- 🔐 Securely uses environment variables for tokens and secrets.
- 📡 Easily deployable as a Flask web server.

---

## 🧰 Technologies Used

- Python 3.x
- Flask
- Slack SDK (`slack_sdk`)
- Google Generative AI (`google.generativeai`)
- `dotenv` for environment variable management

---

## 📦 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/slack-chat-summarizer.git
cd slack-chat-summarizer
```

### 2. Create a `.env` file

Add the following environment variables in a `.env` file in the root directory:

```env
SLACK_BOT_TOKEN=your-slack-bot-token
SLACK_SIGNING_SECRET=your-slack-signing-secret
SLACK_CHANNEL_ID=your-slack-channel-id
GEMINI_API_KEY=your-gemini-api-key
```

### 3. Install dependencies

We recommend using a virtual environment:

```bash
pip install -r requirements.txt
```

**`requirements.txt` might include:**
```
Flask
slack_sdk
python-dotenv
google-generativeai
```

### 4. Run the application

```bash
python app.py
```

By default, the app will run at `http://0.0.0.0:5000`.

---

## 📥 Endpoint

### `/summarize` [POST]

Triggers the summarization of recent Slack channel messages.

#### Example curl command:

```bash
curl -X POST http://localhost:5000/summarize -d "user_id=U123456"
```

---

## 🛡️ Security

- Ensure your `.env` file is **never committed** to version control.
- Use Slack’s request signing feature to verify requests (can be expanded in this app).
- Rate limit the endpoint if exposing publicly.

---

## 📌 Future Enhancements

- Add support for interactive Slack slash commands.
- Allow custom message limits or time range filtering.
- Store and retrieve summaries in a database for audit or analytics.

---

## 🙌 Credits

Built using:
- [Slack API](https://api.slack.com/)
- [Google Generative AI (Gemini)](https://ai.google.dev/)
- [Flask](https://flask.palletsprojects.com/)

