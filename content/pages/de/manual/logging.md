title: Protokollierung und Lesen von Datendateien
hash: 6c081bb9571ecf270fcbd02104d88319bf6044245745b621d549cbc38c34e370
locale: de
language: German

Überprüfen Sie immer dreifach, ob Ihre Daten korrekt protokolliert wurden, bevor Sie Ihr Experiment starten!
{: .page-notification}

[TOC]


## Verwendung des Logger-Elements

OpenSesame protokolliert Ihre Daten nicht automatisch. Stattdessen müssen Sie ein LOGGER-Element einfügen, in der Regel am Ende Ihrer Versuchssequenz.

%--
figure:
 id: FigLogger
 source: logger.png
 caption: |
  Das LOGGER-Element.
--%

Der einfachste Weg, den LOGGER zu verwenden, besteht darin, die Option "Automatisch alle Variablen protokollieren" aktiviert zu lassen. Auf diese Weise werden alle Variablen, die OpenSesame kennt, in die Log-Datei geschrieben, mit Ausnahme derjenigen, die ausdrücklich ausgeschlossen sind (siehe unten).

Sie können ausdrücklich *einschließen*, welche Variablen Sie protokollieren möchten. Der Hauptgrund dafür ist, wenn Sie feststellen, dass einige Variablen fehlen (weil OpenSesame sie nicht automatisch erkannt hat) oder wenn Sie die Option "Automatisch alle Variablen protokollieren" deaktiviert haben.

Sie können auch bestimmte Variablen ausdrücklich von der Log-Datei ausschließen. Der Hauptgrund dafür besteht darin, die Log-Dateien sauber zu halten, indem Variablen ausgeschlossen werden, die im Allgemeinen nicht nützlich sind.

Im Allgemeinen sollte man nur ein Logger-Element erstellen und dieses LOGGER bei Bedarf an verschiedenen Stellen im Experiment wiederverwenden (d. h. verknüpfte Kopien desselben LOGGER-Elements verwenden). Wenn Sie mehrere Logger erstellen (anstatt ein einzelnes Logger-Element mehrfach zu verwenden), schreiben sie alle in dieselbe Log-Datei, und das Ergebnis wird chaotisch sein!

## Verwendung von Python Inline-Skript

Sie können die `log`-Objekt verwenden, um in die Log-Datei zu schreiben:

~~~ .python
log.write('Dies wird in die Log-Datei geschrieben!')
~~~

Für weitere Informationen siehe:

- %link:log%

Im Allgemeinen sollten Sie nicht direkt in die Log-Datei schreiben und gleichzeitig ein LOGGER-Element verwenden; dies führt zu unübersichtlichen Log-Dateien.

## Format der Datendateien

Wenn Sie das Standard LOGGER-Element verwendet haben, sind die Datendateien im folgenden Format formatiert (einfach standard csv):

- Klartext
- kommagetrennt
- doppelte Anführungszeichen (wörtliche doppelte Anführungszeichen werden durch Rückwärtsschrägstriche escaped)
- Unix-Stil Zeilenumbrüche
- UTF-8 codiert
- Spaltennamen in der ersten Zeile

## Lesen und Verarbeiten von Datendateien

### In Python mit Pandas oder DataMatrix

In Python können Sie [pandas](http://pandas.pydata.org/) verwenden, um csv-Dateien zu lesen.

```python
import pandas
df = pandas.read_csv('subject-1.csv')
print(df)
```

Oder [DataMatrix](https://datamatrix.cogsci.nl/):

```python
from datamatrix import io
dm = io.readtxt('subject-1.csv')
print(dm)
```

### In R

In R können Sie einfach die `read.csv()` Funktion verwenden, um eine einzelne Datendatei zu lesen.

~~~ .R
df = read.csv('subject-1.csv', encoding = 'UTF-8')
head(df)
~~~

Außerdem können Sie die `read_opensesame()` Funktion aus dem [readbulk](https://github.com/pascalkieslich/readbulk) Paket verwenden, um mehrere Datendateien einfach zu lesen und zu einer großen Datentabelle zusammenzuführen. Das Paket ist auf CRAN verfügbar und kann über `install.packages('readbulk')` installiert werden.

~~~ .R
# Lesen und Zusammenführen aller in dem Ordner 'raw_data' gespeicherten Datendateien
library(readbulk)
df = read_opensesame('raw_data')
~~~

### In JASP

[JASP](http://jasp-stats.org/), ein Open-Source-Statistikpaket, öffnet csv-Dateien ohne weiteres.

### In LibreOffice Calc

Wenn Sie eine csv-Datei in LibreOffice Calc öffnen, müssen Sie das genaue Datenformat angeben, wie in %FigLibreOffice dargestellt. (Die Standardeinstellungen sind oft korrekt.)

%--
figure:
 source: libreoffice.png
 id: FigLibreOffice
--%

### In Microsoft Excel

In Microsoft Excel müssen Sie den Textimport-Assistenten verwenden.

### Zusammenführen mehrerer Datendateien in eine große Datei

Für manche Zwecke, wie zum Beispiel die Verwendung von Pivot-Tabellen, kann es praktisch sein, alle Datendateien in eine große Datei zusammenzuführen. Mit Python DataMatrix können Sie dies mit dem folgenden Skript tun:

```python
import os
from datamatrix import DataMatrix, io, operations as ops

# Ändere dies in den Ordner, der die .csv-Dateien enthält
SRC_FOLDER = 'student_data'
# Ändere dies in eine Liste von Spaltennamen, die du behalten möchtest
COLUMNS_TO_KEEP = [
    'RT_search',
    'load',
    'memory_resp'
]


dm = DataMatrix()
for basename in os.listdir(SRC_FOLDER):
    path = os.path.join(SRC_FOLDER, basename)
    print('Lese {}'.format(path))
    dm <<= ops.keep_only(io.readtxt(path), *COLUMNS_TO_KEEP)
io.writetxt(dm, 'zusammengeführte-daten.csv')
```


## Logging in OSWeb

Wenn du ein Experiment im Browser mit OSWeb ausführst, funktioniert das Logging anders als wenn du ein Experiment auf dem Desktop ausführst.

Insbesondere, wenn du ein OSWeb-Experiment direkt aus OpenSesame startest, wird die Protokolldatei am Ende des Experiments heruntergeladen. Diese Protokolldatei hat das Format `.json`. Wenn du ein OSWeb-Experiment von JATOS aus startest, gibt es keine Protokolldatei als solche, sondern alle Daten werden an JATOS gesendet, von wo aus sie heruntergeladen werden können.

Sieh auch:

- %link:manual/osweb/workflow%



[libreoffice]: http://www.libreoffice.org/
[openoffice]: http://www.openoffice.org/
[gnumeric]: http://projects.gnome.org/gnumeric/
[log-func]: /python/skript-in-einer-Zeile/#inline_script.log
[codecs]: http://docs.python.org/2/library/codecs.html
[ppa]: https://launchpad.net/~smathot/+archive/cogscinl/