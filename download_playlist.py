from pytube import Playlist
from numpy import round


def get_playlist_info(link):
    print(link.title)
    
    # print(link.description)
    print(f"Number of videos in playlist: {link.length}\n")
    
    for video_obj in link.videos:
        for stream in video_obj.streams.filter(file_extension="mp4",progressive=True):
            # print(type(stream))
            print(f"{stream} -\tAudio={stream.includes_audio_track}\t{round(stream.filesize_approx/1048576,2)}MB")
            # stream.download(output_path="./downloads")
        print("\n")


# playlist_link = input("Enter the link: ")

playlist_link = "https://youtube.com/playlist?list=PLoMt7Ms7DgE38K2z3LXbVUBpCwXy1ODtk" # For Testing
# playlist_link = "https://youtube.com/playlist?list=PLuU3eVwK0I9PT48ZBYAHdKPFazhXg76h5" # streamlit
# playlist_link = "https://youtube.com/playlist?list=PL3cFiqLUjlYPGlWWszesTtdI3v0tcLe5E" # Stocks
# playlist_link="https://youtube.com/playlist?list=PLLssT5z_DsK-h9vYZkQkYNWcItqhlRJLN" # ML

playlist_obj = Playlist(playlist_link)

get_playlist_info(playlist_obj)





