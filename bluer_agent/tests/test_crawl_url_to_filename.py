import pytest

from bluer_agent.crawl.functions import url_to_filename


@pytest.mark.parametrize(
    ["url", "filename"],
    [
        [
            "https://badkoobeh.com",
            "badkoobeh_com",
        ],
        [
            "https://badkoobeh.com/clients/%d8%b4%d8%a7%d9%88%d9%85%d8%a7/",
            "badkoobeh_com_clients__d8_b4_d8_a7_d9_88_d9_85_d8_a7",
        ],
    ],
)
def test_crawl_url_to_filename(
    url: str,
    filename: str,
):
    assert url_to_filename(url) == filename
