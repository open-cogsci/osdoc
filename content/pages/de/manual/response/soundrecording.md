title: Tonaufnahme
hash: 541c85146b0c2948e62bcae0056f831ddb9cf3e2d2a3025254b3d54dac2e5f46
locale: de
language: German

[TOC]


## Audio Low Latency Plugins

Die Audio Low Latency Plugins, entwickelt von Bob Rosbag, sind die empfohlene Möglichkeit, Tonaufnahmen durchzuführen. Das Hauptziel dieses Plugin-Sets ist das Abspielen und Aufnehmen von Audio mit minimalen und vorhersehbaren Latenzzeiten, um eine hohe Genauigkeit und Präzision zu erreichen. Das `PyAlsaAudio`-Paket, das das Linux ALSA-Audiosystem verwendet, liefert die besten Ergebnisse innerhalb von Python. `PortAudio` und `sounddevice` sind plattformübergreifend und funktionieren sowohl unter Windows als auch unter Linux.

Die Plugins sind nicht standardmäßig installiert, können aber über pip installiert werden:

```bash
pip install opensesame-plugin-audio-low-latency
```

Siehe auch:

- <https://pypi.org/project/opensesame-plugin-audio-low-latency/>


## Sound-Recorder-Plugins

Die Sound-Recorder-Plugins, entwickelt von Daniel Schreij, werden nicht mehr aktiv weiterentwickelt und sind daher nicht mehr empfohlen. Weitere Informationen über dieses Plugin-Set finden Sie auf einer früheren Version dieser Seite:

- <https://osdoc.cogsci.nl/3.2/manual/response/soundrecording/>