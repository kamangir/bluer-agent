docs = [
    {
        "path": "../docs/crawl",
    },
] + [
    {
        "path": f"../docs/crawl/{name}",
    }
    for name in [
        "one.md",
        "two",
        "two/badkoobeh.md",
        "two/hnpagency.md",
        "three.md",
    ]
]
