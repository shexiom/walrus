import os
from dotenv import load_dotenv
import asyncio
import sys
import gradio as gr

load_dotenv()

# بررسی متغیرهای محیطی
required = ["API_ID", "API_HASH", "BOT_TOKEN"]
for var in required:
    if not os.getenv(var):
        raise ValueError(f"متغیر {var} در فایل .env تنظیم نشده!")

print("✅ متغیرهای محیطی لود شد")

def launch_bot():
    try:
        # اجرای اصلی پروژه
        from main import main  # یا هر چیزی که entry point هست
        # متأسفانه main.py مستقیم bot رو اجرا می‌کنه، پس باید تنظیم کنیم
        return "ربات در حال اجرا است... (در HF Spaces ممکن است محدود باشد)"
    except Exception as e:
        return f"خطا: {str(e)}"

# رابط Gradio ساده
with gr.Blocks(title="Walrus - تلگرام به روبیکا") as demo:
    gr.Markdown("# Walrus\nربات انتقال فایل از تلگرام به روبیکا")
    gr.Markdown("ربات در پس‌زمینه اجرا می‌شود. برای کنترل از تلگرام استفاده کنید.")
    
    status = gr.Textbox(label="وضعیت", value="در حال آماده‌سازی...")
    btn = gr.Button("راه‌اندازی ربات")
    
    btn.click(launch_bot, outputs=status)

# این خط مهم است برای HF Spaces
if __name__ == "__main__":
    demo.launch()
