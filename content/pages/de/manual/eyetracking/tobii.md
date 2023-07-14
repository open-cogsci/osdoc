title: Tobii
hash: a383da57d44200882bf0aa52f84f681e06fecc7982e5a785150b5372d2d75259
locale: de
language: German

PyGaze bietet *experimentelle* Unterstützung für Tobii Eye-Tracker.

`tobii-research` ist die Python-Bibliothek für Tobii-Unterstützung. Ab Juli 2023 benötigt `tobii-research` Python 3.10, während OpenSesame standardmäßig Python 3.11 verwendet. Daher ist, bis `tobii-research` für Python 3.11 aktualisiert wird, der einfachste Weg, OpenSesame mit Tobii-Unterstützung zu installieren, die Erstellung einer Python 3.10-Umgebung über Anaconda.

Das klingt kompliziert, ist es aber wirklich nicht. Um dies zu tun, lesen Sie zunächst das allgemeine Verfahren zur Installation von OpenSesame über Anaconda, wie es auf der Download-Seite beschrieben ist:

- %link:download%

Sobald Sie das allgemeine Verfahren verstanden haben, beginnen Sie mit der Erstellung einer Python 3.10-Umgebung, setzen Sie die Anweisungen von der Download-Seite fort und installieren Sie dann `tobii-research`:

```
# Beginnen Sie mit der Erstellung einer Python 3.10-Umgebung
conda create -n opensesame-py3 python=3.10
conda activate opensesame-py3
# Befolgen Sie nun die Anweisungen von der Download-Seite
# ...
# Installieren Sie dann die Tobii-Unterstützung
pip install tobii-research
# Und starten Sie jetzt OpenSesame!
opensesame
```

Für weitere Informationen siehe:

- %link:pygaze%
- <https://rapunzel.cogsci.nl/manual/environment/>
- <http://www.tobii.com/en/eye-tracking-research/global/>