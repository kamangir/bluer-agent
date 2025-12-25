from bluer_ai.tests.test_env import test_bluer_ai_env
from bluer_objects.tests.test_env import test_bluer_objects_env

from bluer_agent import env


def test_required_env():
    test_bluer_ai_env()
    test_bluer_objects_env()


def test_bluer_agent_env():
    for var in [
        env.BLUER_AGENT_CHAT_TEMPERATURE,
    ]:
        assert isinstance(var, float)
        assert var >= 0

    for var in [
        env.BLUER_AGENT_CHAT_MAX_TOKENS,
        env.BLUER_AGENT_CHAT_TIMEOUT,
        env.BLUER_AGENT_TRANSCRIPTION_RETRIAL,
    ]:
        assert isinstance(var, int)
        assert var >= 0

    for var in [
        env.BLUER_AGENT_API_KEY,
        #
        env.BLUER_AGENT_AUDIO_TEST_OBJECT,
        #
        env.BLUER_AGENT_CHAT_ENDPOINT,
        env.BLUER_AGENT_CHAT_MODEL_NAME,
        env.BLUER_AGENT_CHAT_TEST_OBJECT,
        #
        env.BLUER_AGENT_CRAWL_TEST_OBJECT,
        #
        env.BLUER_AGENT_MACHINE_USER_NAME,
        #
        env.BLUER_AGENT_RAG_CORPUS_TEST_OBJECT,
        #
        env.BLUER_AGENT_TRANSCRIPTION_ENDPOINT,
        env.BLUER_AGENT_TRANSCRIPTION_MODEL_NAME,
        env.BLUER_AGENT_TRANSCRIPTION_TEST_OBJECT,
    ]:
        assert isinstance(var, str)
        assert var
