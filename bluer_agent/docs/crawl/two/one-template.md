title:::

- continues [one](../one.md).
- uses bash.

```bash
@select crawl-badkoobeh-$(@timestamp)

@crawl collect \
    root=https://badkoobeh.com/,review,upload . \
    --page-count 10 \
    --max-depth 2

@upload public,zip .

@upload public,filename=badkoobeh_com.pkl.html .
```

set:::object_name crawl-badkoobeh-2026-02-05-13-12-12-kbq1lq

object:::get:::object_name

object:::get:::object_name:::badkoobeh_com.pkl.html

details:::metadata
metadata:::get:::object_name
details:::