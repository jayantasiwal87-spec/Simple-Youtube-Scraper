from parser import YouTubeScraper

print("===== YOUTUBE VIDEO ANALYZER =====")

url = input("Enter YouTube Video URL: ")

yt = YouTubeScraper(url)

if not yt.is_valid():
    print("\n❌ Invalid YouTube URL!")
else:
    print("\n🔍 Fetching video details...\n")
    details = yt.get_details()

    print("===== RESULT =====")
    print(f"Title: {details['title']}")
    print(f"Channel: {details['channel']}")
    print(f"Description Word Count: {details['desc_word_count']}")
    print(f"Video ID: {details['video_id']}")
    print("===================")
