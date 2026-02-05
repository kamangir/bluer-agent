title:::

uses [build/one](../build/one.md)

```bash
@select rag-query-$(@timestamp)

@rag query - \
    $BLUER_AGENT_RAG_CORPUS_TEST_OBJECT \
	"کدام شرکت در تبلیغات محیطی موفق‌تر بوده است؟" .

@upload public,filename=query.html .
```

set:::object_name rag-query-2026-02-05-13-35-04-zlld8c

object:::get:::object_name:::query.html