# voice: validation

```bash
@select voice-$(@@timestamp)

@voice generate filename=voice.mp3 . \
    "سلام، من رنگین هستم. چطور می‌تونم کمکتون کنم؟" \
    --speaker nourai

@assets publish extensions=mp3,push
```


[voice.mp3](https://github.com/kamangir/assets/blob/main/TBA/voice.mp3)
