import os
from flask import Flask, render_template, request, send_from_directory
from gtts import gTTS
from PIL import Image, ImageDraw, ImageFont

app = Flask(__name__)
OUTPUT_DIR = "static/outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_script(domain, topic):
    return f"Today in {domain}, we will explore the topic: {topic}. This is an introduction to {topic}. Let's begin!"

def generate_audio(script, filename):
    tts = gTTS(text=script, lang='en')
    tts.save(filename)
    return filename

def generate_slide(topic, domain, filename):
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
    cmd = f'ffmpeg -y -loop 1 -i "{image_path}" -i "{audio_path}" -c:v libx264 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p -shortest "{output_path}"'
    os.system(cmd)
    return output_path

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        domain = request.form["domain"].strip()
        topic = request.form["topic"].strip()
        if not domain or not topic:
            return render_template("index.html", error="Please enter both domain and topic.")

        base_filename = f"{domain}_{topic}".replace(" ", "_")
        script = generate_script(domain, topic)

        audio_file = os.path.join(OUTPUT_DIR, base_filename + ".mp3")
        image_file = os.path.join(OUTPUT_DIR, base_filename + ".png")
        video_file = os.path.join(OUTPUT_DIR, base_filename + ".mp4")

        generate_audio(script, audio_file)
        generate_slide(topic, domain, image_file)
        generate_video_with_ffmpeg(image_file, audio_file, video_file)

        return render_template(
                                "result.html",
                                video_file=os.path.basename(video_file),
                                audio_file=os.path.basename(audio_file),
                                image_file=os.path.basename(image_file)
)

    return render_template("index.html")

@app.route("/download/<filename>")
def download_file(filename):
    return send_from_directory(OUTPUT_DIR, filename, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
