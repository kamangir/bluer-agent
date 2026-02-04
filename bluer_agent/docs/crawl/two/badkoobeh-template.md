title:::

continues [one](../one.md).

```bash
@select crawl-badkoobeh-$(@timestamp)

@crawl collect \
    root=https://badkoobeh.com/,review,upload . \
    --page-count 100 \
    --max-depth 10

@upload public,zip .

@upload public,filename=badkoobeh_com.pkl.html .
```

set:::object_name env:::BLUER_AGENT_CRAWL_SINGLE_ROOT_TEST_OBJECT

object:::get:::object_name

object:::get:::object_name:::badkoobeh_com.pkl.html

details:::metadata
metadata:::get:::object_name
details:::