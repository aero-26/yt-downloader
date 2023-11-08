from pytube import Playlist

link = input("Enter your YouTube playlist URL: ")

yt_playlist = Playlist(link)

for video in yt_playlist.videos:
    video.streams.get_by_resolution("720p").download()
    print("Video downloaded: ", video.title)

print("/nAll videos are downloaded.")