title:::

🔥

```bash
@select ai-agent-transcription-$(@@timestamp)
```

set:::object_name env:::BLUER_AGENT_TRANSCRIPTION_TEST_OBJECT

# farsi

```bash
@agent transcription validate \
	filename=farsi.wav . \
	record,play,upload \
	language=fa,verbose
```

metadata:::get:::object_name:::farsi

assets:::get:::object_name/farsi.wav

# english

```bash
@agent transcription validate \
	filename=english.wav . \
	record,play,upload \
	language=en,verbose
```

metadata:::get:::object_name:::english

assets:::get:::object_name/english.wav

---

details:::code
```bash
@metadata upload
@assets publish extensions=wav,push
```
details:::

