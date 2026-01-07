title:::

continues [three](./three.md).

```bash
@select crawl-$(@timestamp)

@crawl collect \
  root=https://badkoobeh.com/ . \
  --page-count 5 \
  --max-depth 2

@crawl review - .

@metadata upload .

@upload public,zip .

@upload public,filename=badkoobeh_com.pkl.html .
```

set:::object_name crawl-2026-01-07-22-04-24-fzxplo

metadata:::get:::object_name

object:::get:::object_name/badkoobeh_com.pkl.html

object:::get:::object_name