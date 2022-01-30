from pytube import Playlist
from numpy import round


size = 0

def download_vid(stream):
    file_size = round(stream.filesize_approx/1048576,2)
    global size 
    size+=file_size
    print(stream.resolution)
    print(f"File Size: {file_size}MB")
    stream.download(output_path="./downloads")


def download_playlist(link):
    print(link.title)
    print(f"Number of videos in playlist: {link.length}\n")

    i=1
    for video_obj in link.videos:
        print(f"Video count - {i} - \t",end="")
        # print(video_obj.streams.filter(file_extension="mp4",progressive=True,res="360p"))
        for stream in video_obj.streams.filter(file_extension="mp4",progressive=True,res="720p"):
            download_vid(stream)
        i+=1

playlist_link = input("Enter the link: ")

# playlist_link = "https://youtube.com/playlist?list=PLoMt7Ms7DgE38K2z3LXbVUBpCwXy1ODtk" # For Testing

playlist_obj = Playlist(playlist_link)

download_playlist(playlist_obj)

print(f"Total Playlist Size - {size}")


# subprocess.run('rundll32.exe powrprof.dll, SetSuspendState Sleep',shell=True)
