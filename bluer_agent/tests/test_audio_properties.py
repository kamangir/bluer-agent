import argparse

from bluer_agent.audio.properties import AudioProperties


def test_audio_properties():
    properties = AudioProperties()

    assert isinstance(properties.as_str(), str)

    command = properties.record_command(filename="this/that.wav")
    assert isinstance(command, str)

    parser = argparse.ArgumentParser("some name")
    parser.add_argument(
        "task",
        type=str,
        help="some-task",
    )
    AudioProperties.add_args(parser)
    args = parser.parse_args()
