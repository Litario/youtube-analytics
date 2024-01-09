import datetime

from src.playlist import PlayList

if __name__ == '__main__':
    pl = PlayList('PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw')

    ## название плейлиста изменилось
    # assert pl.title == "Moscow Python Meetup №81"
    assert pl.title == "Moscow Python Meetup №81. Вступление."

    assert pl.url == "https://www.youtube.com/playlist?list=PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw"

    duration = pl.total_duration
    assert str(duration) == "1:49:52"
    assert isinstance(duration, datetime.timedelta)
    assert duration.total_seconds() == 6592.0

    ## количество лайков изменилось
    # assert pl.show_best_video() == "https://youtu.be/cUGyMzWQcGM"
    assert pl.show_best_video() == ['https://youtu.be/nApYYXYL9qA', 'https://youtu.be/cUGyMzWQcGM']
