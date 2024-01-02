import json
import os

from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""
    api_key: str = os.getenv('YouTube_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str):
        """
        Экземпляр инициализируется id канала.
        Дальше все данные будут подтягиваться по API.
        """

        self.__channel_id = channel_id
        self.url = f"https://www.youtube.com/channel/{channel_id}"
        yt_info: dict = (self.__class__.youtube.
                         channels().list(id=channel_id,
                                         part='snippet,statistics').execute())
        channel_items = yt_info['items'][0]
        self.title = channel_items['snippet']['title']
        self.description = channel_items['snippet']['description']
        self.subscriber_count = channel_items['statistics']['subscriberCount']
        self.video_count = channel_items['statistics']['videoCount']
        self.view_count = channel_items['statistics']['viewCount']

    @property
    def channel_id(self):
        return self.__channel_id

    def __str__(self):
        return f"{self.title} ({self.url})"

    def __repr__(self):
        return self.title

    def __add__(self, other):
        return int(self.subscriber_count) + int(other.subscriber_count)

    def __sub__(self, other):
        return int(self.subscriber_count) - int(other.subscriber_count)

    def __gt__(self, other):
        return int(self.subscriber_count) > int(other.subscriber_count)

    def __ge__(self, other):
        return int(self.subscriber_count) >= int(other.subscriber_count)

    def __lt__(self, other):
        return int(self.subscriber_count) < int(other.subscriber_count)

    def __le__(self, other):
        return int(self.subscriber_count) <= int(other.subscriber_count)

    def __eq__(self, other):
        return int(self.subscriber_count) == int(other.subscriber_count)

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        yt_info = self.__class__.youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        print(json.dumps(yt_info, indent=2, ensure_ascii=False))

    @classmethod
    def get_service(cls):
        return Channel.youtube

    def to_json(self, file_name):
        output_dir_name = 'output'
        path = output_dir_name + '/' + file_name

        dct = self.__dict__
        json_dict = json.dumps(dct)

        with open(path, 'w') as file:
            file.write(json_dict)

    def atr_to_dict(self):
        return self.__dict__


# mp = Channel('UC-OVMPlMA3-YCIeg4z5z23A')
# pprint(mp.__dict__)
# print(mp.__class__)
# print(type(mp).__class__)
