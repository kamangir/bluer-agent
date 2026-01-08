title:::

using [top advertising agencies in iran](https://trainomarketing.com/top-advertising-agency-in-iran/).
 
```bash
@select crawl-$(@timestamp)

python3 -m bluer_agent.crawl\
    collect \
    --object_name $abcli_object_name \
    --root https://badkoobeh.com/ \
    --page-count 5 \
    --max-depth 2 \
    --out badkoobeh_com.pkl.gz

python3 -m bluer_agent.crawl \
    review \
    --object_name $abcli_object_name \
    --root https://badkoobeh.com/

@upload - .

@upload public,zip .

@upload public,filename=badkoobeh_com.pkl.html .
```

set:::object_name crawl-2026-01-08-12-30-13-kv4ify

object:::get:::object_name

object:::get:::object_name:::badkoobeh_com.pkl.html

metadata:::get:::object_name
