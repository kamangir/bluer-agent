from bluer_ai.tests.test_env import test_bluer_ai_env
from bluer_objects.tests.test_env import test_bluer_objects_env

from bluer_agent import env


def test_required_env():
    test_bluer_ai_env()
    test_bluer_objects_env()


def test_bluer_agent_env():
    assert env.BLUER_AGENT_MACHINE_USER_NAME

    assert env.BLUER_AGENT_API_KEY

    assert env.BLUER_AGENT_TRANSCRIPTION_ENDPOINT
    assert env.BLUER_AGENT_TRANSCRIPTION_TEST_OBJECT

    assert env.BLUER_AGENT_CHAT_ENDPOINT
    assert env.BLUER_AGENT_CHAT_TEST_OBJECT
