title:::

```bash
@select voice-$(@@timestamp)

@voice generate - . \
    "سلام، من رنگین هستم. چطور می‌تونم کمکتون کنم؟" \
    --speaker shahriyar

@assets publish extensions=mp3,push
```

set:::object_name TBA

assets:::get:::object_name/voice.mp3