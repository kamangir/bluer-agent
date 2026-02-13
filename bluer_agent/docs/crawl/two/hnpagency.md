# crawl: two: hnpagency

- repeats [one](./one.md).
- deeper run at [hnpagency.com](https://hnpagency.com/).

```bash
@select crawl-hnpagency-$(@timestamp)

@crawl collect \
    root=https://hnpagency.com/,review,upload . \
    --page-count 100 \
    --max-depth 10

@upload public,zip .

@upload public,filename=hnpagency_com.pkl.html .
```


[crawl-hnpagency-2026-02-05-13-14-24-2txahw.tar.gz](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/crawl-hnpagency-2026-02-05-13-14-24-2txahw.tar.gz)

[crawl-hnpagency-2026-02-05-13-14-24-2txahw/hnpagency_com.pkl.html](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/crawl-hnpagency-2026-02-05-13-14-24-2txahw/hnpagency_com.pkl.html)


<details>
<summary>metadata</summary>

```yaml
{}

```

</details>

