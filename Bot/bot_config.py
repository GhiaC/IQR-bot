import os


class Bot:
    base_url = os.getenv("BASE_URL", "https://tapi.bale.ai/")
    bot_token = os.getenv('TOKEN', "1559103460:5481ef5e798138668f2359b30487899bde3effc3")
    poll_interval = int(os.getenv("POLL_INTERVAL", 2))
