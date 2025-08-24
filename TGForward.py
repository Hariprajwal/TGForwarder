import asyncio
from telethon import TelegramClient

# =========================
# CONFIG
# =========================
api_id = 21891838
api_hash = 'c1cf4ea87d4fd08fd0bf119e16174ff1'
session_name = 'Hello123'
source_group = -1002859107627     # group to scan
destination_group = -1002859107627 # where to forward

client = TelegramClient("user_session", api_id, api_hash)


async def scan_and_forward():
    async with client:  # <-- Jupyter-compatible
        print("🔍 Scanning media...")
        media_counts = {
            "photos": 0,
            "videos": 0,
            "gifs": 0,
            "stickers": 0,
            "documents": 0,
            "audios": 0,
            "voices": 0,
            "others": 0
        }

        messages_to_forward = []

        # Scan all messages
        async for msg in client.iter_messages(source_group, limit=None):
            if msg.gif:
                media_counts["gifs"] += 1
                messages_to_forward.append(msg.id)
            elif msg.sticker:
                media_counts["stickers"] += 1
                messages_to_forward.append(msg.id)
            elif msg.photo:
                media_counts["photos"] += 1
                messages_to_forward.append(msg.id)
            elif msg.video:
                media_counts["videos"] += 1
                messages_to_forward.append(msg.id)
            elif msg.document:
                media_counts["documents"] += 1
                messages_to_forward.append(msg.id)
            elif msg.audio:
                media_counts["audios"] += 1
                messages_to_forward.append(msg.id)
            elif msg.voice:
                media_counts["voices"] += 1
                messages_to_forward.append(msg.id)
            else:
                media_counts["others"] += 1

        total_files = sum(media_counts.values())
        print(f"📊 Total media found: {total_files}")
        for k, v in media_counts.items():
            print(f"{k.capitalize()}: {v}")

        # Forward all files in batches of 100
        batch_size = 100
        forwarded_count = 0

        for i in range(0, len(messages_to_forward), batch_size):
            batch = messages_to_forward[i:i + batch_size]
            await client.forward_messages(destination_group, batch, from_peer=source_group)
            forwarded_count += len(batch)
            print(f"✅ Forwarded batch {i//batch_size + 1} | Total forwarded: {forwarded_count}/{total_files}")

            if forwarded_count >= total_files:
                break

            await asyncio.sleep(2)  # avoid flood limits

        print("🎉 All media forwarded!")


# =========================
# Run in Jupyter/Colab
# =========================
import nest_asyncio
nest_asyncio.apply()  # fix event loop for Jupyter

await scan_and_forward()
