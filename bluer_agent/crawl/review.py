import argparse

from bluer_objects import objects

from bluer_agent.crawl import file
from bluer_agent.crawl.functions import url_to_filename


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument(
        "--root", required=True, help='Root URL, e.g. "https://badkoobeh.com/"'
    )
    p.add_argument("--object_name")
    args = p.parse_args()

    file.load(
        objects.path_of(
            object_name=args.object_name,
            filename="{}.pkl.gz".format(url_to_filename(args.root)),
        )
    )


if __name__ == "__main__":
    main()
