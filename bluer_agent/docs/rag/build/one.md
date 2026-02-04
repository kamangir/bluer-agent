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
- https://irannovin.net/
- https://korosheh.com
crawl:
  https://badkoobeh.com/:
  - https://badkoobeh.com
  - https://badkoobeh.com/projects/
  - https://badkoobeh.com/services/
  - https://badkoobeh.com/about-us/
  - https://badkoobeh.com/clients/
  https://irannovin.net/:
  - https://irannovin.net
  - "https://irannovin.net/\u0646\u0645\u0648\u0646\u0647-\u06A9\u0627\u0631\u0647\
    \u0627/"
  - https://irannovin.net/departments/
  - https://irannovin.net/clients
  - https://irannovin.net/blog/
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
    irannovin_net:
      chunks: 17
      pages: 5
      root: irannovin_net
    korosheh_com:
      chunks: 77
      pages: 5
      root: korosheh_com
  source: crawl-2026-01-08-12-39-45-hflyuj

```

[corpus-2026-02-04-k9njk5.tar.gz](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/corpus-2026-02-04-k9njk5.tar.gz)
