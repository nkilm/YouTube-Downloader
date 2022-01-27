from pytube import YouTube
from numpy import round 

def download_video(yt):
    print(yt.title)
    available_streams = yt.streams.filter(file_extension='mp4',progressive=True)
    # available_streams = yt.streams.filter(file_extension='mp4',adaptive=True)
    
    
    for stream in available_streams:
        # stream.download
        print(f"{stream} -\tAudio={stream.includes_audio_track}\t{round(stream.filesize_approx/1048576,2)}MB")


link = input("Enter the link: ")

yt = YouTube(link)

download_video(yt)



