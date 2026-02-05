import pytest

from bluer_objects import objects
from bluer_objects import storage
from bluer_objects.storage.policies import DownloadPolicy

from bluer_agent import env
from bluer_agent.crawl import file


@pytest.mark.parametrize(
    ["object_name"],
    [
        [env.BLUER_AGENT_CRAWL_TEST_OBJECT],
        [env.BLUER_AGENT_CRAWL_SINGLE_ROOT_TEST_OBJECT],
    ],
)
def test_crawl_file(object_name: str):
    filename = "badkoobeh_com.pkl.gz"

    assert storage.download(
        object_name,
        policy=DownloadPolicy.DOESNT_EXIST,
    )

    success, results = file.load(
        object_name=object_name,
        filename=filename,
    )
    assert success
    assert isinstance(results, dict)

    key = "https://badkoobeh.com"
    assert key in results

    test_object_name = objects.unique_object("test_crawl_file")

    assert file.save(
        results=results,
        object_name=test_object_name,
        filename=filename,
    )

    success, results_loaded = file.load(
        object_name=test_object_name,
        filename=filename,
    )
    assert success

    assert results == results_loaded

    success = file.export(
        results=results,
        object_name=test_object_name,
        filename=filename,
    )
    assert success
