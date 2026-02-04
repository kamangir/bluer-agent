# crawl: two: simaara

repeats [two:a](./a.md).

🔥

# shorten the code
```bash
@select crawl-simaara-$(@timestamp)

@crawl collect \
    root=https://simaara.com/ . \
    --page-count 5 \
    --max-depth 2

# absorb?
@crawl review - .

# absorb?
@upload - .

@upload public,zip .

# html is generated? 🤔
@upload public,filename=xyz.pkl.html . # <- refactor, remove filename
```


[TBA.tar.gz](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/TBA.tar.gz)

[TBA/simaara_com.pkl.html](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/TBA/simaara_com.pkl.html)

```yaml
{}

```
