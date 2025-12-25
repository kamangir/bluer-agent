title:::

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

set:::object_name env:::BLUER_AGENT_CRAWL_TEST_OBJECT

metadata:::get:::object_name:::corpus

```bash
@crawl collect - . \
    --page-count 5 \
    --max-depth 2

@crawl review - .

@metadata upload .

@upload public,zip .
```

metadata:::get:::object_name:::crawl

object:::get:::object_name