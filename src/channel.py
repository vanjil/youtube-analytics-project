import json

class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.title = None
        self.description = None
        self.url = None
        self.subscriber_count = None
        self.video_count = None
        self.view_count = None

        self._load_channel_data()

    def _load_channel_data(self):
        """Загружает данные канала из YouTube API."""
        api_key = "AIzaSyD39r7OwJbDwxtR1xyzFOM6i0UMYCF-gc0"
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

            self.title = snippet['title']
            self.description = snippet['description']
            self.url = f"https://www.youtube.com/channel/{self.channel_id}"
            self.subscriber_count = int(statistics['subscriberCount'])
            self.video_count = int(statistics['videoCount'])
            self.view_count = int(statistics['viewCount'])

            # Добавим необходимые атрибуты
            self.id = channel_data['id']

        else:
            print("Channel not found or API request failed.")

    @classmethod
    def get_service(cls):
        """Возвращает объект для работы с YouTube API."""
        api_key = "AIzaSyD39r7OwJbDwxtR1xyzFOM6i0UMYCF-gc0"
        return build('youtube', 'v3', developerKey=api_key)

    def to_json(self, filename):
        """Сохраняет значения атрибутов экземпляра Channel в файл JSON."""
        data = {
            'channel_id': self.channel_id,
            'title': self.title,
            'description': self.description,
            'url': self.url,
            'subscriber_count': self.subscriber_count,
            'video_count': self.video_count,
            'view_count': self.view_count,
            'id': self.id  # Добавим id к атрибутам, сохраняемым в файл
        }

        with open(filename, 'w') as json_file:
            json.dump(data, json_file, indent=2)

    def __str__(self):
        """Возвращает строковое представление канала."""
        return f"{self.title} ({self.url})"

    def __add__(self, other):
        """Сложение двух каналов: сумма подписчиков и просмотров."""
        if not isinstance(other, Channel):
            raise TypeError("Unsupported operand type. You can only add two Channel instances.")

        total_subscribers = self.subscriber_count + other.subscriber_count
        total_views = self.view_count + other.view_count

        return total_subscribers + total_views

    def __sub__(self, other):
        """Вычитание двух каналов: разница подписчиков и просмотров."""
        if not isinstance(other, Channel):
            raise TypeError("Unsupported operand type. You can only subtract two Channel instances.")

        diff_subscribers = self.subscriber_count - other.subscriber_count
        diff_views = self.view_count - other.view_count

        return diff_subscribers + diff_views

    def __eq__(self, other):
        """Сравнение двух каналов: равны, если id одинаковы."""
        if not isinstance(other, Channel):
            raise TypeError("Unsupported operand type. You can only compare two Channel instances.")

        return self.id == other.id

    def __lt__(self, other):
        """Сравнение двух каналов: меньше, если сумма подписчиков и просмотров меньше."""
        if not isinstance(other, Channel):
            raise TypeError("Unsupported operand type. You can only compare two Channel instances.")

        self_total = self.subscriber_count + self.view_count
        other_total = other.subscriber_count + other.view_count

        return self_total < other_total

    def __le__(self, other):
        """Сравнение двух каналов: меньше или равно, если сумма подписчиков и просмотров меньше или равна."""
        if not isinstance(other, Channel):
            raise TypeError("Unsupported operand type. You can only compare two Channel instances.")

        self_total = self.subscriber_count + self.view_count
        other_total = other.subscriber_count + other.view_count

        return self_total <= other_total

    def __gt__(self, other):
        """Сравнение двух каналов: больше, если сумма подписчиков и просмотров больше."""
        if not isinstance(other, Channel):
            raise TypeError("Unsupported operand type. You can only compare two Channel instances.")

        self_total = self.subscriber_count + self.view_count
        other_total = other.subscriber_count + other.view_count

        return self_total > other_total

    def __ge__(self, other):
        """Сравнение двух каналов: больше или равно, если сумма подписчиков и просмотров больше или равна."""
        if not isinstance(other, Channel):
            raise TypeError("Unsupported operand type. You can only compare two Channel instances.")

        self_total = self.subscriber_count + self.view_count
        other_total = other.subscriber_count + other.view_count

        return self_total >= other_total

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Item(name='{self.name}', price={self.price})"

    def __str__(self):
        return f"{self.name} - ${self.price}"