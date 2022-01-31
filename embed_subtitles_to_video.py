from pytube import Playlist,YouTube,Caption
from os import listdir
from numpy import array 

files = array(listdir("E:\\play-list\\threeJS\\"))

def getCaption(v_obj):
    # print(v_obj.title)
    eng_subs = v_obj.captions['en']
    # print(eng_subs.xml_captions)
    print(eng_subs.generate_srt_captions())


link = "https://youtu.be/uzkedMF-l4Q?list=PLbu98QxRH81KkLTN00OXhD8Y-pRVgTCnM"

yt = YouTube(link)

getCaption(yt)




