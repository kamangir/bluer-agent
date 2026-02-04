# crawl: two: hnpagency

repeats [two:a](./a.md).

🔥

# shorten the code
```bash
@select crawl-hnpagency-$(@timestamp)

@crawl collect \
    root=https://hnpagency.com/ . \
    --page-count 5 \
    --max-depth 2

@crawl review - .

@upload - .

@upload public,zip .

@upload public,filename=xyz.pkl.html . # <- refactor, remove filename
```


[TBA.tar.gz](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/TBA.tar.gz)

[TBA/hnpagency_com.pkl.html](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/TBA/hnpagency_com.pkl.html)

```yaml
{}

```
