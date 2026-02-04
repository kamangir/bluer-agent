title:::

repeats [two:a](./a.md).

🔥

# shorten the code
```bash
@select crawl-hnpagency-$(@timestamp)

@crawl collect \
    root=https://hnpagency.com/ . \
    --page-count 5 \
    --max-depth 2

@crawl review - .

@upload - .

@upload public,zip .

@upload public,filename=xyz.pkl.html . # <- refactor, remove filename
```

set:::object_name TBA

object:::get:::object_name

object:::get:::object_name:::hnpagency_com.pkl.html

metadata:::get:::object_name