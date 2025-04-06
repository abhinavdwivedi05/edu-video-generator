
# 🎓 AI Educational Video Generator

An AI-powered web application that helps users generate educational video content by simply entering a **domain** and **topic**. The system creates slides, converts text to speech, and compiles everything into a downloadable video.

---

## 🚀 Features

- ✍️ Auto-generates script based on user inputs (domain & topic)
- 🗣️ Text-to-speech voiceover (using gTTS)
- 🖼️ Slide image creation (via Pillow)
- 🎞️ Video generation with audio + image (via FFmpeg)
- 📥 Download generated audio, slide, and video
- 🧑‍🎓 User-friendly minimalist UI

---

## 🛠️ Tech Stack

- **Frontend**: HTML, CSS (off-white/black minimalist theme)
- **Backend**: Python + Flask
- **Libraries**:
  - `gTTS` for voiceover generation
  - `Pillow` (PIL) for slide creation
  - `FFmpeg` for audio + image to video
- **Other Tools**:
  - IDX by Google (for development)
  - Gemini API (for future integration)

---

## 📁 Project Structure

```
ai-educational-video-generator/
├── static/
│   ├── style.css
│   └── outputs/         # Stores generated audio, video, image
├── templates/
│   ├── index.html        # Front page
│   └── generated.html    # Result page
├── app.py                # Flask application
├── requirements.txt
└── README.md
```

---

## 🔧 How to Run Locally

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/ai-educational-video-generator.git
cd ai-educational-video-generator
```

2. Install the dependencies:
```bash
pip install -r requirements.txt
```

3. Run the app:
```bash
python app.py
```

4. Visit `http://localhost:5000` in your browser 🎉

---

## 📈 Future Scope

- Generate multi-slide videos
- Add AI-generated images & music
- Export to `.pptx`
- Deploy on platforms like Render or Railway
- Add user login & dashboard
- Full Gemini AI integration for advanced scripting

---

## 🙌 Developed By

- **Abhinav Dwivedi**  
  [LinkedIn](https://www.linkedin.com/in/abhinav-dwivedi-0b0b342ab/)
- **Surbhi Singla**  
  [LinkedIn](https://www.linkedin.com/in/surbhi-singla-3147722ba/)

---

## 📷 Snapshots

- Homepage Form UI
- Generated Outputs (Slide, Audio, Video)

---

## 📜 License

[MIT](LICENSE)
