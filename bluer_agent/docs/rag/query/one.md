# rag: query: one

uses [build/one](../build/one.md)

```bash
@select rag-query-$(@timestamp)

@rag query - \
    $BLUER_AGENT_RAG_CORPUS_TEST_OBJECT \
	"کدام شرکت در تبلیغات محیطی موفق‌تر بوده است؟" .

@upload public,filename=query.html .
```


[rag-query-2026-02-05-13-35-04-zlld8c/query.html](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/rag-query-2026-02-05-13-35-04-zlld8c/query.html)
