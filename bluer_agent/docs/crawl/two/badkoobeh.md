# crawl: two: badkoobeh

- repeats [one](./one.md).
- deeper run at [badkoobeh.com/](https://badkoobeh.com/).

```bash
@select crawl-badkoobeh-$(@timestamp)

@crawl collect \
    root=https://badkoobeh.com/,review,upload . \
    --page-count 100 \
    --max-depth 10

@upload public,zip .

@upload public,filename=badkoobeh_com.pkl.html .
```


[crawl-badkoobeh-2026-02-05-13-13-07-5zdn2b.tar.gz](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/crawl-badkoobeh-2026-02-05-13-13-07-5zdn2b.tar.gz)

[crawl-badkoobeh-2026-02-05-13-13-07-5zdn2b/badkoobeh_com.pkl.html](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/crawl-badkoobeh-2026-02-05-13-13-07-5zdn2b/badkoobeh_com.pkl.html)


<details>
<summary>metadata</summary>

```yaml
{}

```

</details>

