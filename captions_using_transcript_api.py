from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import JSONFormatter

link = "https://youtu.be/FK3dav4bA4s"

# lang = YouTubeTranscriptApi.list_transcripts("FK3dav4bA4s")

eng_transcript = YouTubeTranscriptApi.get_transcript("FK3dav4bA4s",languages=['en'])


formatter = JSONFormatter()

# .format_transcript(transcript) turns the transcript into a JSON string.
json_formatted = formatter.format_transcript(eng_transcript)


# Now we can write it out to a file.
with open('output_subtitles.json', 'w', encoding='utf-8') as json_file:
    json_file.write(json_formatted)















