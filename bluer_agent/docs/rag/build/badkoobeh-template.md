title:::

- uses [crawl/two/badkoobeh](../../crawl/two/badkoobeh.md)

🔥

```bash
@select $BLUER_AGENT_CRAWL_SINGLE_ROOT_TEST_OBJECT

@select corpus-badkoobeh-$(@@timestamp)

@rag build_corpus upload .. .

@upload public,zip .
```

set:::object_crawl_name env:::BLUER_AGENT_CRAWL_SINGLE_ROOT_TEST_OBJECT
set:::object_corpus_name env:::BLUER_AGENT_RAG_CORPUS_SINGLE_ROOT_TEST_OBJECT

metadata:::get:::object_crawl_name

metadata:::get:::object_corpus_name

object:::get:::object_corpus_name