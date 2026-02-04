title:::

repeats [two:badkoobeh](./badkoobeh.md) for [hnpagency.com](https://hnpagency.com/).

```bash
@select crawl-hnpagency-$(@timestamp)

@crawl collect \
    root=https://hnpagency.com/,review,upload . \
    --page-count 100 \
    --max-depth 10

@upload public,zip .

@upload public,filename=hnpagency_com.pkl.html .
```

set:::object_name crawl-hnpagency-2026-02-04-17-17-32-d24z45

object:::get:::object_name

object:::get:::object_name:::hnpagency_com.pkl.html

details:::metadata
metadata:::get:::object_name
details:::