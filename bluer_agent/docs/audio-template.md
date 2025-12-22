title:::

# record

```bash
@select audio-$(@@timestamp)

@audio record play,upload .

@audio play - .

@assets publish extensions=wav,push .
```

set:::object_name audio-2025-12-22-4styuj

assets:::get:::object_name/audio.wav

# listen

```bash
@select audio-$(@@timestamp)

@audio listen play,upload .

@audio play - .

@assets publish extensions=wav,push .
```

set:::object_name audio-2025-12-22-u3f5lh

assets:::get:::object_name/audio.wav