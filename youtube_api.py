"""

DOCS: 
https://github.com/googleapis/google-api-python-client/blob/main/docs/README.md


"""
# youtube = googleapiclient.discovery.build(
#         api_service_name, api_version, credentials=credentials)

#     request = youtube.captions().download(
#         id="YOUR_CAPTION_TRACK_ID"
#     )


from dotenv import load_dotenv
from os import environ
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
import io

load_dotenv()
API_KEY = environ.get('API_KEY')

yt = build('youtube','v3',developerKey=API_KEY)

req = yt.channels().list(
    part='statistics',
    forUsername = 'sentdex'
)

res = req.execute()
print(res)

# id = "FK3dav4bA4s" # video id 

# req = yt.captions().download(id=id)

# res = req.execute()

print(res)

yt.close()



