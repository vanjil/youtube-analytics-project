from src.video import Video, PLVideo, PlayList

if __name__ == '__main__':
    video1 = Video('AWX4JnAnjBE', 'GIL в Python: зачем он нужен и как с этим жить', 'https://www.youtube.com/watch?v=AWX4JnAnjBE', 1000, 50)
    video2 = PLVideo('4fObz_qw9u4', 'PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC', 'MoscowPython Meetup 78 - вступление', 'https://www.youtube.com/watch?v=4fObz_qw9u4', 500, 30)

    playlist = PlayList('PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC', 'Python Meetup Playlist', 'https://www.youtube.com/playlist?list=PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC')
    playlist.add_video(video1)
    playlist.add_video(video2)

    # Проверяем вывод
    assert str(video1) == 'GIL в Python: зачем он нужен и как с этим жить'
    assert str(video2) == 'MoscowPython Meetup 78 - вступление'
    assert playlist.total_duration.total_seconds() == 1500  # сумма длительностей видео
    assert playlist.show_best_video() == 'https://www.youtube.com/watch?v=AWX4JnAnjBE'  # ссылка на самое популярное видео
