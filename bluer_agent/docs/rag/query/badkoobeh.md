# rag: query: badkoobeh

- uses [build/badkoobeh](../build/badkoobeh.md).

```bash
@select rag-query-$(@timestamp)

@rag query - \
	$BLUER_AGENT_RAG_CORPUS_SINGLE_ROOT_TEST_OBJECT \
	"چطور برای تبلیغات محلی تصمیم بگیرم؟" .

@upload public,filename=query.html .
```


[rag-query-2026-02-05-13-35-22-3r7nq9/query.html](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/rag-query-2026-02-05-13-35-22-3r7nq9/query.html)
