title:::

- uses [build/badkoobeh](../build/badkoobeh.md).

```bash
@select rag-query-$(@timestamp)

@rag query - \
	$BLUER_AGENT_RAG_CORPUS_SINGLE_ROOT_TEST_OBJECT \
	"چطور برای تبلیغات محلی تصمیم بگیرم؟" .

@upload public,filename=query.html .
```

set:::object_name rag-query-2026-02-05-14-48-55-xag0g3

object:::get:::object_name:::query.html