from tkinter import filedialog
import os
import shutil
import pytube
from moviepy.editor import *
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    files = request.files.getlist('file')
    links = []
    downloads_dir = filedialog.askdirectory(title="Select Directory to Create Files and Folders In")
    for file in files:
        links += file.read().decode().split('\n')
    try:
        for link in links:
            if link.strip() != '':
                yt = pytube.YouTube(link.strip())
                audio_stream = yt.streams.filter(only_audio=True).first()
                audio_file = audio_stream.download()
                audio_clip = AudioFileClip(audio_file)
                mp3_file = os.path.splitext(audio_file)[0] + ".mp3"
                audio_clip.write_audiofile(mp3_file)
                os.remove(audio_file)
                shutil.move(mp3_file, downloads_dir)
        return jsonify({'success': True}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
