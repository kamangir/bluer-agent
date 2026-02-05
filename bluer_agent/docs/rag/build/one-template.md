title:::

- using [top advertising agencies in iran](https://trainomarketing.com/top-advertising-agency-in-iran/).
- uses [crawl/three](../../crawl/three.md)

```bash
@select $BLUER_AGENT_CRAWL_TEST_OBJECT

@select corpus-$(@@timestamp)

@rag build_corpus upload .. .

@upload public,zip .
```

set:::object_crawl_name env:::BLUER_AGENT_CRAWL_TEST_OBJECT
set:::object_corpus_name env:::BLUER_AGENT_RAG_CORPUS_TEST_OBJECT

metadata:::get:::object_crawl_name

metadata:::get:::object_corpus_name

object:::get:::object_corpus_name