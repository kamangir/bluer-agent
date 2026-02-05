title:::

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

set:::object_name env:::BLUER_AGENT_CRAWL_TEST_OBJECT

object:::get:::object_name

object:::get:::object_name:::badkoobeh_com.pkl.html

object:::get:::object_name:::korosheh_com.pkl.html

metadata:::get:::object_name