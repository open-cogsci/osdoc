<div class="ClassDoc YAMLDoc" markdown="1">

# class __Sampler__

Die `Sampler` Klasse bietet Funktionen zum Abspielen von Soundproben. Üblicherweise erstellt man ein `Sampler`-Objekt mit der `Sampler()` Factory-Funktion, wie im Abschnitt [Erstellen eines Samplers](#creating-a-sampler) beschrieben.

__Beispiel:__

~~~ .python
src = pool['bark.ogg']
my_sampler = Sampler(src, volume=.5)
my_sampler.play()
~~~

[TOC]

## Wissenswertes

### Erstellen eines Samplers

Normalerweise erstellt man einen `Sampler` mit der `Sampler()` Factory-Funktion, die den vollständigen Pfad zu einer Sounddatei als ersten Argument nimmt.

~~~ .python
src = pool['bark.ogg']
my_sampler = Sampler(src)
~~~

Optional können Sie [Playback-Schlüsselwörter](#playback-keywords) an `Sampler()` weitergeben, um das Standardverhalten festzulegen:

~~~ .python
src = pool['bark.ogg']
my_sampler = Sampler(src, volume=.5)
~~~

### Abtastrate

Wenn Sie feststellen, dass Ihre Probe zu langsam (tiefe Tonhöhe) oder zu schnell (hohe Tonhöhe) abgespielt wird, stellen Sie sicher, dass die Abtastrate Ihrer Probe mit der Abtastrate des Sampler-Backends übereinstimmt, wie in den Backend-Einstellungen angegeben.

### Unterstützte Dateiformate

Sounddateien in den Formaten `.wav`, `.mp3` und `.ogg` werden unterstützt. Wenn Sie Proben aus einem anderen Format konvertieren müssen, können Sie [Audacity](http://sourceforge.net/projects/audacity/) verwenden.

### Playback-Schlüsselwörter

Funktionen, die `**playback_args` akzeptieren, nehmen die folgenden Keyword-Argumente:

- `volume` gibt eine Lautstärke zwischen `0.0` (stumm) und `1.0` (maximal) an.
- `pitch` gibt eine Tonhöhe (oder Wiedergabegeschwindigkeit) an, wobei Werte > 1 eine höhere Tonhöhe und Werte < 1 eine niedrigere Tonhöhe anzeigen.
- `pan` gibt eine Panoramaeinstellung an, wobei Werte < 0 eine Verschiebung nach links und Werte > 0 eine Verschiebung nach rechts anzeigen. Alternativ können Sie Pan auf 'left' oder 'right' einstellen, um nur einen einzigen Kanal abzuspielen.
- `duration` gibt die Dauer des Klangs in Millisekunden an oder ist auf `0` oder `None` eingestellt, um den gesamten Klang abzuspielen.
- `fade_in` gibt die Fade-in-Zeit (oder Angriff) des Klangs an, oder ist auf `0` oder `None` eingestellt, um Fade-in zu deaktivieren.
- `block` gibt an, ob das Experiment während der Wiedergabe (`True`) blockiert oder nicht (`False`) blockiert werden soll.

~~~ .python
src = pool['bark.ogg']
my_sampler = Sampler(src)
my_sampler.play(volume=.5, pan='left')
~~~

Playback-Schlüsselwörter wirken sich nur auf den aktuellen Vorgang aus (außer wenn sie beim Erstellen des Objekts an `Sampler()` weitergegeben werden). Um das Verhalten für alle nachfolgenden Vorgänge zu ändern, legen Sie die Wiedergabeeinstellungen direkt fest:

~~~ .python
src = pool['bark.ogg']
my_sampler = Sampler(src)
my_sampler.volume = .5
my_sampler.pan = 'left'
my_sampler.play()
~~~

Oder geben Sie die Playback-Schlüsselwörter beim Erstellen des Objekts an `Sampler()` weiter:

~~~ .python
src = pool['bark.ogg']
my_sampler = Sampler(src, volume=.5, pan='left')
my_sampler.play()
~~~

## close_sound(experiment)

Schließt den Mixer nach Abschluss des Experiments.


__Parameter__

- **experiment**: Das Experiment-Objekt.


## init_sound(experiment)

Initialisiert den pygame-Mixer vor Beginn des Experiments.


__Parameter__

- **experiment**: Das Experiment-Objekt.


## is_playing(self)

Überprüft, ob ein Klang gerade abgespielt wird.



__Rückgabe__

- True, wenn ein Klang abgespielt wird, False, wenn nicht.

__Beispiel__

~~~ .python
src = pool['my_sound.ogg']
my_sampler = Sampler(src)
my_sampler.play()
sleep(100)
if my_sampler.is_playing():
        print('Der Sampler spielt noch!')
~~~



## pause(self)

Pausiert die Wiedergabe (falls vorhanden).



__Beispiel__

~~~ .python
src = pool['my_sound.ogg']
my_sampler = Sampler(src)
my_sampler.play()
sleep(100)
my_sampler.pause()
sleep(100)
my_sampler.resume()
~~~



## play(\*arglist, \*\*kwdict)

Spielt den Klang ab.


__Parameter__

- **\*\*playback_args**: Optionale [Wiedergabe-Schlüsselwörter](#playback-keywords), die für diesen Aufruf von `Sampler.play()` verwendet werden. Dies wirkt sich nicht auf nachfolgende Vorgänge aus.

__Beispiel__

~~~ .python
src = pool['my_sound.ogg']
my_sampler = Sampler(src)
my_sampler.play(pitch=.5, block=True)
~~~



## resume(self)

Wiedergabe fortsetzen (falls vorhanden).



__Beispiel__

~~~ .python
src = pool['my_sound.ogg']
my_sampler = Sampler(src)
my_sampler.play()
sleep(100)
my_sampler.pause()
sleep(100)
my_sampler.resume()
~~~



## set_config(\*\*cfg)

Aktualisiert die konfigurierbaren Werte.


__Parameter__

- **\*\*cfg**: Die zu aktualisierenden konfigurierbaren Werte.


## stop(self)

Stoppt den aktuell abspielenden Ton (falls vorhanden).



__Beispiel__

~~~ .python
src = pool['my_sound.ogg']
my_sampler = Sampler(src)
my_sampler.play()
sleep(100)
my_sampler.stop()
~~~



## wait(self)

Blockiert, bis der Ton abgespielt ist oder kehrt sofort zurück,
wenn kein Ton abgespielt wird.



__Beispiel__

~~~ .python
src = pool['my_sound.ogg']
my_sampler = Sampler(src)
my_sampler.play()
my_sampler.wait()
print('Der Sampler ist fertig!')
~~~



</div>