# crawl: three

continues [two](./two.md).

```bash
@select crawl-$(@timestamp)

cat > metadata.yaml <<'EOF'
corpus:
  - https://badkoobeh.com/
  - https://irannovin.net/
  - https://korosheh.com
EOF

@crawl collect - . \
    --page-count 5 \
    --max-depth 2

@crawl review - .

@upload - .

@upload public,zip .

@upload public,filename=badkoobeh_com.pkl.html .
@upload public,filename=irannovin_net.pkl.html .
@upload public,filename=korosheh_com.pkl.html .
```


[crawl-2026-01-08-12-39-45-hflyuj.tar.gz](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/crawl-2026-01-08-12-39-45-hflyuj.tar.gz)

[crawl-2026-01-08-12-39-45-hflyuj/badkoobeh_com.pkl.html](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/crawl-2026-01-08-12-39-45-hflyuj/badkoobeh_com.pkl.html)

[crawl-2026-01-08-12-39-45-hflyuj/irannovin_net.pkl.html](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/crawl-2026-01-08-12-39-45-hflyuj/irannovin_net.pkl.html)

[crawl-2026-01-08-12-39-45-hflyuj/korosheh_com.pkl.html](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/crawl-2026-01-08-12-39-45-hflyuj/korosheh_com.pkl.html)

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
