# TGForwarder
TGForwarder is an advanced Telegram bot designed to seamlessly share content from one Telegram group to another. Whether it’s images, GIFs, videos, documents, or messages, this bot ensures that your selected content is forwarded efficiently, reliably, and without duplication.


<img width="401" height="325" alt="image" src="https://github.com/user-attachments/assets/9c32e3b0-6d60-4898-ae2c-70cbdf11bbd8" />
# 🚀 TGForwarder: Intelligent Content Synchronization

**TGForwarder** is an automated distribution bot designed for high-volume Telegram community management. It enables the seamless replication of content across multiple groups or channels, ensuring that your community stays updated without the manual overhead of cross-posting.

## ✨ Key Features
* **Multi-Media Support:** Seamlessly forwards Images, GIFs, Videos, Documents, and Text.
* **Intelligent De-duplication:** Built-in logic to ensure content is only forwarded once, preventing spam.
* **Real-Time Processing:** Zero-latency forwarding to keep distributed groups in perfect sync.
* **Scalable Architecture:** Designed to handle high-traffic groups with minimal overhead.

## 🛠 Tech Stack
* **Language:** Python 3.12
* **Library:** Telethon / Pyrogram (Telegram MTProto API)
* **Environment:** Optimized for VPS or Local Server deployment.

## 📦 How it Works
1. Configure your Source and Destination Group IDs.
2. Set your `API_ID` and `API_HASH` in the environment.
3. Run the forwarder:
   ```bash
   python TGForward.py
