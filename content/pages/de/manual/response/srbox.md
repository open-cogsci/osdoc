title: SR Box
hash: 4071d0970094db9727787578d613e899ded69a490b5c9c3e902816836096ee9a
locale: de
language: German

[TOC]

## Über das srbox Plugin

Die serielle Antwort (SR) Box ist eine Tastenbox, die speziell für die Erfassung von Reaktionen in psychologischen Experimenten entwickelt wurde. Die ursprüngliche Version, entwickelt von Psychology Software Tools, hat 5 Tasten, 5 Lichter und ist über die serielle Schnittstelle mit dem PC verbunden. Es gibt auch SR Box-kompatible Geräte von anderen Herstellern, die sich in der Anzahl der Tasten und Lichter unterscheiden und oft eine USB-Verbindung verwenden, die einen seriellen Anschluss emuliert.

Das SRBOX-Plugin für OpenSesame ermöglicht es Ihnen, die SR Box oder ein kompatibles Gerät in Ihren OpenSesame-Experimenten zu verwenden.

## Screenshot

%--
Abbildung:
  Quelle: srbox.png
  id: FigSrbox
  Bildunterschrift: Das srbox-Plugin in OpenSesame.
--%

## Gerätenamen einstellen

Standardmäßig versucht das Plugin, Ihre SR Box automatisch zu erkennen. Wenn das funktioniert, müssen Sie nichts ändern. Wenn Ihr Experiment einfriert, hat OpenSesame den falschen seriellen Anschluss gewählt und Sie müssen den Gerätenamen manuell eingeben. Unter Windows heißt das Gerät wahrscheinlich so ähnlich wie

```text
COM4
```

Unter Linux heißt das Gerät wahrscheinlich so ähnlich wie

```text
/dev/tty0
```

## Anforderungen

Eine SR Box oder kompatible Tastenbox. Nicht alle Tastenboxen sind kompatibel, siehe:

- %link:buttonbox%

## Verwendung der SR Box aus Python Inline-Code

Das `srbox`-Objekt existiert *nicht*, wenn das Plug-in im Dummy-Modus ist.

%-- include: include/api/srbox.md --%
