import argparse

from bluer_agent.audio.properties import AudioProperties


def test_audio_properties():
    properties = AudioProperties()

    assert isinstance(properties.as_str(), str)

    command = properties.record_command(filename="this/that.wav")
    assert isinstance(command, list)
    for item in command:
        assert isinstance(item, str)

    parser = argparse.ArgumentParser("some name")
    AudioProperties.add_args(parser)
