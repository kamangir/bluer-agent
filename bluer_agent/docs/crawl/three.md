# crawl: three

continues [two](./two.md).

```bash
@select corpus-$(@timestamp)

cat > metadata.yaml <<'EOF'
corpus:
  - https://badkoobeh.com/
  - https://irannovin.net/
  - https://korosheh.com
  - https://eshareh.com/
  - https://tusi.co/
  - https://daarvag.com
  - https://sainaagency.com
  - https://andisheparsi.com
EOF

@crawl collect - . \
    --page-count 5 \
    --max-depth 2

@crawl review - .

@metadata upload .
```

🔥


```yaml
{}

```
