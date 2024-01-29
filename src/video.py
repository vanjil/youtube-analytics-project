# src/video.py

class Video:
    def __init__(self, video_id, title, video_url, views, likes):
        self.video_id = video_id
        self.title = title
        self.video_url = video_url
        self.views = views
        self.likes = likes

    def __str__(self):
        return self.title


class PLVideo(Video):
    def __init__(self, video_id, playlist_id, title, video_url, views, likes):
        super().__init__(video_id, title, video_url, views, likes)
        self.playlist_id = playlist_id

# Пример использования классов:

if __name__ == '__main__':
    # Создаем два экземпляра класса
    video1 = Video('AWX4JnAnjBE', 'GIL в Python: зачем он нужен и как с этим жить', 'https://www.youtube.com/watch?v=AWX4JnAnjBE', 1000, 50)
    video2 = PLVideo('4fObz_qw9u4', 'PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC', 'MoscowPython Meetup 78 - вступление', 'https://www.youtube.com/watch?v=4fObz_qw9u4', 500, 30)

    # Проверяем вывод
    assert str(video1) == 'GIL в Python: зачем он нужен и как с этим жить'
    assert str(video2) == 'MoscowPython Meetup 78 - вступление'
