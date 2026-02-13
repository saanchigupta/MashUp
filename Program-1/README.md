# MashUP – Program 1 (Command Line Mashup Generator)

This project is a Python-based **command line mashup generator** developed as part of an academic assignment.  
It downloads songs of a given singer from YouTube, extracts a fixed duration from each song, and merges them into a single mashup audio file.

---

## Objective

- Accept singer name, number of videos, audio duration, and output file name as command-line arguments
- Download multiple YouTube videos related to the singer
- Extract the **first Y seconds** from each audio
- Merge all extracted clips into **one MP3 mashup**
- Handle invalid inputs and runtime errors gracefully

---

##  Technologies & Libraries Used

- **Python 3.11**
- **yt-dlp** – for downloading YouTube videos
- **pydub** – for audio processing and merging
- **ffmpeg & ffprobe** – backend tools required by pydub

(All Python libraries are installed from **PyPI**)

---

##  Requirements

- Python 3.11
- ffmpeg.exe and ffprobe.exe available (locally or in PATH)

Install required Python libraries:
```bash
pip install yt-dlp pydub
