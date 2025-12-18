# ai-agent: transcription: validation

```bash
@select ai-agent-transcription-$(@@timestamp)
```


# farsi

```bash
@agent transcription validate \
	filename=farsi.wav,language=fa,record,upload .
```

```yaml
{}

```

[farsi.wav](https://github.com/kamangir/assets/blob/main//farsi.wav)

# english

```bash
@agent transcription validate \
	filename=english.wav,language=en,record,upload .
```

```yaml
{}

```

[english.wav](https://github.com/kamangir/assets/blob/main//english.wav)

---


<details>
<summary>code</summary>

```bash
@metadata upload
@assets publish extensions=wav,push
```

</details>


