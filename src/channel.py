import json
import os
from pprint import pprint

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
        inf = self.youtube.channels().list(id=channel_id, part='snippet,statistics').execute()

        self.__channel_id = channel_id
        self.url = f"https://www.youtube.com/channel/{channel_id}"
        self.title = inf['items'][0]['snippet']['title']
        self.description = inf['items'][0]['snippet']['description']
        self.subscriber_count = inf['items'][0]['statistics']['subscriberCount']
        self.video_count = inf['items'][0]['statistics']['videoCount']
        self.view_count = inf['items'][0]['statistics']['viewCount']

    def __repr__(self):
        return self.title

    @property
    def channel_id(self):
        return self.__channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        inf = self.youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        print(json.dumps(inf, indent=2, ensure_ascii=False))

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


mp = Channel('UC-OVMPlMA3-YCIeg4z5z23A')
pprint(mp.atr_to_dict())
