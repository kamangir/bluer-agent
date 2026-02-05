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
corpus:
- https://badkoobeh.com/
- https://korosheh.com
crawl:
  https://badkoobeh.com/:
  - https://badkoobeh.com
  - https://badkoobeh.com/projects/
  - https://badkoobeh.com/services/
  - https://badkoobeh.com/about-us/
  - https://badkoobeh.com/clients/
  https://korosheh.com:
  - https://korosheh.com
  - https://korosheh.com/services
  - https://korosheh.com/branding-marketing
  - https://korosheh.com/digital-marketing
  - https://korosheh.com/video-marketing

```

```yaml
crawl:
  roots:
    badkoobeh_com:
      chunks: 27
      pages: 5
      root: badkoobeh_com
    korosheh_com:
      chunks: 77
      pages: 5
      root: korosheh_com
  source: crawl-2026-02-05-13-17-07-mj236t

```

[corpus-2026-02-05-xckrj1.tar.gz](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/corpus-2026-02-05-xckrj1.tar.gz)
