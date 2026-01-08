# crawl: two

continues [one](./one.md).


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


[TBA.tar.gz](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/TBA.tar.gz)

[TBA/badkoobeh_com.pkl.html](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/TBA/badkoobeh_com.pkl.html)

```yaml
{}

```
