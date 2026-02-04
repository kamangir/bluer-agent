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
        "two/a.md",
        "two/b.md",
        "three.md",
    ]
]
