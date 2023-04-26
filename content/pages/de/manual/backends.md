title: Backends
hash: 1447d1754e76a00442c1709babb3c8b9ef77f76eb2aeb0c1e6bb57c9a232512c
locale: de
language: German

Das *Backend* ist die Softwareschicht, die sich mit Eingaben (Tastatureingaben, Mauseingaben usw.) und Ausgaben (Bildschirmpräsentation, Tonwiedergabe usw.) befasst. Es gibt viele Bibliotheken, die diese Art von Funktionalität bieten, und OpenSesame könnte im Prinzip eine beliebige davon verwenden. Aus diesem Grund ist OpenSesame backend-unabhängig, in dem Sinne, dass Sie auswählen können, welches Backend verwendet werden soll. Derzeit gibt es vier Backends: *legacy*, *psycho*, *xpyriment* und *osweb*.

[TOC]

## Unterschiede und einige Tipps

Normalerweise werden Sie nicht bemerken, welches Backend verwendet wird. Die Unterschiede zwischen den Backends sind größtenteils technisch und solange Sie die grafische Benutzeroberfläche verwenden, funktionieren alle Backends mehr oder weniger auf die gleiche Weise. Es gibt jedoch einige Gründe, ein Backend gegenüber einem anderen zu bevorzugen:

- Wenn Sie das Experiment in einem Browser ausführen möchten, müssen Sie das Backend *osweb* auswählen.
- Backends unterscheiden sich in der [zeitlichen Präzision](%link:timing%).
	- Tipp: Wenn Sie Wert auf millisekundengenaue zeitliche Präzision legen, verwenden Sie *xpyriment* oder *psycho*.
- Backends unterscheiden sich in der Dauer der Stimulusvorbereitung.
	- Tipp: Wenn [Formulare](%link:manual/forms/about%) langsam sind, verwenden Sie *legacy*.
	- Tipp: Wenn das Intervall zwischen den Versuchen lang ist (aufgrund der Stimulusvorbereitung), verwenden Sie *legacy*.
- Sie können backend-spezifische Funktionen verwenden, wenn Sie Python-Code schreiben.
	- Tipp: Wenn Sie PsychoPy-Funktionalität verwenden möchten, verwenden Sie *psycho*.
	- Tipp: Wenn Sie Expyriment-Funktionalität verwenden möchten, verwenden Sie *xpyriment*.
	- Tipp: Wenn Sie PyGame-Funktionalität verwenden möchten, verwenden Sie *legacy*.
- Einige Backends sind nicht auf allen Plattformen verfügbar.

## Auswahl eines Backends

Sie können ein Backend in den allgemeinen Eigenschaften des Experiments auswählen (%FigSelect).

%--
figure:
 id: FigSelect
 source: fig-select.png
 caption: "Auswahl eines Backends"
--%

Wenn Sie das allgemeine Skript anzeigen (wählen Sie "Skripteditor anzeigen"), werden Ihnen tatsächlich sechs verschiedene Backends angezeigt: canvas, keyboard, mouse, sampler, color und clock. Die Combobox-Methode wählt automatisch eine geeignete, vordefinierte Kombination von Backends aus, aber Sie könnten theoretisch mischen und abgleichen.

Zum Beispiel wird beim Auswählen des *xpyriment* Backends der folgende Code generiert:

	set sampler_backend legacy
	set mouse_backend xpyriment
	set keyboard_backend legacy
	set color_backend legacy
	set clock_backend legacy
	set canvas_backend xpyriment

## xpyriment

Das Backend *xpyriment* basiert auf [Expyriment][], einer Bibliothek zur Erstellung von psychologischen Experimenten. Es handelt sich um ein leichtgewichtiges hardwarebeschleunigtes Backend mit ausgezeichneten Zeitgebungseigenschaften. Wenn Sie Wert auf zeitliche Präzision legen, aber keine komplexen Reize (z.B. Gabor-Patches, Random-Dot-Gratings usw.) erzeugen möchten, ist *xpyriment* eine gute Wahl.

### Verwendung von Expyriment direkt

Umfangreiche Dokumentation zu Expyriment finden Sie unter <http://www.expyriment.org/doc>. Der folgende Codeausschnitt zeigt eine Zeile Text:

~~~ .python
from expyriment import stimuli
text = stimuli.TextLine('Das ist Expyriment!')
text.present()
~~~

### Zitation

Obwohl Expyriment mit den binären Distributionen von OpenSesame gebündelt ist, handelt es sich um ein separates Projekt. Geben Sie bitte, wenn angebracht, die folgende Zitation zusätzlich zur Zitation von OpenSesame an:

Krause, F., & Lindemann, O. (im Druck). Expyriment: Eine Python-Bibliothek für kognitive und neurowissenschaftliche Experimente. *Behavior Research Methods*.
{: .reference}

## psycho

Das Psycho-Backend basiert auf [PsychoPy][], einer Bibliothek zur Erstellung von psychologischen Experimenten. Es ist hardwarebeschleunigt und bietet High-Level-Routinen zum Erstellen komplexer visueller Reize (driftende Gitter usw.). Wenn Sie Wert auf Timing legen und komplizierte Reize erzeugen möchten, ist Psycho eine gute Wahl.

### Verwendung von PsychoPy direkt

Sie finden ausführliche Dokumentation zu PsychoPy unter <http://www.psychopy.org/>. Wenn Sie PsychoPy in OpenSesame verwenden, ist es wichtig zu wissen, dass das Hauptfenster als `self.experiment.window` oder einfach `win` aufgerufen werden kann. Der folgende Code-Ausschnitt zeichnet einen Gabor-Patch:

~~~ .python
from psychopy import visual
gabor = visual.PatchStim(win, tex="sin", size=256, mask="gauss", sf=0.05, ori=45)
gabor.draw()
win.flip()
~~~

### Tutorials

Ein Tutorial speziell für die Verwendung von PsychoPy in OpenSesame:

- <http://www.cogsci.nl/blog/tutorials/211-a-bit-about-patches-textures-and-masks-in-psychopy>

Und ein allgemeineres PsychoPy-Tutorial:

- <http://gestaltrevision.be/wiki/coding>

### Zitat

Obwohl PsychoPy mit den binären Distributionen von OpenSesame gebündelt ist, handelt es sich um ein separates Projekt. Wenn es angemessen ist, zitieren Sie bitte die folgenden Werke zusätzlich zu OpenSesame:

Peirce, J. W. (2007). PsychoPy: Psychophysics software in Python. *Journal of Neuroscience Methods*, *162*(1-2), 8-13. doi:10.1016/j.jneumeth.2006.11.017
{: .reference}

Peirce, J. W. (2009). Generating stimuli for neuroscience using PsychoPy. *Frontiers in Neuroinformatics*, *2*(10). doi:10.3389/neuro.11.010.2008
{: .reference}

## legacy

Das Legacy-Backend basiert auf [PyGame][] im Nicht-OpenGL-Modus. Der Nachteil dabei ist, dass keine Hardwarebeschleunigung vorhanden ist und die Timing-Eigenschaften nicht so gut sind wie bei den psycho- oder xpyriment-Backends. Der Vorteil ist jedoch, dass PyGame sehr einfach zu verwenden, sehr zuverlässig und auf einer Vielzahl von Plattformen gut unterstützt ist.

### Sichtbarkeit des Mauszeigers

Auf einigen Systemen ist der Mauszeiger im Vollbildmodus beim Verwenden des *legacy* Backend nicht sichtbar. Sie können dies auf folgende Weise umgehen:

1. Öffnen Sie die *legacy* Backend-Einstellungen und stellen Sie "Doppelte Pufferung" auf "nein".
	- *Hinweis:* Dies kann v-sync deaktivieren, was für zeitkritische Experimente wichtig sein kann, wie [hier](%link:timing%) erläutert.
2. Öffnen Sie die *legacy* Backend-Einstellungen und stellen Sie "Benutzerdefinierter Cursor" auf "ja".
3. Wechseln Sie zu einem anderen Backend.

### PyGame direkt verwenden

PyGame ist gut dokumentiert und Sie finden alles, was Sie über die Verwendung von PyGame wissen müssen, unter <http://www.pygame.org/docs/>. Speziell für OpenSesame ist die Tatsache, dass die Anzeigefläche als `self.experiment.window` oder einfach `win` gespeichert ist. Der folgende Code-Ausschnitt, den Sie in ein INLINE_SCRIPT-Element einfügen könnten, zeichnet ein rotes Rechteck auf die Anzeige:

~~~ .python
import pygame # PyGame-Modul importieren
pygame.draw.rect(self.experiment.window, pygame.Color("red"),
	[20, 20, 100, 100]) # Zeichnen eines roten Rechtecks. Noch nicht angezeigt...
pygame.display.flip() # Anzeige aktualisieren, um das rote Rechteck zu zeigen.
~~~


## osweb

Das *osweb* Backend basiert auf OSWeb und ermöglicht die Ausführung von Experimenten in einem Browser. Weitere Informationen finden Sie unter:

- %link:manual/osweb/workflow%