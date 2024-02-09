from src.video import Video

if __name__ == '__main__':
    try:
        broken_video = Video('broken_video_id')
        assert broken_video.title is None
        assert broken_video.like_count is None
    except Exception as e:
        print(f"An error occurred: {e}")
