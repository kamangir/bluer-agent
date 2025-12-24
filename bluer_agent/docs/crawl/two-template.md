title:::

continues [one](./one.md).

```bash
@select corpus-$(@timestamp)

@crawl collect \
    root=https://badkoobeh.com/ . \
    --page-count 5 \
    --max-depth 2

@crawl review root=https://badkoobeh.com/ .

@metadata upload .
```

set:::object_name corpus-2025-12-25-03-04-37-xfttjy

metadata:::get:::object_name:::crawl_collect