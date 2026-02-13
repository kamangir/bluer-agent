# transcription: validation

🔥

```bash
@select ai-agent-transcription-$(@@timestamp)
```


# farsi

```bash
@agent transcribe \
	filename=farsi.wav . \
	record,play,upload \
	language=fa,verbose
```

```yaml
{}

```

[farsi.wav](https://github.com/kamangir/assets/blob/main/ai-agent-speech-to-text-2025-12-18-r5hbwu/farsi.wav)

# english

```bash
@agent transcribe \
	filename=english.wav . \
	record,play,upload \
	language=en,verbose
```

```yaml
{}

```

[english.wav](https://github.com/kamangir/assets/blob/main/ai-agent-speech-to-text-2025-12-18-r5hbwu/english.wav)

---


<details>
<summary>code</summary>

```bash
@metadata upload
@assets publish extensions=wav,push
```

</details>


