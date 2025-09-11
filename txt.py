import asyncio
from telethon import TelegramClient

# =========================
# CONFIG
# =========================
api_id = 21891838
api_hash = 'c1cf4ea87d4fd08fd0bf119e16174ff1'
session_name = 'Hello123'
source_group = -1002799056698     # group to scan
destination_group = -1003038409258 # where to forward

client = TelegramClient("user_session", api_id, api_hash)


async def scan_and_forward():
    async with client:
        print("🔍 Scanning text messages...")
        text_messages = []

        # Scan all messages
        async for msg in client.iter_messages(source_group, limit=None):
            # Only process text messages (ignore all media types)
            if (msg.text and not msg.media and 
                not msg.gif and not msg.sticker and 
                not msg.photo and not msg.video and 
                not msg.document and not msg.audio and 
                not msg.voice):
                text_messages.append(msg.id)

        total_messages = len(text_messages)
        print(f"📊 Total text messages found: {total_messages}")

        # Forward all text messages in batches of 100
        batch_size = 100
        forwarded_count = 0

        for i in range(0, len(text_messages), batch_size):
            batch = text_messages[i:i + batch_size]
            await client.forward_messages(destination_group, batch, from_peer=source_group)
            forwarded_count += len(batch)
            print(f"✅ Forwarded batch {i//batch_size + 1} | Total forwarded: {forwarded_count}/{total_messages}")

            if forwarded_count >= total_messages:
                break

            await asyncio.sleep(10)  # avoid flood limits

        print("🎉 All text messages forwarded!")


# =========================
# Run in Jupyter/Colab
# =========================
import nest_asyncio
nest_asyncio.apply()  # fix event loop for Jupyter

await scan_and_forward()
