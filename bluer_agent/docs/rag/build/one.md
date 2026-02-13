# rag: build: one

- using [top advertising agencies in iran](https://trainomarketing.com/top-advertising-agency-in-iran/).
- uses [crawl/three](../../crawl/three.md)

```bash
@select $BLUER_AGENT_CRAWL_TEST_OBJECT

@select corpus-$(@@timestamp)

@rag build_corpus upload .. .

@upload public,zip .
```


```yaml
{}

```

```yaml
{}

```

[corpus-2026-02-05-xckrj1.tar.gz](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/corpus-2026-02-05-xckrj1.tar.gz)
