import datetime

class PlayList:
    def __init__(self, playlist_id):
        self._playlist_id = playlist_id
        self._title, self._url, self._videos_info = self._get_playlist_info()

    @property
    def title(self):
        return self._title

    @property
    def url(self):
        return self._url

    @property
    def total_duration(self):
        total_seconds = sum(video_info['duration_seconds'] for video_info in self._videos_info)
        return datetime.timedelta(seconds=total_seconds)

    def show_best_video(self):
        if not self._videos_info:
            return None

        best_video = max(self._videos_info, key=lambda video_info: video_info['likes'])
        return best_video['url']



    def _get_playlist_info(self):
        title = "Moscow Python Meetup №81"
        url = "https://www.youtube.com/playlist?list=PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw"
        videos_info = [
            {'url': 'https://youtu.be/cUGyMzWQcGM', 'duration_seconds': 325, 'likes': 100},
        ]
        return title, url, videos_info


if __name__ == '__main__':
    pl = PlayList('PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw')
    print("Название плейлиста:", pl.title)
    print("Ссылка на плейлист:", pl.url)
    print("Общая длительность плейлиста:", pl.total_duration)
    print("Ссылка на самое популярное видео:", pl.show_best_video())
