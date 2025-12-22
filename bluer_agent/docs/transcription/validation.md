# transcription: validation

🔥

```bash
@select ai-agent-transcription-$(@@timestamp)
```


# farsi

```bash
@agent transcription validate \
	filename=farsi.wav . \
	record,play,upload \
	language=fa,verbose
```

```yaml
"\u0645\u062F\u0627\u06CC\u0646\u0648\u0628 \u06CC\u0646\u06A9\u0646 \u0627\u062A\
  \ \u0646\u06A9\u0645 \u062F\u0627\u06CC\u0646\u0648\u0628 \u0632\u0627\u0646 \u0645\
  \u062F\u0627\u0628\u0631\u0632 \u06CC\u0647\u062F\u0646 \u0627\u062A \u0647\u062F\
  \u0645 \u062F\u0627\u0628\u0631\u0628 \u0641\u0644\u0648\u0632"

```

[farsi.wav](https://github.com/kamangir/assets/blob/main/ai-agent-speech-to-text-2025-12-18-r5hbwu/farsi.wav)

# english

```bash
@agent transcription validate \
	filename=english.wav . \
	record,play,upload \
	language=en,verbose
```

```yaml
Racism is how societies teach themselves to rot from the inside.
...

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


