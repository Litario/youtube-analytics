import os

from googleapiclient.discovery import build


class Video:
    """Класс для видео из YOUTUBE-канала"""
    api_key: str = os.getenv('YouTube_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, video_id: str):
        """
        Экземпляр инициализируется id видео.
        Дальше все данные будут подтягиваться по API.
        """
        try:
            self.video_id = video_id

            self.url = f"https://youtu.be/{self.video_id}"

            video_response = (self.__class__.youtube.videos().
                              list(part='snippet,statistics,'
                                        'contentDetails,topicDetails', id=self.video_id).
                              execute())
            video_items = video_response['items'][0]

            self.title = video_items['snippet']['title']
            self.view_count = video_items['statistics']['viewCount']
            self.like_count = video_items['statistics']['likeCount']
        except IndexError:
            print('Неправильный id видео')
            self.url = self.title = self.view_count = self.like_count = None
        except Exception:
            print('Неизвестная ошибка')

    def __str__(self):
        return str(self.title)


class PLVideo(Video):
    """Класс для play-листов из YOUTUBE-канала"""

    def __init__(self, video_id: str, playlist_id: str):
        """
        Экземпляр инициализируется id видео и id play-листа.
        Дальше все данные будут подтягиваться по API.
        """
        super().__init__(video_id)
        self.playlist_id = playlist_id
