title: Ton
hash: 2a7ee6fde847af9407b8719c0f7ddecc8711cf1e09f8a2c6db320088aa8d67f1
locale: de
language: German

Die gebräuchlichste Methode, um Ton abzuspielen, ist die Verwendung des SAMPLER-Elements zum Abspielen von Audiodateien oder des SYNTH-Elements zum Abspielen einfacher Töne usw.

[TOC]

## Der Sampler

Der SAMPLER spielt eine einzelne Sounddatei ab, normalerweise aus dem Dateipool.

Sounddateien werden immer mit der Abtastrate wiedergegeben, die vom OpenSesame-Sampler-Backend verwendet wird. Wenn Ihre Probe zu schnell (hohe Tonlage) oder zu langsam (niedrige Tonlage) zu sein scheint, können Sie die Abtastrate Ihrer Sounddatei in einem Soundeditor anpassen oder die vom OpenSesame-Sampler-Backend verwendete Abtastrate ändern (unter "Backend-Einstellungen und Informationen anzeigen" im Reiter "Allgemein").

Der SAMPLER hat einige Optionen:

- *Sounddatei* gibt die abzuspielende Datei an.
- *Lautstärke* zwischen 0 (stumm) und 1 (normale Lautstärke).
- *Pan* reduziert den rechten (negative Werte) oder linken (positive Werte) Kanal. Für vollständiges Panning geben Sie "left" oder "right" ein.
- *Tonhöhe* gibt die Wiedergabegeschwindigkeit an, wobei 1 der ursprünglichen Geschwindigkeit entspricht.
- *Stopp nach* gibt an, wie lange die Sounddatei abgespielt werden soll. Wenn beispielsweise ein Wert von 100 ms eingegeben wird, wird die Wiedergabe nach 100 ms gestoppt, unabhängig von der Länge der Sounddatei. Ein Wert von 0 ms bedeutet, dass die Sounddatei vollständig abgespielt wird.
- *Fade in* gibt die Einblendzeit für die Sounddatei an. Wenn beispielsweise ein Wert von 100 ms eingegeben wird, wird die Sounddatei stumm gestartet und erreicht innerhalb von 100 ms den Höchstwert.
- *Dauer* gibt die Dauer des SAMPLER-Elements an, bevor das nächste Element präsentiert wird. Dies muss nicht der Länge der Sounddatei entsprechen. Wenn beispielsweise die Dauer des Samplers auf 0 ms eingestellt ist, geht OpenSesame direkt zum Element, das auf den SAMPLER folgt (z. B. ein Sketchpad), *während die Sounddatei im Hintergrund weiter abgespielt wird*. Zusätzlich zu einem numerischen Wert können Sie die Dauer auf "keypress" (Tastendruck warten), "mouseclick" (Mausklick warten) oder "sound" (warten, bis der SAMPLER fertig ist) einstellen.

## Der Synthesizer

Der SYNTH ist ein einfacher Sound-Synthesizer.

Sie können eine Reihe von Optionen festlegen:

- *Wellenform* kann auf Sinus, Sägezahn, Rechteck oder weißes Rauschen eingestellt werden.
- *Anschwellzeit* ist die Zeit, die der Ton benötigt, um die maximale Lautstärke zu erreichen (d. h. Fade-in).
- *Abklingzeit* ist die Zeit, die der Ton benötigt, um auszuklingen (d. h. Fade-out). Beachten Sie, dass das Abklingen innerhalb der Länge des Tons erfolgt.
- *Lautstärke* zwischen 0 und 100%.
- *Pan* reduziert den rechten (negative Werte) oder linken (positive Werte) Kanal. Das Einstellen von Pan auf -20 oder 20 schaltet den rechten oder linken Kanal vollständig stumm.
- *Länge* gibt die Länge des Tons in Millisekunden an.
- *Dauer* gibt die Dauer des SYNTH-Elements an, bevor das nächste Element präsentiert wird. Dies muss nicht der Länge des Tons entsprechen. Beispielsweise kann die Dauer des SYNTH auf 0 ms eingestellt werden, um direkt zum nächsten Element (z. B. ein SKETCHPAD) zu gelangen, während der Ton im Hintergrund weiter abgespielt wird. Zusätzlich zu einem numerischen Wert können Sie die Dauer auf "keypress" (Tastendruck warten), "mouseclick" (Mausklick warten) oder "sound" (warten, bis der SYNTH fertig ist) einstellen.

## Tonwiedergabe in Python

Sie können das SAMPLER-Objekt und die SYNTH-Funktion verwenden, um visuelle Reize in Python zu präsentieren:

- %link:sampler%
- %link:manual/python/common%

## Audio Low Latency-Plugins

Das Hauptziel der Audio Low Latency-Plugins, entwickelt von Bob Rosbag, besteht darin, Audio mit minimalen und vorhersehbaren Latenzen abzuspielen und aufzunehmen, um eine hohe Genauigkeit und Präzision zu erreichen. Das `PyAlsaAudio`-Paket, das das Linux ALSA-Audiosystem verwendet, erzielte die besten Ergebnisse innerhalb von Python. `PortAudio` und `sounddevice` sind plattformübergreifend und funktionieren sowohl unter Windows als auch unter Linux.

Die Plugins sind standardmäßig nicht installiert, können aber über pip installiert werden:

```bash
pip install opensesame-plugin-audio-low-latency
```

Siehe auch:

- <https://pypi.org/project/opensesame-plugin-audio-low-latency/>