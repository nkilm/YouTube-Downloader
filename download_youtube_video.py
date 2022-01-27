# https://youtu.be/tPEE9ZwTmy0 # shortest video on YT.    XD

from pytube import YouTube
from numpy import round 

def completed(stream_downloaded,path):
    print(f"Saved to {path}")

def down_progress(chunk,file_handler,remaining_bytes):
    # Segment of media file binary data, not yet written to disk.
    print(chunk,file_handler,remaining_bytes)

def get_resolutions(obj):
    return [i.resolution for i in obj]

def download_video(yt):
    print(yt.title)

    available_streams = yt.streams.filter(file_extension='mp4',progressive=True)
    # available_streams = yt.streams.filter(file_extension='mp4',adaptive=True)
    print(f"Available Quality - {get_resolutions(available_streams)}")
    vid_quality = input("Video Quality: ")
    desired_stream = available_streams.get_by_resolution(vid_quality)
    file_size = round(desired_stream.filesize_approx/1048576,2)
    print(f"File Size: {file_size}MB")
    desired_stream.download(output_path="downloads")


link = input("Enter the link: ")

yt = YouTube(link,on_complete_callback=completed)

download_video(yt)



