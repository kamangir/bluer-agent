title:::

uses [build/hnpagency](../build/hnpagency.md)

```bash
@select rag-query-$(@timestamp)

@rag query - \
	corpus-hnpagency-2026-02-04-34rd2w \
	"چطور برای تبلیغات محلی تصمیم بگیرم؟" .

@upload public,filename=query.html .
```

set:::object_name rag-query-2026-02-05-15-10-39-q2ki73

object:::get:::object_name:::query.html