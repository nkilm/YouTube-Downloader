from pytube import YouTube
from numpy import round 

def download_video(yt):
    print(yt.title)
    # available_streams = yt.streams.filter(file_extension='mp4',progressive=True)
    available_streams = yt.streams.filter(file_extension='mp4',adaptive=True)
    
    
    for stream in available_streams:
        print(f"{stream.resolution} -\tAudio={stream.includes_audio_track}\t{round(stream.filesize_approx/1048576,2)}MB")


# link = "https://youtu.be/SdGL0qxgZGM?list=PLoMt7Ms7DgE1AbCrhf855R77ARkJ0wkR1"

# link="https://youtu.be/wfF0zHeU3Zs" # Fur Elise
link="https://youtu.be/uSibwB2TQC4?list=PLoMt7Ms7DgE1AbCrhf855R77ARkJ0wkR1"

# link = input("Enter the link: ")

yt = YouTube(link)

download_video(yt)


