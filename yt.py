google-api-python-client

from apiclient.discovery import build

DEV_KEY = 'AIzaSyBQ4_mRJbwOuWS_Wu3nVM9SqVXs2t36hAI'
yt = build('youtube', 'v3', developerKey=DEV_KEY)

def youtube(vid):
	results = yt.videos().list(id=vid, part="id, snippet, statistics, contentDetails").execute()
	for result in results.get('items', []):
		title = result["snippet"]["title"]
		dur = result["contentDetails"]["duration"].split("PT")[1].lower()
		views = int(result["statistics"]["viewCount"])
		likes = int(result["statistics"]["likeCount"])
		dislikes = int(result["statistics"]["dislikeCount"])
		channel = result["snippet"]["channelTitle"]

		ytmsg = "{} ({}) | {:,}+ / {:,}- | views {:,} | {}".format(title,
																   dur,
																   likes,
																   dislikes,
																   views,
																   channel)
		return ytmsg

if msg.find("youtube.com/") != -1:
	vid = msg.split('v=')[1][:11]
	ytmsg = youtube(vid)
	sendmsg(chan, ytmsg)

if msg.find("youtu.be/") != -1:
	vid = msg.split("//")[1].split("/")[1][:11]
	ytmsg = youtube(vid)
	sendmsg(chan, ytmsg)
