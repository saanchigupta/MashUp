# MashUP

MashUP is a Python-based project that implements a YouTube audio mashup generator in two parts:

1. Program-1: Command line Python application  
2. Program-2: Web service for mashup generation and email delivery  

The system downloads N videos of a given singer from YouTube, converts them to audio, trims the first Y seconds from each file, merges them into a single audio file, and provides the final mashup as output.

------------------------------------------------------------
Project Structure
------------------------------------------------------------

MashUP/
│
├── Program-1/
│   └── <RollNumber>.py
│
├── Program 2/
│   ├── app.py
│   ├── templates/
│   └── requirements.txt
│
└── README.md


------------------------------------------------------------
Program 1: Command Line Mashup Generator
------------------------------------------------------------

Description:
This program is a command line Python script that:
1. Downloads N YouTube videos of a given singer.
2. Converts all downloaded videos into audio format.
3. Cuts the first Y seconds from each audio file.
4. Merges all trimmed audio files into one final output file.

Usage:
python <RollNumber>.py <SingerName> <NumberOfVideos> <AudioDuration> <OutputFileName>

Example:
python 102303323.py "Sharry Maan" 20 20 102303323-output.mp3

Parameters:
SingerName        Name of the singer
NumberOfVideos    Number of videos to download (must be greater than 10)
AudioDuration     Duration in seconds to cut from each video (must be greater than 20)
OutputFileName    Final merged output file name

Features:
- Validates number of command line arguments
- Validates numeric inputs
- Handles exceptions
- Shows proper error messages for invalid inputs

Libraries Used:
- yt-dlp or pytube (for downloading YouTube videos)
- moviepy or ffmpeg (for video to audio conversion)
- pydub (for trimming and merging audio)
- argparse or sys (for command line argument parsing)

Installation:
pip install yt-dlp pytube moviepy pydub ffmpeg-python

Note:
FFmpeg must be installed and configured in system PATH.


------------------------------------------------------------
Program 2: Web Service Mashup Generator
------------------------------------------------------------

Description:
This program provides a web interface for mashup generation.

User Inputs:
- Singer Name
- Number of Videos
- Duration of each video (in seconds)
- Email ID

Workflow:
1. User fills the form and submits.
2. Backend downloads N videos of the singer.
3. Converts them to audio.
4. Cuts first Y seconds from each audio.
5. Merges all trimmed audios.
6. Compresses final output into a ZIP file.
7. Sends the ZIP file to the provided email address.

Validation:
- All fields are required.
- Number of videos must be greater than 10.
- Duration must be greater than 20 seconds.
- Email must be valid format.

Technologies Used:
- Flask (Web framework)
- yt-dlp or pytube
- pydub
- moviepy or ffmpeg
- smtplib or Flask-Mail (for sending email)
- zipfile (for compression)

Run Locally:
cd Program 2
pip install -r requirements.txt
python app.py

Open in browser:
http://127.0.0.1:5000/

Deployment:
The web service is deployed and accessible via:
https://mashup-web-uk85.onrender.com


------------------------------------------------------------
Error Handling
------------------------------------------------------------

Both programs implement:
- Input validation
- Exception handling
- Proper user-friendly error messages
- Safe file handling
- Cleanup of temporary files after execution


------------------------------------------------------------
Requirements
------------------------------------------------------------

Python 3.8 or higher

Python Libraries:
yt-dlp
pytube
moviepy
pydub
flask
flask-mail
ffmpeg-python

System Requirement:
FFmpeg installed and added to PATH


------------------------------------------------------------
How It Works (High Level Flow)
------------------------------------------------------------

1. Take user input (CLI or Web).
2. Search and download N videos of the given singer from YouTube.
3. Convert videos to audio format.
4. Trim first Y seconds from each audio file.
5. Merge all trimmed audio files into one.
6. Save final mashup.
7. Provide output file (download or email).


------------------------------------------------------------
Author
------------------------------------------------------------

Saanchi Gupta
