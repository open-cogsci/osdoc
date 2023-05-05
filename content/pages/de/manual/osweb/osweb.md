title: OSWeb
hash: 9fc0b6a63aa91000243df7d41fe843fc7eb52f30b3e6ac866728b5e0e8ebde0a
locale: de
language: German

[TOC]

## Über OSWeb

OSWeb ist eine Online-Laufzeitumgebung für OpenSesame-Experimente. Das bedeutet, es handelt sich um eine JavaScript-Bibliothek, die OpenSesame-Experimente interpretiert und ausführt.

## Die OSWeb-Erweiterung

Die OSWeb-Erweiterung für OpenSesame (%FigOSWebExtension) ermöglicht es Ihnen, Experimente in einem Browser zu testen und in einem Format zu exportieren, das Sie in [JATOS](%url:jatos%) importieren können.

%--
figure:
 id: FigOSWebExtension
 source: osweb-extension.png
 caption: Die OSWeb-Erweiterung für OpenSesame.
--%

## Testen in einem Browser

- Öffnen Sie in OpenSesame die OSWeb-Erweiterung (Menü → Extras → OSWeb).
- Die Erweiterung führt eine einfache (und unvollständige) Prüfung durch, ob Ihr Experiment mit OSWeb kompatibel zu sein scheint.
- Wenn keine Probleme festgestellt werden, klicken Sie auf "Test experiment in external browser" oder auf die entsprechende Schaltfläche in der Hauptwerkzeugleiste.
- Dadurch wird das Experiment in Ihrem Standardbrowser geöffnet, damit Sie überprüfen können, ob das Experiment wie erwartet ausgeführt wird (%FigTestRun).
- Sie können auch auf die Schaltfläche "Run in browser" in der Hauptwerkzeugleiste klicken (Alt+Ctrl+W)

%--
figure:
 id: FigTestRun
 source: testrun.png
 caption: Der Begrüßungsbildschirm von OSWeb beim Testen des Experiments in einem Browser.
--%

## Debugging

Stellen Sie zunächst sicher, dass Ihr Experiment nur unterstützte Funktionen verwendet, wie unten beschrieben. Führen Sie das Experiment als nächstes auf herkömmliche Weise (nicht im Browser) in OpenSesame aus. Dies gibt Ihnen die informativsten Fehlermeldungen, die Sie zum Debuggen verwenden können.

Wenn Ihr Experiment nur unterstützte Funktionen verwendet und normal in OpenSesame ausgeführt wird, können Sie die Browserkonsole verwenden, um JavaScript-Fehlermeldungen anzuzeigen. Diese sind viel weniger informativ als OpenSesames Fehlermeldungen, können aber dennoch hilfreich sein. Jeder Browser hat eine andere Methode, um auf die Konsole zuzugreifen. In Chrome können Sie auf die Konsole zugreifen, indem Sie mit der rechten Maustaste klicken, Inspect (`Ctrl+Shift+I`) auswählen und dann auf die Registerkarte Console wechseln (siehe %FigChromeConsole). In Firefox können Sie auf die Konsole zugreifen, indem Sie auf das Menüsymbol in der oberen rechten Ecke klicken und dann Web Developer → Web Console (`Ctrl+Shift+I`) auswählen.

Wenn Sie in Ihrem Experiment INLINE_JAVASCRIPT-Elemente verwenden, ist die Browserkonsole auch eine leistungsstarke Möglichkeit, um Ihre Skripte zu debuggen, wie hier beschrieben:

- %link:manual/javascript/about%

%--
figure:
 id: FigChromeConsole
 source: chrome-console.png
 caption: Chromes Browserkonsole.
--%

## Unterstützte Funktionen

Sie können überprüfen, ob Ihr Experiment mit OSWeb kompatibel ist, indem Sie die Kompatibilitätsprüfung (%FigOSWebExtension) verwenden. Diese Kompatibilitätsprüfung ist ziemlich oberflächlich. Eine vollständigere Übersicht über unterstützte Funktionen finden Sie unten.

__Wichtig__: Viele unterstützte Funktionen wurden in OSWeb 1.4 hinzugefügt. Überprüfen Sie daher Ihre OSWeb-Version gegen die Versionshinweise in der Liste unten.

- `advanced_delay`
- `feedback`
    - Siehe `sketchpad`
- `form_consent` (unterstützt >= v1.4)
- `form_text_display` (unterstützt >= 1.4)
- `form_text_input` (unterstützt >= 1.4)
    - Nicht unterstützt: Vollbildmodus
- `form_multiple_choice` (unterstützt >= 1.4)
- `inline_html` (unterstützt >= 1.4)
- `inline_javascript`
- `keyboard`
    - Nicht unterstützt: Tastenfreigabe
    - Nicht unterstützt: HSV-, HSL- und CIELab-Farbräume
- `logger`
- `loop`
    - Nicht unterstützt: Fortsetzen nach Pause
    - Nicht unterstützt: Deaktivierung von "Evaluate on first cycle"
    - Nicht unterstützt: Einschränkungen (Pseudorandomisierung)
    - Unterstützt >= 1.4: Dateiquelle
- `mouse`
    - Nicht unterstützt: Mausfreigabe
    - Nicht unterstützt: Verknüpftes sketchpad
- `notepad`
- `repeat_cycle`
- `reset_feedback`
- `sampler`
    - Unterstützt >= 1.4.12: Panning, Tonhöhe und Fade-In
    - Unterstützt >= 1.4.12: Sound-Wiedergabe in Safari auf Mac OS oder in jedem Browser auf iOS
    - Nicht unterstützt: Stop after
- `sequence`
- `sketchpad`
    - Nicht unterstützt: Benannte Elemente
    - Unterstützt >= 1.4: Bildrotation
    - Nicht unterstützt: HSV-, HSL- und CIELab-Farbräume
- `touch_response`

Die Kompatibilitätsprüfung kann auch Fehler der folgenden Art anzeigen:

```bash
Die Prepare-Phase für Item new_logger wird mehrmals hintereinander aufgerufen
Die Run-Phase für Item new_logger wird mehrmals hintereinander aufgerufen
```

Dieser Fehler resultiert aus der Struktur des Experiments, insbesondere der Verwendung von verknüpften Kopien. Es ist nicht immer einfach zu verstehen, woher dieser Fehler kommt, aber Sie können mehr über die Prepare-Run-Strategie in [diesem Artikel](%url:prepare-run%) erfahren. Als Problemumgehung können Sie die problematischen Items in eine Dummy-LOOP stellen, also eine LOOP, die das Item einfach einmal aufruft.

## Unterstützte Browser

Die folgenden Kombinationen von Browser und Betriebssystemen wurden mit der neuesten Version von OSWeb getestet. Ältere Browserversionen, Betriebssysteme und Versionen von OSWeb könnten funktionieren, wurden jedoch nicht kürzlich getestet. Bestimmte Erweiterungen, wie Ad-Blocker oder Script-Blocker, können verhindern, dass OSWeb ausgeführt wird.

### Vollständig unterstützt

- Chrome >= 101 (Windows 11, Mac OS Monterey, Ubuntu 22.04, Android 12.0)
- Edge >= 101 (Windows 11, Mac OS Monterey)
- Firefox >= 99 (Windows 11, Mac OS Monterey, Ubuntu 22.04, Android 12.0)
- Opera >= 86 (Windows 11) 
- Chromium >= 101 (iOS 15.2)
- Firefox >= 99 (iOS 15.2)
- Opera >= 86 (Mac OS Monterey) 
- Safari >= 15 (iOS 15.2, Mac OS Monterey)

### Nicht unterstützt

- Internet Explorer >= 11 (Windows 10)


## OSWeb aktualisieren

OSWeb wird aktiv entwickelt. Wenn Sie sicherstellen möchten, dass Sie die neueste Version verwenden, können Sie die OSWeb-Erweiterung aktualisieren, die `opensesame-extension-osweb` genannt wird. Ab OpenSesame 3.3 können Sie dies tun, indem Sie den folgenden Befehl in der Konsole ausführen:

```bash
conda update opensesame-extension-osweb -c cogsci -c conda-forge -y
```

Oder:

```bash
pip install --pre opensesame-extension-osweb --upgrade
```

Siehe auch:

- <https://rapunzel.cogsci.nl/manual/environment/>


## Externe JavaScript-Pakete einbinden

Neu in OSWeb v1.4.6.1
{:.page-notification}

Sie können externe JavaScript-Pakete einbinden, indem Sie die URLs zu diesen Paketen (eine URL pro Zeile) in das Eingabefeld mit der Bezeichnung 'Externe JavaScript-Bibliotheken' eingeben. Diese Pakete werden dann mit `<script>`-Tags im Kopf des HTML eingefügt.

Zum Beispiel können Sie [WebGazer](%url:webgazer%) für den In-Browser-Einsatz einbinden, indem Sie den folgenden Link eingeben:

```
https://webgazer.cs.brown.edu/webgazer.js
```