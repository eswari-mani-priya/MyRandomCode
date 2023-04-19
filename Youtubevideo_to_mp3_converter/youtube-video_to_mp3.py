from pytube import YouTube
import os

yt = YouTube("https://youtu.be/_z-1fTlSDF0")

# Extract only audio
video = yt.streams.filter(only_audio=True).first()

output = video.download(output_path="./")
filename, ext = os.path.splitext(output)
new_file = filename + '.mp3'
os.rename(output, new_file)
print(yt.title + ' has been downloaded successfully!')




