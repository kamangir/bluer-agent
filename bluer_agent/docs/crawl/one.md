# crawl: one

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


[crawl-2026-01-08-12-30-13-kv4ify.tar.gz](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/crawl-2026-01-08-12-30-13-kv4ify.tar.gz)

[crawl-2026-01-08-12-30-13-kv4ify/badkoobeh_com.pkl.html](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/crawl-2026-01-08-12-30-13-kv4ify/badkoobeh_com.pkl.html)

```yaml
crawl:
  https://badkoobeh.com/:
  - https://badkoobeh.com
  - https://badkoobeh.com/projects/
  - https://badkoobeh.com/services/
  - https://badkoobeh.com/about-us/
  - https://badkoobeh.com/clients/

```
