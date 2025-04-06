import os
from gtts import gTTS
from PIL import Image, ImageDraw, ImageFont
import tkinter as tk
from tkinter import messagebox

def generate_script(domain, topic):
    return f"Today in {domain}, we will explore the topic: {topic}. This is an introduction to {topic}. Let's begin!"

def generate_audio(script, filename="voiceover.mp3"):
    tts = gTTS(text=script, lang='en')
    tts.save(filename)
    return filename

def generate_slide(topic, domain, filename="slide.png"):
    img = Image.new('RGB', (1280, 720), color='black')
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("arial.ttf", 60)
    except:
        font = ImageFont.load_default()

    text = f"{topic}\n({domain})"
    lines = text.split("\n")
    y_offset = 720 // 3

    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=font)
        text_width = bbox[2] - bbox[0]
        draw.text(((1280 - text_width) / 2, y_offset), line, fill="white", font=font)
        y_offset += 80

    img.save(filename)
    return filename

def generate_video_with_ffmpeg(image_path, audio_path, output_path):
    cmd = f'ffmpeg -y -loop 1 -i "{image_path}" -i "{audio_path}" ' \
          f'-c:v libx264 -tune stillimage -c:a aac -b:a 192k ' \
          f'-pix_fmt yuv420p -shortest -movflags +faststart "{output_path}"'
    os.system(cmd)
    return output_path


def run_generator():
    domain = domain_entry.get().strip()
    topic = topic_entry.get().strip()

    if not domain or not topic:
        messagebox.showerror("Input Error", "Please fill in both domain and topic.")
        return

    try:
        script = generate_script(domain, topic)
        audio_file = generate_audio(script)
        slide_image = generate_slide(topic, domain)
        video_file = generate_video_with_ffmpeg(slide_image, audio_file)

        messagebox.showinfo("Success", f"✅ Video generated successfully:\n{video_file}")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{str(e)}")

# === GUI Setup ===
root = tk.Tk()
root.title("AI Educational Video Generator")
root.geometry("400x300")
root.configure(bg="#f2f2f2")

tk.Label(root, text="Enter Domain:", bg="#f2f2f2", font=("Arial", 12)).pack(pady=10)
domain_entry = tk.Entry(root, width=40)
domain_entry.pack()

tk.Label(root, text="Enter Topic:", bg="#f2f2f2", font=("Arial", 12)).pack(pady=10)
topic_entry = tk.Entry(root, width=40)
topic_entry.pack()

generate_btn = tk.Button(root, text="Generate Video", command=run_generator, bg="#4CAF50", fg="white", font=("Arial", 12))
generate_btn.pack(pady=20)

root.mainloop()
