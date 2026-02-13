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
crawl:
  https://badkoobeh.com/:
  - https://badkoobeh.com
  - https://badkoobeh.com/projects/
  - https://badkoobeh.com/services/
  - https://badkoobeh.com/about-us/
  - https://badkoobeh.com/clients/
  - https://badkoobeh.com/careers/
  - https://badkoobeh.com/contact/
  - https://badkoobeh.com/blog/
  - https://badkoobeh.com/casestudy/
  - https://badkoobeh.com/works/%da%a9%d8%a7%d8%b1-%d8%ad%d8%b1%d9%81%d9%87-%d8%a7%db%8c%d8%8c-%d8%a7%d8%a8%d8%b2%d8%a7%d8%b1-%d8%ad%d8%b1%d9%81%d9%87-%d8%a7%db%8c-%d9%85%db%8c-%d8%ae%d9%88%d8%a7%d9%87%d8%af/

```

</details>

