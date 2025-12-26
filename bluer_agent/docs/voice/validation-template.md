title:::

```bash
@select voice-$(@@timestamp)

@voice generate filename=voice.mp3 . \
    "سلام، من رنگین هستم. چطور می‌تونم کمکتون کنم؟" \
    --speaker nourai

@assets publish extensions=mp3,push
```

set:::object_name TBA

assets:::get:::object_name/voice.mp3