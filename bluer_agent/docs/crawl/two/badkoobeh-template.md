title:::

continues [one](../one.md).

```bash
@select crawl-$(@timestamp)

@crawl collect \
    root=https://badkoobeh.com/ . \
    --page-count 5 \
    --max-depth 2

@crawl review - .

@upload - .

@upload public,zip .

@upload public,filename=badkoobeh_com.pkl.html .
```

set:::object_name crawl-2026-01-08-12-37-35-elxbeo

object:::get:::object_name

object:::get:::object_name:::badkoobeh_com.pkl.html

metadata:::get:::object_name