from youtube_easy_api.easy_wrapper import *
from dotenv import load_dotenv
from os import environ

load_dotenv() # check for .env file in local folder
API_KEY = environ.get('API_KEY')

easy_wrapper = YoutubeEasyWrapper()
easy_wrapper.initialize(api_key=API_KEY)

results = easy_wrapper.search_videos(search_keyword='Fur Elise',order='relevance')
print(results)
metadata = easy_wrapper.get_metadata(video_id="O3oM-awzFus")

for comment,i in enumerate(metadata.get('comments')):
    print(f"{i}. {comment}")

















