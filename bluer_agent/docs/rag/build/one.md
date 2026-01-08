# rag: build: one

using [top advertising agencies in iran](https://trainomarketing.com/top-advertising-agency-in-iran/).

uses [crawl/three](../crawl/three.md)

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
{}

```

[corpus-2025-12-25-rx092a.tar.gz](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/corpus-2025-12-25-rx092a.tar.gz)
