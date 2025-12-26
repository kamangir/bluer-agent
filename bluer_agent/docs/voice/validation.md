# voice: validation

```bash
@select voice-$(@@timestamp)

@voice generate - . \
    "سلام، من رنگین هستم. چطور می‌تونم کمکتون کنم؟" \
    --speaker shahriyar

@assets publish extensions=mp3,push
```


[voice.mp3](https://github.com/kamangir/assets/blob/main/TBA/voice.mp3)
