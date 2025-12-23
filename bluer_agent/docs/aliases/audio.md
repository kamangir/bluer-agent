# aliases: audio

```bash
@audio \
	install
 . install.
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
```
