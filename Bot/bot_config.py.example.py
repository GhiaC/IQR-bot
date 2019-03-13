import os


class Bot:
    base_url = os.getenv("BASE_URL", "https://tapi.bale.ai/")
    bot_token = os.getenv("TOKEN", "YOUR_TOKEN")
    poll_interval = int(os.getenv("POLL_INTERVAL", 2))
