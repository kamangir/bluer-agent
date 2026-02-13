# crawl: two: one

- continues [one](../one.md).
- uses bash.

```bash
@select crawl-badkoobeh-$(@timestamp)

@crawl collect \
    root=https://badkoobeh.com/,review,upload . \
    --page-count 10 \
    --max-depth 2

@upload public,zip .

@upload public,filename=badkoobeh_com.pkl.html .
```


[crawl-badkoobeh-2026-02-05-13-12-12-kbq1lq.tar.gz](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/crawl-badkoobeh-2026-02-05-13-12-12-kbq1lq.tar.gz)

[crawl-badkoobeh-2026-02-05-13-12-12-kbq1lq/badkoobeh_com.pkl.html](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/crawl-badkoobeh-2026-02-05-13-12-12-kbq1lq/badkoobeh_com.pkl.html)


<details>
<summary>metadata</summary>

```yaml
{}

```

</details>

