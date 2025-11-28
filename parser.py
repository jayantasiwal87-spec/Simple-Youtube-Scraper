import re
import requests
from bs4 import BeautifulSoup

class YouTubeScraper:
    def __init__(self, url):
        self.url = url

    def is_valid(self):
        return ("youtube.com/watch" in self.url) or ("youtu.be" in self.url)

    def extract_video_id(self):
        if "v=" in self.url:
            return self.url.split("v=")[1][:11]
        elif "youtu.be" in self.url:
            return self.url.split("/")[-1][:11]
        return None

    def get_details(self):
        video_id = self.extract_video_id()

        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, "html.parser")

        # Titles
        title_tag = soup.find("meta", property="og:title")
        title = title_tag["content"] if title_tag else "Unknown"

        # Channel Name
        channel_tag = soup.find("link", itemprop="name")
        channel = channel_tag["content"] if channel_tag else "Unknown"

        # Description
        desc_tag = soup.find("meta", property="og:description")
        description = desc_tag["content"] if desc_tag else ""

        return {
            "video_id": video_id,
            "title": title,
            "channel": channel,
            "description": description,
            "desc_word_count": len(description.split())
        }
