# rag: build: one

using [top advertising agencies in iran](https://trainomarketing.com/top-advertising-agency-in-iran/).

uses [crawl/three](../crawl/three.md)

```bash
@select $BLUER_AGENT_CRAWL_TEST_OBJECT

@select corpus-$(@@timestamp)
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
  - https://irannovin.net/departments/
  - https://irannovin.net/clients
  - https://irannovin.net/blog/
  - "https://irannovin.net/\u062A\u0645\u0627\u0633-\u0628\u0627-\u0645\u0627/"
  https://korosheh.com:
  - https://korosheh.com
  - https://korosheh.com/services
  - https://korosheh.com/branding-marketing
  - https://korosheh.com/digital-marketing
  - https://korosheh.com/video-marketing

```

```bash
@rag build_corpus - .. .
```

```yaml
corpus:
- https://badkoobeh.com/
- https://irannovin.net/
- https://korosheh.com
- https://eshareh.com/
- https://tusi.co/
- https://daarvag.com
- https://sainaagency.com
- https://andisheparsi.com
corpus-not:
- https://maat.com
- https://felesh.com

```
