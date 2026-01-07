# crawl: four

continues [three](./three.md).

```bash
@select crawl-$(@timestamp)

@crawl collect \
  root=https://badkoobeh.com/ . \
  --page-count 5 \
  --max-depth 2

@crawl review - .

@metadata upload .

@upload public,zip .

@upload public,filename=badkoobeh_com.pkl.html .
```


```yaml
crawl:
  https://badkoobeh.com/:
  - https://badkoobeh.com
  - https://badkoobeh.com/projects/
  - https://badkoobeh.com/services/
  - https://badkoobeh.com/about-us/
  - https://badkoobeh.com/clients/

```

[crawl-2026-01-07-22-04-24-fzxplo/badkoobeh_com.pkl.html](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/crawl-2026-01-07-22-04-24-fzxplo/badkoobeh_com.pkl.html)

[crawl-2026-01-07-22-04-24-fzxplo.tar.gz](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/crawl-2026-01-07-22-04-24-fzxplo.tar.gz)
