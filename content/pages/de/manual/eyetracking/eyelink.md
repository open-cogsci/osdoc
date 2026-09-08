title: EyeLink
hash: 37419c41f2ba79dc8903d36fe35edc800de2791247978b58d7a4c3ee07121ff1
locale: de
language: German

[TOC]

## Über EyeLink

Die von SR Research hergestellten EyeLink-Eye-Tracker gehören zu den in der psychologischen Forschung am häufigsten verwendeten Eye-Trackern. SR Research stellt Python-Bindings für die Kommunikation mit dem EyeLink bereit (PyLink genannt), die von PyGaze und ihrem eigenen EyeLink Plugin verwendet werden. 


## Installation von PyLink

Die Python-Bibliothek für die EyeLink-Integration ist auf PyPI als `sr-research-pylink` verfügbar. Sie bietet vollständige Unterstützung für Windows, macOS und Linux unter Python 2.7 bis 3.14 und kann daher in den neuesten OpenSesame-Installationen installiert werden.

Sie können sie direkt über das Terminal installieren:

```
pip install sr-research-pylink
```

**Wichtig:** Versuchen Sie *nicht*, `pylink` durch Ausführen von `pip install pylink` zu installieren. Dadurch wird ein völlig anderes, nicht verwandtes Paket installiert!

Weitere Informationen über `sr-research-pylink` finden Sie im SR Research Forum (kostenlose Registrierung erforderlich):

- <https://www.sr-research.com/support/> 
- <https://www.sr-research.com/support/thread-48.html>
	
## PyGaze

Nachdem Sie PyLink mithilfe der obigen Anweisungen installiert haben, können Sie EyeLink mit PyGaze verwenden! Siehe:

- %link:pygaze%

## SR Research EyeLink Plugin

SR Research bietet auch ein eigenes EyeLink-Plugin-Set für OpenSesame an. Dieses Plugin bietet zusätzliche EyeLink-Integration, die über PyGaze nicht verfügbar ist, beispielsweise einen Blickauslöser, EDF-Übertragung beim Abbrechen einer Aufgabe sowie vollständige Unterstützung während der Kameraübertragung für aktuelle EyeLink-Modelle. Um das Plugin zu installieren, führen Sie Folgendes aus:

```
pip install opensesame-plugin-eyelink
```

Weitere Informationen finden Sie unter:

- <https://www.sr-research.com/support/thread-52.html>

## Optional: EyeLink Developers Kit

Obwohl es nicht mehr erforderlich ist, um PyLink in OpenSesame auszuführen, bietet das EyeLink Developers Kit (manchmal EyeLink Display Software genannt) zusätzliche nützliche Werkzeuge, wie den Konverter `edf2asc`, Dokumentation und Offline-Installationsdateien (.whl) für `sr-research-pylink`.

Falls Sie diese Hilfsprogramme benötigen, finden Sie die Installer für Windows, macOS und Ubuntu-Repositories auf der SR Research Support-Website:

- <https://www.sr-research.com/support/forum-9.html>