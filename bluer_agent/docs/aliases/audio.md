# aliases: audio

```bash
@audio \
	converse \
	[~download,,upload] \
	[corpus-badkoobeh-2026-02-05-hvu72u | <context-object-name>] \
	[-|<object-name>] \
	[--channels <1>] \
	[--crop_silence <0>] \
	[--greeting <str>] \
	[--language fa | en] \
	[--length <30>] \
	[--rate <16000>]
 . have a conversation based on the context.
@audio \
	install
 . install audio.
@audio \
	play \
	[download,filename=<audio.wav>] \
	[.|<object-name>]
 . play <object-name>/<audio.wav>.
@audio \
	record \
	[filename=<audio.wav>,play,upload] \
	[-|<object-name>] \
	[--channels <1>] \
	[--crop_silence <0>] \
	[--length <30>] \
	[--rate <16000>]
 . record <object-name>/<audio.wav>.
@audio \
	test
 . test audio.
```
