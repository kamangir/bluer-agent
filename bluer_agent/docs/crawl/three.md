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
```


```yaml
{}

```

```bash
@crawl collect - . \
    --page-count 5 \
    --max-depth 2

@crawl review - .

@metadata upload .

@upload public,zip .
```

```yaml
{}

```

[](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/.tar.gz)
