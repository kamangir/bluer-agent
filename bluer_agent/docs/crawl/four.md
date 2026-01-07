# crawl: four

continues [three](./three.md).

```bash
@select crawl-$(@timestamp)
```


```bash
@crawl collect \
  root=https://badkoobeh.com/ . \
  --page-count 5 \
  --max-depth 2

@crawl review - .

@metadata upload .

@upload public,zip .
```

```yaml
{}

```

[TBA](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/TBA.tar.gz)
