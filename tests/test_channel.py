from src.channel import Channel

obj = Channel("MoscowPython", "UC-OVMPlMA3-YCIeg4z5z23A")

def test__channel_init():
    assert isinstance(obj, Channel)
    assert obj.name == "MoscowPython"
    assert obj.info["kind"] == "youtube#channelListResponse"
    assert isinstance(1, int)


