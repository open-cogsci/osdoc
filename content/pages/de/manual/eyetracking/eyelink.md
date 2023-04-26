title: Eyelink
hash: c9635275665d7dc2d7c42f6f480e386381284e31750ff4cd7cbaab5fb4522ee5
locale: de
language: German

[TOC]

## Über EyeLink

Die Eyelink-Reihe von Eye-Trackern, produziert von SR Research, gehört zu den am häufigsten verwendeten Eye-Trackern in der psychologischen Forschung. SR Research bietet Python-Bindungen für den Eyelink (genannt PyLink) an, die von PyGaze verwendet werden. Die Lizenz von PyLink ist nicht mit der von OpenSesame verwendeten Lizenz kompatibel. Aus diesem Grund ist PyLink nicht in der Standardverteilung von OpenSesame enthalten und muss separat installiert werden.

## SR Research Forum

Sie müssen einige Software aus dem SR Research Forum herunterladen. Dies ist ein geschlossenes Forum, aber Sie können sich kostenlos registrieren.

- <https://www.sr-support.com/>

## Windows

### Installation des EyeLink Developers Kit

Das Eyelink Developers Kit (manchmal auch Display Software genannt) enthält die erforderlichen Bibliotheken, um mit dem Eyelink PC zu kommunizieren. Hier finden Sie es:

- <https://www.sr-support.com/thread-13.html>

Wenn Sie die .zip-Datei entpacken und dann den .exe-Installer ausführen, wird die EyeLink-Anzeige in einem der folgenden Ordner installiert (abhängig von Ihrer Windows-Version:

```
C:\Program Files\SR Research\EyeLink\
C:\Program Files (x86)\SR Research\EyeLink
```

In diesem Ordner gibt es einen `libs`-Unterordner, den Sie zum Systempfad hinzufügen müssen (dieser wurde möglicherweise automatisch zum Pfad hinzugefügt, überprüfen Sie jedoch, ob dies der Fall ist). Sie können dies tun, indem Sie auf "Arbeitsplatz" klicken, "Systeminformationen anzeigen" auswählen, die Registerkarte "Erweitert" öffnen, auf "Umgebungsvariablen" klicken und `;C:\Program Files\SR Research\EyeLink\libs` oder (abhängig von Ihrem System) `;C:\Program Files (x86)\SR Research\EyeLink\libs` zur Path-Variable (unter Systemvariablen) hinzufügen.

### Installation von PyLink

PyLink ist die Python-Bibliothek für EyeLink-Unterstützung. PyLink ist in neueren Versionen der EyeLink-Anzeigesoftware (oben beschrieben) enthalten und Sie finden es in einem der folgenden Ordner (abhängig von Ihrer Windows-Version):

```
C:\Program Files\SR Research\EyeLink\SampleExperiments\Python
C:\Program Files (x86)\SR Research\EyeLink\SampleExperiments\Python
```

Alternativ können Sie Pylink auch hier herunterladen:

- <https://www.sr-support.com/thread-13.html>

Um PyLink in OpenSesame zu installieren, kopieren Sie einfach den Ordner mit dem PyLink in den OpenSesame-Programmordner oder in den `Lib\site-packages`-Unterordner. In einigen Fällen hat der `pylink`-Ordner einen Namen wie `pylink27-amd64`, in diesem Fall müssen Sie ihn einfach in `pylink` umbenennen.

__Wichtig:__ Die Python-Version von PyLink muss mit der Python-Version Ihrer OpenSesame-Installation übereinstimmen. In den meisten Fällen bedeutet dies, dass Sie PyLink für Python 3.7 benötigen.

## Ubuntu

Die EyeLink-Anzeigesoftware kann direkt aus einem Repository installiert werden. Dadurch werden auch PyLink und verschiedene nützliche Tools, wie der `edf2asc`-Konverter, installiert.

```bash
sudo add-apt-repository "deb http://download.sr-support.com/software SRResearch main"
sudo apt-get update
sudo apt-get install eyelink-display-software
```

Für weitere Informationen besuchen Sie bitte:

- <https://www.sr-support.com/thread-13.html>

## PyGaze

Nachdem Sie die EyeLink-Anzeigesoftware und PyLink gemäß den obigen Anweisungen installiert haben, können Sie den EyeLink mit PyGaze verwenden! Siehe:

- %link:pygaze%