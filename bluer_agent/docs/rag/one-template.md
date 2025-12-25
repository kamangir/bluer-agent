title:::

using [top advertising agencies in iran](https://trainomarketing.com/top-advertising-agency-in-iran/).

```bash
@select $BLUER_AGENT_CRAWL_TEST_OBJECT

@select corpus-$(@@timestamp)
```

set:::object_crawl_name env:::BLUER_AGENT_CRAWL_TEST_OBJECT
set:::object_corpus_name env:::BLUER_AGENT_RAG_CORPUS_TEST_OBJECT

metadata:::get:::object_crawl_name

```bash
@rag build_corpus - .. .
```

metadata:::get:::object_corpus_name