# crawl: two: a

continues [one](../one.md).

```bash
@select crawl-$(@timestamp)

@crawl collect \
    root=https://badkoobeh.com/ . \
    --page-count 5 \
    --max-depth 2

@crawl review - .

@upload - .

@upload public,zip .

@upload public,filename=badkoobeh_com.pkl.html .
```


[crawl-2026-01-08-12-37-35-elxbeo.tar.gz](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/crawl-2026-01-08-12-37-35-elxbeo.tar.gz)

[crawl-2026-01-08-12-37-35-elxbeo/badkoobeh_com.pkl.html](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/crawl-2026-01-08-12-37-35-elxbeo/badkoobeh_com.pkl.html)

```yaml
crawl:
  https://badkoobeh.com/:
  - https://badkoobeh.com
  - https://badkoobeh.com/projects/
  - https://badkoobeh.com/services/
  - https://badkoobeh.com/about-us/
  - https://badkoobeh.com/clients/

```
