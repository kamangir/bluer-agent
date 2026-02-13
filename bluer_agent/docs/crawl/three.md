# crawl: three

continues [two](./two).

```bash
@select crawl-$(@timestamp)

cat > metadata.yaml <<'EOF'
corpus:
  - https://badkoobeh.com/
  - https://korosheh.com
EOF

@crawl collect - . \
    --page-count 5 \
    --max-depth 2

@crawl review - .

@upload - .

@upload public,zip .

@upload public,filename=badkoobeh_com.pkl.html .
@upload public,filename=korosheh_com.pkl.html .
```


[crawl-2026-02-05-13-17-07-mj236t.tar.gz](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/crawl-2026-02-05-13-17-07-mj236t.tar.gz)

[crawl-2026-02-05-13-17-07-mj236t/badkoobeh_com.pkl.html](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/crawl-2026-02-05-13-17-07-mj236t/badkoobeh_com.pkl.html)

[crawl-2026-02-05-13-17-07-mj236t/korosheh_com.pkl.html](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/crawl-2026-02-05-13-17-07-mj236t/korosheh_com.pkl.html)

```yaml
{}

```
