from pytube import Playlist


def get_playlist_info(link):
    print(link.title)
    # print(link.description)
    print(f"Number of videos in playlist: {link.length}\n")
    
    for video_obj in link.videos:
        print(video_obj.streams)



# playlist_link = input("Enter the link: ")
playlist_link = "https://youtube.com/playlist?list=PLuU3eVwK0I9PT48ZBYAHdKPFazhXg76h5"

playlist_obj = Playlist(playlist_link)

get_playlist_info(playlist_obj)





