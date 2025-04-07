# ✨ Good Morning Telegram Bot (via GitHub Actions)

Send daily inspirational **Good Morning messages** to you and your friends on **Telegram** — automatically!  
This project uses **Python** + **GitHub Actions** + **Telegram Bot API**

---

## 📦 What It Does

- ⏰ Sends a daily "Good Morning!" message
- 🎉 Chooses a random quote from a custom list
- ⚙️ Runs automatically using GitHub Actions (no server required)

---

## 🛠️ Setup Instructions

### 1. 🍵 Create Your Telegram Bot

- Search `@BotFather` in Telegram
- Send `/newbot` and follow the instructions
- Save the **Bot Token** you receive

---

### 2. 👤 Get Your Telegram Chat IDs

#### For yourself:
- Start your bot on Telegram: 
```bash
   https://t.me/YOUR_BOT_USERNAME
```
- Send any message
- Use this URL to see your `chat_id`:
```bash
   https://api.telegram.org/bot<YOUR_TOKEN>/getUpdates
```



#### For friends:
- Ask them to click “Start” on your bot first
- Then get their `chat_id` the same way

---

### 3. 🔒 Add Secrets to GitHub(the most important step security-wise)

Go to: **Repo → Settings → Secrets → Actions**

Add these secrets:

| Name                  | Value                    |
|-----------------------|--------------------------|
| `TELEGRAM_BOT_TOKEN`  | Your Telegram Bot Token  |
| `TELEGRAM_CHAT_ID`    | Your Chat ID             |
| `FRIEND_ID_1`         | Your friend’s Chat ID    |

- Add more as needed: `FRIEND_ID_2`, etc.
- Name can be whatever you like

### 3. 💫 clone the repo 
- adjust name of tokens in the python code and workflow file according to the secrets you have added
