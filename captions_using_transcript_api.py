from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import JSONFormatter

link = "https://youtu.be/FK3dav4bA4s"

all_subs = YouTubeTranscriptApi.list_transcripts("FK3dav4bA4s")

# eng_transcript = YouTubeTranscriptApi.get_transcript("FK3dav4bA4s",languages=['en'])

# print(all_subs)
eng_transcript = all_subs.find_generated_transcript(['en'])

print(eng_transcript.fetch())

# for sub in all_subs:
    # print(sub)
















