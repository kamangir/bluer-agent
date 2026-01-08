title:::

using [top advertising agencies in iran](https://trainomarketing.com/top-advertising-agency-in-iran/).

```bash
@select crawl-$(@timestamp)

python3 -m bluer_agent.crawl.collect \
    --root https://badkoobeh.com/ \
    --page-count 5 \
    --max-depth 2 \
    --out site_text.pkl.gz

python3 -m bluer_agent.crawl.review

@upload - .

@upload public,zip .

@upload public,filename=badkoobeh_com.pkl.html .
```

set:::object_name TBA

object:::get:::object_name

object:::get:::object_name:::badkoobeh_com.pkl.html

metadata:::get:::object_name
