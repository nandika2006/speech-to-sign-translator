## Speech to sign translator

A basic GUI app that listens to your speech and translates it to Sign Language using animated GIFs (ASL-based).

# Features
- Uses microphone input
- Displays sign language animations
- Fallback to alphabet-wise GIFs if word GIF is missing

# How to Run

    pip install -r requirements.txt
    python main.py

## 🧠 FUTURE IDEAS

- Add real-time webcam-based gesture recognition (with MediaPipe)
- Expand to Indian Sign Language (ISL)
- Add text-to-sign and sign-to-text toggle
- Export as an `.exe` or `.apk` app


## 🎁 BONUS TIP: Sample Word-to-GIF Mapping

You can use this dictionary in `main.py` to map more complex phrases or do aliasing:

custom_gifs = {
    "hello": "hello.gif",
    "thank": "thankyou.gif",
    "thanks": "thankyou.gif",
    "i": "i.gif",
    "love": "love.gif",
    "you": "you.gif"
}

