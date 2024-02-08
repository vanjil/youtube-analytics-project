import datetime
from datetime import timedelta
import isodate
from googleapiclient.discovery import build

class PlayList:
    def __init__(self, playlist_id):
        self._playlist_id = playlist_id
        youtube = self._get_playlist_info()
        playlist_request = youtube.playlists().list(
            part="snippet",
            id=self._playlist_id
        )
        playlist_response = playlist_request.execute()
        self._title = playlist_response['items'][0]['snippet']['title']
        self._url = f"https://www.youtube.com/playlist?list={self._playlist_id}"

    @property
    def title(self):
        return self._title

    @property
    def url(self):
        return self._url

    @property
    def total_duration(self):
        youtube = self._get_playlist_info()
        videos_request = youtube.playlistItems().list(
            part="snippet,contentDetails",
            playlistId=self._playlist_id
        ).execute()
        video_ids: list[str] = [video['contentDetails']['videoId']
                                for video in videos_request['items']]
        video_response = youtube.videos().list(
            part='contentDetails,statistics',
            id=','.join(video_ids)
        ).execute()
        total_duration = timedelta(hours=0, minutes=0, seconds=0)
        for item in video_response['items']:
            duration_seconds = item['contentDetails']['duration']
            total_duration += isodate.parse_duration(duration_seconds)

        return total_duration


    def show_best_video(self):
        youtube = self._get_playlist_info()
        videos_request = youtube.playlistItems().list(
            part="snippet,contentDetails",
            playlistId=self._playlist_id
        )
        videos_response = videos_request.execute()
        videos_info = []
        for item in videos_response['items']:
            video_info = {
                'url': f"https://youtu.be/{item['snippet']['resourceId']['videoId']}",
                'likes': self._get_video_likes(youtube, item['snippet']['resourceId']['videoId'])
            }
            videos_info.append(video_info)

        best_video = max(videos_info, key=lambda video_info: video_info['likes'])
        return best_video['url']

    def _get_playlist_info(self):
        api_key = "AIzaSyD39r7OwJbDwxtR1xyzFOM6i0UMYCF-gc0"
        youtube = build('youtube', 'v3', developerKey=api_key)

        return youtube

    def _get_video_likes(self, youtube, video_id):
        # Get the number of likes for a video using YouTube API
        video_request = youtube.videos().list(
            part="statistics",
            id=video_id
        )
        video_response = video_request.execute()
        return int(video_response['items'][0]['statistics']['likeCount'])


if __name__ == '__main__':
    pl = PlayList('PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw')
    print("Название плейлиста:", pl.title)
    print("Ссылка на плейлист:", pl.url)
    print("Общая длительность плейлиста:", pl.total_duration)
    print("Ссылка на самое популярное видео:", pl.show_best_video())
