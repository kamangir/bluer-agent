# crawl: one

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


[TBA.tar.gz](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/TBA.tar.gz)

[TBA/badkoobeh_com.pkl.html](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/TBA/badkoobeh_com.pkl.html)

```yaml
{}

```
