title:::

repeats [two:a](./a.md).

🔥

# shorten the code
```bash
@select crawl-simaara-$(@timestamp)

@crawl collect \
    root=https://simaara.com/ . \
    --page-count 5 \
    --max-depth 2

# absorb?
@crawl review - .

# absorb?
@upload - .

@upload public,zip .

# html is generated? 🤔
@upload public,filename=xyz.pkl.html . # <- refactor, remove filename
```

set:::object_name TBA

object:::get:::object_name

object:::get:::object_name:::simaara_com.pkl.html

metadata:::get:::object_name