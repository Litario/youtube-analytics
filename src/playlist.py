import os
from datetime import timedelta
import isodate
from pprint import pprint
from icecream import ic

from googleapiclient.discovery import build

from src.video import Video


class PlayList:
    """
    Класс playlist ютуб-канала.
    """
    api_key: str = os.getenv('YouTube_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, playlist_id: str):
        self.__playlist_id = playlist_id
        self.url = f"https://www.youtube.com/playlist?list={self.__playlist_id}"

        self.__playlist_videos: dict = (self.__class__.youtube.playlistItems().
                                        list(playlistId=playlist_id,
                                             part='contentDetails', maxResults=50).
                                        execute())

        self.title = self.__class__.youtube.playlistItems().list(
            playlistId=playlist_id, part='snippet',
            maxResults=50).execute()['items'][0]['snippet']['title']

    @property
    def total_duration(self):
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.__playlist_videos['items']]

        video_response: dict = self.__class__.youtube.videos().list(part='contentDetails',
                                                                    id=','.join(video_ids)
                                                                    ).execute()

        total_duration = timedelta(0, 0, 0)
        for video in video_response['items']:
            # YouTube video duration is in ISO 8601 format
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            total_duration += duration

        return total_duration

    def show_best_video(self):
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.__playlist_videos['items']]

        ## словарь вида {url : int(количество лайков)}
        video_dict = {}
        for video_id in video_ids:
            vd = Video(video_id)
            video_dict[vd.url] = int(vd.like_count)

        ## словарь вида {int(количество лайков) : [url}
        video_like_dict = {}
        for k, v in video_dict.items():
            video_like_dict[v] = video_like_dict.get(v, []) + [k]

        return video_like_dict[max(video_like_dict)]


# pl = PlayList('PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw')
# pl.total_duration
# # print(pl.show_best_video())
