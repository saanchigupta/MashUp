import sys
import os
from yt_dlp import YoutubeDL
from pydub import AudioSegment
from pydub import AudioSegment
AudioSegment.converter = "ffmpeg.exe"
AudioSegment.ffprobe = "ffprobe.exe"

def error(msg):
    print("Error:", msg)
    sys.exit(1)

if len(sys.argv) != 5:
    error("Usage: python <program.py> <SingerName> <NumberOfVideos> <AudioDuration> <OutputFileName>")

singer = sys.argv[1]
try:
    num_videos = int(sys.argv[2])
    duration = int(sys.argv[3])
except ValueError:
    error("NumberOfVideos and AudioDuration must be integers")

output_file = sys.argv[4]

if num_videos <= 10 or duration <= 20:
    error("NumberOfVideos must be >10 and AudioDuration must be >20 seconds")

os.makedirs("downloads", exist_ok=True)

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': 'downloads/%(title)s.%(ext)s',
    'noplaylist': True,
    'quiet': True
}

print("Downloading videos...")

with YoutubeDL(ydl_opts) as ydl:
    ydl.download([f"ytsearch{num_videos}:{singer} songs"])

merged = AudioSegment.empty()

print("Processing audio files...")

for file in os.listdir("downloads"):
    if file.endswith((".mp3", ".m4a", ".webm")):
        audio = AudioSegment.from_file(f"downloads/{file}")
        merged += audio[:duration * 1000]

merged.export(output_file, format="mp3")
print("Mashup created successfully:", output_file)
