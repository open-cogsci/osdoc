title: Ton
hash: abc659dc7f36f6c760c6f029cd4e89ea9f3cf46e33e009701bc55bafd4f59b01
locale: de
language: German

Die gebräuchlichste Art, Sound abzuspielen, ist die Verwendung des SAMPLER-Items zur Wiedergabe von Audiodateien oder des SYNTH-Items zur Wiedergabe einfacher Pieptöne usw.

[TOC]

## The sampler

Der SAMPLER spielt eine einzelne Sounddatei ab, typischerweise aus dem Datei-Pool.

Sounddateien werden immer mit der Abtastrate abgespielt, die vom OpenSesame sampler backend verwendet wird. Wenn Ihr Sample beschleunigt (hohe Tonhöhe) oder verlangsamt (tiefe Tonhöhe) zu sein scheint, können Sie die Abtastrate Ihrer Sounddatei in einem Sound-Editor anpassen oder die vom OpenSesame sampler backend verwendete Abtastrate ändern (unter „Show backend settings and info“ im Reiter „General“).

Der SAMPLER hat einige Optionen:

- *Sound file* gibt die abzuspielende Datei an.
- *Volume* zwischen 0 (stumm) und 1 (normale Lautstärke).
- *Pan* regelt den rechten (negative Werte) oder linken (positive Werte) Kanal herunter. Für vollständiges Panning geben Sie „left“ oder „right“ ein,
- *Pitch* gibt die Wiedergabegeschwindigkeit an, wobei 1 der Originalgeschwindigkeit entspricht.
- *Stop after* gibt an, wie lange die Sounddatei abgespielt werden soll. Ein Wert von 100 ms bedeutet zum Beispiel, dass die Wiedergabe nach 100 ms gestoppt wird, unabhängig davon, wie lang die Sounddatei ist. Ein Wert von 0 ms bedeutet, dass die Sounddatei vollständig abgespielt wird.
- *Fade in* gibt die Einblendzeit für die Sounddatei an. Ein Wert von 100 ms bedeutet zum Beispiel, dass die Sounddatei stumm beginnt und innerhalb von 100 ms auf den Maximalwert ansteigt.
- *Duration* gibt die Dauer des sampler-Items an, bevor das nächste Item präsentiert wird. Diese muss nicht mit der Länge der Sounddatei übereinstimmen. Wenn die Dauer des sampler zum Beispiel auf 0 ms gesetzt ist, geht OpenSesame direkt zum auf den SAMPLER folgenden Item weiter (z. B. einem sketchpad), *während die Sounddatei im Hintergrund weiter abgespielt wird*. Zusätzlich zu einem numerischen Wert können Sie duration auf Folgendes setzen:
	- „keypress“, um auf einen Tastendruck zu warten
	- „mouseclick“, um auf einen Mausklick zu warten
	- „sound“, um zu warten, bis der sampler fertig abgespielt ist.

## The synth

Der SYNTH ist ein einfacher Soundsynthesizer.

Sie können eine
Reihe von Optionen angeben:

- *Waveform* kann auf sine, sawtooth, square oder white noise gesetzt werden
- *Attack* ist die Zeit, die der Sound benötigt, um die maximale Lautstärke zu erreichen (d. h. Fade-in).
- *Decay* ist die Zeit, die der Sound benötigt, um auszuklingen (d. h. Fade-out). Beachten Sie, dass der Decay innerhalb der Länge des Sounds auftritt.
- *Volume* zwischen 0 und 100 %
- *Pan* regelt den rechten (negative Werte) oder linken (positive Werte) Kanal herunter. Wenn pan auf -20 oder 20 gesetzt wird, wird der rechte bzw. linke Kanal vollständig stummgeschaltet.
- *Length* gibt die Länge des Sounds an (in Millisekunden).
- *Duration* gibt die Dauer des SYNTH-Items an, bevor das nächste Item präsentiert wird. Diese muss nicht mit der Länge des Sounds übereinstimmen. Zum Beispiel kann die Dauer des SYNTH auf 0 ms gesetzt werden, um direkt zum nächsten Item weiterzugehen (z. B. einem SKETCHPAD), während der Sound im Hintergrund weiter abgespielt wird. Zusätzlich zu einem numerischen Wert können Sie die Dauer auf „keypress“ setzen, um auf einen Tastendruck zu warten, auf „mouseclick“, um auf einen Mausklick zu warten, oder auf „sound“, um zu warten, bis der SYNTH fertig abgespielt ist.

## Sound-Timing in sampler und synth

Das Abspielen eines Sounds in OpenSesame umfasst zwei unabhängige Steuerungen: eine, die bestimmt, wie lange der Sound selbst abgespielt wird, und eine, die bestimmt, wie lange das Experiment beim aktuellen Item wartet, bevor es weitergeht. Den Unterschied zwischen diesen beiden Steuerungen zu verstehen, ist für präzises Stimulus-Timing entscheidend.

### Zwei unabhängige Steuerungen

#### Soundlänge

| Item | Parameter | Beschreibung |
|---|---|---|
| **Sampler** | **Stop after** | Schneidet die Audiodatei nach der angegebenen Anzahl von ms ab. Auf `0` gesetzt, wird die Datei bis zu ihrem natürlichen Ende abgespielt. |
| **Synth** | **Length** | Legt direkt fest, wie lange der erzeugte Ton dauert (in ms). Es gibt kein natürliches Ende über den angegebenen Wert hinaus. |

#### Item-Timing

Sowohl SAMPLER als auch SYNTH verwenden den Parameter *Duration*, der steuert, wie lange das Experiment beim Item bleibt, bevor es zum nächsten weitergeht. Er wirkt sich nicht direkt auf den Ton selbst aus.

| Duration value | Verhalten |
|---|---|
| `0` | Sofort weitergehen |
| *number* (ms) | Die angegebene Anzahl von ms warten und dann weitergehen |
| `sound` | Warten, bis der Ton vollständig abgespielt wurde |


### Allgemeine Regel

Mit *sound length* ist gemeint:
- *Stop after* für SAMPLER oder die natürliche Länge der Datei, wenn *Stop after* `0` ist
- *Length* für SYNTH

Dann gilt Folgendes:

| Condition | Result |
|---|---|
| *Duration* **<** sound length | Das Item endet vor dem Ton, sodass der Ton im nächsten Item weiterläuft |
| *Duration* = `sound` | Das Experiment wartet, bis der Ton beendet ist |
| *Duration* **≥** sound length | Das Item dauert länger als der Ton, sodass die Wiedergabe beendet ist, bevor das nächste Item beginnt |

### Hinweise

- Bei SAMPLER ist die tatsächliche Wiedergabezeit die natürliche Dateilänge, es sei denn, *Stop after* ist größer als `0`; in diesem Fall stoppt die Wiedergabe nach der angegebenen Dauer.
- Bei SYNTH ist die tatsächliche Wiedergabezeit immer gleich *Length*.
- Wenn *Duration* = `sound` ist, wartet das Experiment auf die tatsächliche Wiedergabezeit und berücksichtigt dabei *Stop after* für SAMPLER.

### Ton, der im nächsten Item weiterläuft

Ein Ton kann nach dem Ende des aktuellen Items weiter abgespielt werden, wenn *Duration* kürzer ist als die tatsächliche Wiedergabezeit. Das kann beabsichtigt sein, zum Beispiel wenn ein Ton im Hintergrund weiterlaufen soll, während das nächste Item angezeigt wird. Es kann aber auch unbeabsichtigt passieren, wenn *Duration* kürzer ist als erwartet; in diesem Fall kann der Ton in das nächste Versuchselement hineinragen.

## Tonwiedergabe in Python

Sie können das SAMPLER-Objekt und die SYNTH-Funktion verwenden, um visuelle Stimuli in Python darzubieten:

- %link:sampler%
- %link:manual/python/common%


## Audio Low Latency plugins

Das Hauptziel der von Bob Rosbag entwickelten Audio Low Latency plugins ist es, Audio mit minimalen und vorhersagbaren Latenzen abzuspielen und aufzuzeichnen, um eine hohe Genauigkeit und Präzision zu erreichen. Das `PyAlsaAudio`-Paket, das das Linux-ALSA-Audiosystem verwendet, lieferte innerhalb von Python die besten Ergebnisse. `PortAudio` und `sounddevice` sind plattformübergreifend und funktionieren sowohl unter Windows als auch unter Linux.

Die plugins sind nicht standardmäßig installiert, können aber über pip installiert werden:

```bash
pip install opensesame-plugin-audio-low-latency
```

Siehe auch:

- <https://pypi.org/project/opensesame-plugin-audio-low-latency/>