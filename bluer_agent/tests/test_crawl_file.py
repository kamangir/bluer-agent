import pytest

from bluer_objects import objects
from bluer_objects import storage
from bluer_objects.storage.policies import DownloadPolicy

from bluer_agent import env
from bluer_agent.crawl import file


@pytest.mark.parametrize(
    ["object_name"],
    [[env.BLUER_AGENT_CRAWL_TEST_OBJECT]],
)
def test_crawl_file(object_name: str):
    assert storage.download(
        object_name,
        policy=DownloadPolicy.DOESNT_EXIST,
    )

    success, content = file.load(
        objects.path_of(
            object_name=object_name,
            filename="badkoobeh_com.pkl.gz",
        )
    )
    assert success
    assert isinstance(content, dict)

    key = "https://badkoobeh.com"
    assert key in content

    test_object_name = objects.unique_object("test_crawl_file")
    test_filename = objects.path_of(
        object_name=test_object_name,
        filename="badkoobeh_com.pkl.gz",
    )

    assert file.save(content, test_filename)

    success, content_loaded = file.load(test_filename)
    assert success

    assert content == content_loaded
