from pytube import YouTube


def get_captions(yt):
    # print(yt.title)
    # print(yt.captions.generate_srt_captions())
    # print(yt.captions)

    # eng_subs = yt.captions.get_by_language_code("a.en") # also works but we get depracated warning

    eng_subs = yt.captions["a.en"]  # no error
    # print(eng_subs)
    # print(type(eng_subs))
    # print(eng_subs.xml_captions)
    print(eng_subs.generate_srt_captions())

link = input("Enter the link: ")

yt = YouTube(link)

get_captions(yt)



















