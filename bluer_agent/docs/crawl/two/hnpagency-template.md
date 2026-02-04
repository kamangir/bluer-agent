title:::

repeats [two:a](./a.md).

🔥

# shorten the code
```bash
@select crawl-hnpagency-$(@timestamp)

@crawl collect \
    root=https://hnpagency.com/,review . \
    --page-count 100 \
    --max-depth 10

@upload public,zip .

@upload public,filename=hnpagency_com.pkl.html .
```

set:::object_name crawl-hnpagency-2026-02-04-17-09-29-xqfnva

object:::get:::object_name

object:::get:::object_name:::hnpagency_com.pkl.html

metadata:::get:::object_name