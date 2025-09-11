import asyncio
from telethon import TelegramClient

# =========================
# CONFIG
# =========================
api_id = 21891838
api_hash = 'c1cf4ea87d4fd08fd0bf119e16174ff1'
session_name = 'Hello123'
source_group = -1001114301412  # group to scan
destination_group = -1002859107627 # where to forward

client = TelegramClient("user_session", api_id, api_hash)

async def scan_and_forward():
    async with client:
        # Ask user for starting count
        print("🔍 Scanning for stickers and GIFs...")
        print("Enter the number of stickers/GIFs already forwarded (press Enter to start from the beginning):")
        
        try:
            # Wait for user input with a 10-second timeout
            start_count = await asyncio.wait_for(
                asyncio.get_event_loop().run_in_executor(None, input), 
                timeout=10.0
            )
            start_count = int(start_count.strip()) if start_count.strip() else 0
        except asyncio.TimeoutError:
            print("No input received, starting from the beginning...")
            start_count = 0
        except ValueError:
            print("Invalid input, starting from the beginning...")
            start_count = 0
        
        print(f"Starting from count: {start_count}")
        
        target_messages = []
        processed_count = 0
        skipped_count = 0

        # Scan all messages
        async for msg in client.iter_messages(source_group, limit=None):
            # Only process stickers and GIFs
            if msg.sticker or (msg.document and msg.document.mime_type == 'video/mp4'):
                # Skip already forwarded items
                if processed_count < start_count:
                    skipped_count += 1
                    processed_count += 1
                    continue
                    
                target_messages.append(msg.id)
                processed_count += 1

        total_messages = len(target_messages)
        print(f"📊 Skipped {skipped_count} already forwarded stickers/GIFs")
        print(f"📊 New stickers and GIFs found: {total_messages}")

        if total_messages == 0:
            print("No new stickers or GIFs found to forward.")
            return

        # Forward messages in batches
        batch_size = 10  # Reduced batch size for media
        forwarded_count = 0

        for i in range(0, len(target_messages), batch_size):
            batch = target_messages[i:i + batch_size]
            await client.forward_messages(destination_group, batch, from_peer=source_group)
            forwarded_count += len(batch)
            print(f"✅ Forwarded batch {i//batch_size + 1} | Total forwarded: {forwarded_count}/{total_messages}")

            if forwarded_count >= total_messages:
                break

            await asyncio.sleep(10)  # avoid flood limits

        print("🎉 All new stickers and GIFs forwarded!")
        print(f"Total stickers/GIFs processed so far: {processed_count}")

# =========================
# Run in Jupyter/Colab
# =========================
import nest_asyncio
nest_asyncio.apply()  # fix event loop for Jupyter

await scan_and_forward()
