from bluer_objects import file

from bluer_agent.assets.path import get_path


def test_assets():
    assert file.exists(get_path("./query.html"))
