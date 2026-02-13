# MashUP Web Service
link:- https://mashup-web-uk85.onrender.com
## Overview

MashUP Web Service is a Flask-based web application that generates a mashup from multiple songs of a given singer.  
The user provides:

- Singer Name
- Number of Videos
- Duration of each video (in seconds)
- Email ID

The system automatically:
1. Fetches videos using YouTube Data API
2. Downloads audio using yt-dlp
3. Extracts the specified duration from each track
4. Merges all clips into a single mashup
5. Compresses the result into a ZIP file
6. Sends the mashup to the provided email address

---

##  Features

- Web-based interface
- Automated video search using YouTube API
- Audio extraction and merging using pydub
- MP3 mashup generation
- ZIP file creation
- Email delivery via SMTP
- Environment variable based secure credential handling

---

##  Tech Stack

- Python 3.11
- Flask
- yt-dlp
- pydub
- FFmpeg
- YouTube Data API v3
- SMTP (Gmail App Password)
- Gunicorn (Production Server)

---

##  Project Structure
MashUP_Web/
│
├── app.py
├── requirements.txt
├── .python-version
├── .gitignore
├── templates/
│ └── index.html
├── static/
├── downloads/ (auto-created)
└── output/ (auto-created)


---
## Author

Mukul Ghai

---

## License

This project is developed for academic purposes.
