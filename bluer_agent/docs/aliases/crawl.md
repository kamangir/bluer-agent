# aliases: crawl

```bash
@crawl \
	collect \
	[download,root=<url>,upload] \
	[-|<object-name>] \
	[--page-count 25] \
	[--max-depth 2] \
	[--timeout 15.0] \
	[--max-retries 4] \
	[--backoff-base 0.7] \
	[--backoff-jitter 0.4] \
	[--delay 0.2]
 . crawl <root> -> <object-name>.
@crawl \
	review \
	[download,root=<url>] \
	[.|<object-name>]
 . review <object-name>.
```
