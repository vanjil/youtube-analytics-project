import os
import requests

class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        api_key = os.environ.get("YOUTUBE_API_KEY")
        if not api_key:
            raise ValueError("API key is missing. Set it using os.environ['YOUTUBE_API_KEY'] = 'your_api_key'")

        base_url = "https://www.googleapis.com/youtube/v3/channels"
        params = {
            'part': 'snippet,contentDetails,statistics',
            'id': self.channel_id,
            'key': api_key
        }

        response = requests.get(base_url, params=params)
        data = response.json()

        if 'items' in data and data['items']:
            channel_data = data['items'][0]
            snippet = channel_data['snippet']
            statistics = channel_data['statistics']

            print(f"Channel ID: {self.channel_id}")
            print(f"Title: {snippet['title']}")
            print(f"Description: {snippet['description']}")
            print(f"Published At: {snippet['publishedAt']}")
            print(f"Total Views: {statistics['viewCount']}")
            print(f"Subscriber Count: {statistics['subscriberCount']}")
        else:
            print("Channel not found or API request failed.")
