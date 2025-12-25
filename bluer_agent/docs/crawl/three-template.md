title:::

continues [two](./two.md).

```bash
@select corpus-$(@timestamp)

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

@metadata upload .
```

set:::object_name corpus-2025-12-25-12-52-52-m81i3e

metadata:::get:::object_name:::crawl_collection