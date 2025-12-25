# crawl: three

continues [two](./two.md).

```bash
@select corpus-$(@timestamp)

cat > metadata.yaml <<'EOF'
corpus:
  - https://badkoobeh.com/
  - https://irannovin.net/
  - https://korosheh.com
EOF
```


```yaml
- https://badkoobeh.com/
- https://irannovin.net/
- https://korosheh.com

```

```bash
@crawl collect - . \
    --page-count 5 \
    --max-depth 2

@crawl review - .

@metadata upload .
```

```yaml
https://badkoobeh.com/:
- https://badkoobeh.com
- https://badkoobeh.com/projects/
- https://badkoobeh.com/services/
- https://badkoobeh.com/about-us/
- https://badkoobeh.com/clients/
https://irannovin.net/:
- https://irannovin.net
- https://irannovin.net/departments/
- https://irannovin.net/clients
- https://irannovin.net/blog/
- "https://irannovin.net/\u062A\u0645\u0627\u0633-\u0628\u0627-\u0645\u0627/"
https://korosheh.com:
- https://korosheh.com
- https://korosheh.com/services
- https://korosheh.com/branding-marketing
- https://korosheh.com/digital-marketing
- https://korosheh.com/video-marketing

```
