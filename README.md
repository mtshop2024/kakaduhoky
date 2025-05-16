
# 💡 Electric Bill Telegram Bot (Webhook-based)

This is a Telegram bot that calculates electricity bill based on user input in kilowatt-hours (kWh), using tiered pricing.

## 🔧 Features
- Instant Telegram response
- Works 24/7 via Webhook (on PythonAnywhere)
- Supports Arabic
- Free hosting compatible

## 📦 Requirements

```bash
pip install -r requirements.txt
```

## 🚀 Deploy to PythonAnywhere

1. Sign up at [https://www.pythonanywhere.com/](https://www.pythonanywhere.com/)
2. Upload this project
3. Create a Web App (manual, Python 3.10)
4. Set WSGI config to:

```python
import sys
path = '/home/your_username'
if path not in sys.path:
    sys.path.append(path)

from webhook_bot import app as application
```

5. Set webhook with:

```bash
curl -F "url=https://your_username.pythonanywhere.com/YOUR_BOT_TOKEN" \
     https://api.telegram.org/botYOUR_BOT_TOKEN/setWebhook
```

## ✅ Done! Test your bot on Telegram.
