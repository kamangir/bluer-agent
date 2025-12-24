# crawl: two

continues [one](./one.md).

```bash
@select corpus-$(@timestamp)

@crawl collect \
    root=https://badkoobeh.com/ . \
    --page-count 5 \
    --max-depth 2

@crawl review root=https://badkoobeh.com/ .

@metadata upload .
```


```yaml
- https://badkoobeh.com
- https://badkoobeh.com/projects/
- https://badkoobeh.com/services/
- https://badkoobeh.com/about-us/
- https://badkoobeh.com/clients/

```
