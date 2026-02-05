# rag: query: hnpagency

uses [build/hnpagency](../build/hnpagency.md)

```bash
@select rag-query-$(@timestamp)

@rag query - \
	corpus-hnpagency-2026-02-04-34rd2w \
	"چطور برای تبلیغات محلی تصمیم بگیرم؟" .

@upload public,filename=query.html .
```


[rag-query-2026-02-05-13-35-37-16yog5/query.html](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/rag-query-2026-02-05-13-35-37-16yog5/query.html)
