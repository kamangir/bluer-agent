title:::

- uses [crawl/two/hnpagency](../../crawl/two/hnpagency.md)

🔥

```bash
@select crawl-hnpagency-2026-02-04-17-17-32-d24z45

@select corpus-hnpagency-$(@@timestamp)

@rag build_corpus upload .. .

@upload public,zip .
```

set:::object_crawl_name crawl-hnpagency-2026-02-04-17-17-32-d24z45
set:::object_corpus_name corpus-hnpagency-2026-02-04-63hokm

metadata:::get:::object_crawl_name

metadata:::get:::object_corpus_name

object:::get:::object_corpus_name