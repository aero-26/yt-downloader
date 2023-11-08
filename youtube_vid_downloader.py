from pytube import YouTube

link = input("Enter your YouTube video URL: ")

ytVid = YouTube(link)

ytVid = ytVid.streams.get_by_resolution("720p").download()

print("Download Successful")
