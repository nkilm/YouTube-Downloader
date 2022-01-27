from pytube import YouTube


def video_info(yt):
    print(yt.title)
    print(yt.length) # in seconds
    print(yt.age_restricted)
    print(yt.rating)
    print(yt.thumbnail_url)
    # print(yt.metadata)
    # print(yt.check_availability())



# link = "https://youtu.be/wfF0zHeU3Zs"
link=input("Enter the link: ")

yt = YouTube(link)

video_info(yt)





