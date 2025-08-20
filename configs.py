# (c) @RIYA40X

# Don't Forget That I Made This!
# So Give Credits!


import os


class Config(object):
	BOT_TOKEN = os.environ.get("8258897903:AAGhHqyJA6QpAXrIP6xOXoch0H8xy_1f5fs")
	API_ID = int(os.environ.get("API_ID", 29490954))
	API_HASH = os.environ.get("dbd8f5af56b0f6e16327c20a84eece99")
	STREAMTAPE_API_PASS = os.environ.get("STREAMTAPE_API_PASS", "NoNeed")
	STREAMTAPE_API_USERNAME = os.environ.get("STREAMTAPE_API_USERNAME", "NoNeed")
	LOG_CHANNEL = int(os.environ.get("-1003096560737"))
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
	DOWN_PATH = os.environ.get("DOWN_PATH", "./downloads")
	PRESET = os.environ.get("PRESET", "ultrafast")
	OWNER_ID = int(os.environ.get("OWNER_ID", 7660860610))
	CAPTION = "By @RIYA40X"
	BOT_USERNAME = os.environ.get("BOT_USERNAME", "watermark_73737_bot")
	DATABASE_URL = os.environ.get("mongodb+srv://fibegi:8oV4fjNNVasSfcoY@cluster0.jp8thup.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	ALLOW_UPLOAD_TO_STREAMTAPE = bool(os.environ.get("ALLOW_UPLOAD_TO_STREAMTAPE", False))
	USAGE_WATERMARK_ADDER = """
Hi, I am Video Watermark Adder Bot!

**How to Added Watermark to a Video?**
**Usage:** First Send a JPG Image/Logo, then send any Video. Better add watermark to a MP4 or MKV Video.

__Note: I can only process one video at a time. As my server is Heroku, my health is not good. If you have any issues with Adding Watermark to a Video, then please Report at [Support Group](https://t.me/linux_repo).__

Desgined by @RIYA40X
"""
	PROGRESS = """
Percentage : {0}%
Done ✅: {1}
Total 🌀: {2}
Speed 🚀: {3}/s
ETA 🕰: {4}
"""
