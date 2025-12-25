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
```

metadata:::get:::object_name:::corpus

set:::object_name corpus-2025-12-25-12-52-52-m81i3e

```bash
@crawl collect - . \
    --page-count 5 \
    --max-depth 2

@crawl review - .

@metadata upload .
```

metadata:::get:::object_name:::crawl_collection