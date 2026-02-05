title:::

- uses [crawl/two/hnpagency](../../crawl/two/hnpagency.md)

```bash
@select crawl-hnpagency-2026-02-04-17-17-32-d24z45

@select corpus-hnpagency-$(@@timestamp)

@rag build_corpus upload .. .

@upload public,zip .
```

set:::object_crawl_name crawl-hnpagency-2026-02-05-13-14-24-2txahw
set:::object_corpus_name corpus-hnpagency-2026-02-05-qm23g7

details:::crawl metadata
metadata:::get:::object_crawl_name
details:::

rag metadata
metadata:::get:::object_corpus_name

object:::get:::object_corpus_name