# aliases: crawl

```bash
@crawl \
	collect \
	[download,root=<url>|all,upload] \
	[-|<object-name>] \
	[--page-count 25] \
	[--max-depth 2] \
	[--timeout 15.0] \
	[--max-retries 4] \
	[--backoff-base 0.7] \
	[--backoff-jitter 0.4] \
	[--delay 0.2]
 . crawl -> <object-name>.
@crawl \
	review \
	[download,root=<url>|all] \
	[.|<object-name>]
 . review <object-name>.
```
