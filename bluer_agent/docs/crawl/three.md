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


[crawl-2025-12-25-13-33-15-7s08w8.tar.gz](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/crawl-2025-12-25-13-33-15-7s08w8.tar.gz)

[crawl-2025-12-25-13-33-15-7s08w8/badkoobeh_com.pkl.html](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/crawl-2025-12-25-13-33-15-7s08w8/badkoobeh_com.pkl.html)
[crawl-2025-12-25-13-33-15-7s08w8/irannovin_net.pkl.html](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/crawl-2025-12-25-13-33-15-7s08w8/irannovin_net.pkl.html)
[crawl-2025-12-25-13-33-15-7s08w8/korosheh_com.pkl.html](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/crawl-2025-12-25-13-33-15-7s08w8/korosheh_com.pkl.html)

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
