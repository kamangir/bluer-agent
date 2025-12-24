title:::

```bash
@select corpus-$(@timestamp)

python3 -m bluer_agent.crawl.collect \
    --root https://badkoobeh.com/ \
    --page-count 5 \
    --max-depth 2 \
    --out site_text.pkl.gz

python3 -m bluer_agent.crawl.review
```