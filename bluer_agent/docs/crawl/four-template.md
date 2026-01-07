title:::

continues [three](./three.md).

```bash
@select crawl-$(@timestamp)
```

set:::object_name TBA

```bash
@crawl collect \
  root=https://badkoobeh.com/ . \
  --page-count 5 \
  --max-depth 2

@crawl review - .

@metadata upload .

@upload public,zip .
```

metadata:::get:::object_name

object:::get:::object_name