title: Parallelport (EEG-Trigger)
reviewed: false
hash: 587cf8f063e30d745e5bef81527ea94d14a49a67069a670b5d61e369af1c09ff
locale: de
language: German

In EEG/ ERP-Studien ist es üblich, Trigger zu senden, um den Zeitstempel für bedeutende Ereignisse zu markieren (z.B. Beginn eines Versuchs, Präsentation eines bestimmten Reizes usw.). Trigger sind typischerweise Bytes, die über den Parallelport an das EEG-Gerät gesendet werden.

[TOC]

## Verwendung des `parallel_port_trigger` Plugins

Parallel_port_trigger ist ein Plugin eines Drittanbieters, wurde jedoch vom OpenSesame-Team überprüft.
{: .page-notification}

Trigger können mit dem `parallel_port_trigger` Plugin gesendet werden, das unter Linux und Windows funktioniert.

Das Plugin hat drei Eingabefelder:

- Der Wert liegt zwischen 0-255 und gibt das Trigger-Byte an.
- Die Dauer (in ms) ist die Zeit, in der der Trigger aktiv ist. Falls keine 0 ms Dauer angegeben wurde, wird der Trigger nach diesem Intervall auf 0 zurückgesetzt.
- Die Port-Adresse muss manuell angegeben werden. Diese Einstellung gilt nur für Windows und wird unter Linux ignoriert.

Das Plugin kann hier heruntergeladen werden:

- <https://github.com/dev-jam/opensesame_plugin_parallel-port-trigger>

%--
figure:
 id: FigScreenshot
 source: plugin-screenshot.png
 caption: |
  Ein Screenshot des `parallel_port_trigger` Plugins.
--%

## Verwendung von `dportio.dll` in einem Python Inline-Skript (nur Windows)

Anstelle des `parallel_port_trigger` Plugins können Trigger auch mit `dlportio.dll` über ein Python Inline-Skript gesendet werden. Dieser Ansatz funktioniert nur unter Windows. Fügen Sie dazu zuerst einen INLINE_SCRIPT zu Beginn des Experiments mit folgendem Code in der Vorbereitungsphase hinzu:

~~~ .python
try:
	from ctypes import windll
	global io
	io = windll.dlportio # requires dlportio.dll !!!
except:
	print('The parallel port couldn\'t be opened')
~~~

Dies wird `dlportio.dll` als globales Objekt namens `io` laden. Beachten Sie, dass Fehler das Experiment nicht zum Absturz bringen, also überprüfen Sie das Debug-Fenster für Fehlermeldungen!

Verwenden Sie dann den folgenden Code in einem INLINE_SCRIPT irgendwo im Experiment, um einen Trigger zu senden:

~~~ .python
global io
trigger = 1
port = 0x378
try:
	io.DlPortWritePortUchar(port, trigger)
except:
	print('Failed to send trigger!')
~~~

Beachten Sie, dass dies Trigger 1 an Port 0x378 (=888) sendet. Ändern Sie diese Werte entsprechend Ihrer Konfiguration.

## Zugang zum Parallelport erhalten

### Linux

Unter Linux verwenden wir das `parport_pc`-Modul (getestet in Debian Wheezy) und müssen uns selbst die Berechtigung dazu geben. Dies kann erreicht werden, indem die folgenden Befehle ausgeführt werden:

	sudo rmmod lp
	sudo rmmod parport_pc
	sudo modprobe parport_pc
	sudo adduser [user] lp

Hier sollte `[user]` durch Ihren Benutzernamen ersetzt werden. Anschließend melden Sie sich ab und wieder an, und Sie sind einsatzbereit!

### Windows XP und Windows Vista (32 Bit)

1. Laden Sie den 32-Bit DLPortIO-Treiber von [hier][win32-dll] herunter und entpacken Sie das ZIP-Archiv.
2. Gehen Sie zum `DriverLINX/drivers` Ordner und kopieren Sie `dlportio.dll` und `dlportio.sys` in den `install` Ordner. Dies ist der Ordner, in dem sich `install.exe` befindet. Führen Sie anschließend `install.exe` aus.
3. Sie müssen `dlportio.dll` in den OpenSesame-Ordner kopieren (also in denselben Ordner, der `opensesame.exe` enthält).

### Windows 7 (32 und 64 Bit)

1. Laden Sie den 32-Bit- oder 64-Bit-DLPortIO-Treiber [hier][win7-dll] herunter und entpacken Sie das ZIP-Archiv.
2. Da Windows 7 ein verstärktes Sicherheitssystem hat (zumindest im Vergleich zu XP), kann man den DLPortIO-Treiber nicht einfach installieren. Dies funktioniert nicht, da Windows 7 alle Versuche, einen nicht offiziell signierten (von Microsoft) Treiber zu installieren, blockieren wird. Gut für die Sicherheit eines durchschnittlichen Benutzers - schlecht für uns. Um diese Einschränkung zu umgehen, muss man ein kleines Hilfsprogramm namens "Digital Signature Enforcement Overrider" (DSEO) verwenden, das [hier][dseo] heruntergeladen werden kann (es gibt natürlich auch andere mögliche Wege, dies zu tun, aber dieses Programm wird in der DLPortIO-`readme.txt` erwähnt und man muss sich nicht tiefer in die Spezialitäten der MS Windows 7-Architektur einarbeiten).
3. Starten Sie DSEO mit Administratorrechten (Rechtsklick auf `dseo13b.exe`, "Als Administrator ausführen" wählen). Nun erscheint das DSEO-Fenster. Es zeigt lediglich eine Liste von Optionen, welche Aktion als nächstes ausgeführt werden soll.
4. Wählen Sie die Option "Treiber-/sys-Datei signieren" und drücken Sie "OK". Jetzt erscheint ein weiteres Fenster, in dem Sie den absoluten Pfad zur Datei `DLPortIO.sys` eingeben müssen (nur diese, nicht die DLL!). Denken Sie daran, Leerzeichen im Pfad zu escapen, wenn Sie welche haben (fragen Sie nicht, wie lange das bei mir dauerte), sonst werden Ihre Dateien nicht gefunden. Wenn Sie auf "OK" drücken, wird die sys-Datei signiert.
5. Wählen Sie im DSEO-Listenfenster "Testmodus aktivieren" und drücken Sie "OK". Wählen Sie dann "Beenden" und starten Sie Ihren PC neu. Windows 7 beschwert sich fälschlicherweise, dass DSEO möglicherweise nicht korrekt installiert ist - klicken Sie einfach auf "Ja, die Software ist korrekt installiert".
6. Nach Abschluss des Hochfahrens sehen Sie, dass so etwas wie "Windows 7 Testmodus Build #Nummer#" auf dem Desktop direkt über der Uhr in der Starterleiste geschrieben steht. Das ist notwendig. Sie müssen im Testmodus sein, um diesen inoffiziell signierten Treiber auszuführen.
7. Führen Sie nun `DLPortIO_install.bat` mit Administratorrechten aus (im Windows Explorer, Rechtsklick auf die Datei, ...). Antworten Sie "Ja", wenn Windows Sie vor Registrierungsänderungen warnt.
8. Starten Sie Ihren PC neu.
9. Kopieren Sie `DLPortIO.dll` in den OpenSesame-Ordner, also den gleichen Ordner, der die Datei `opensesame.exe` enthält.

Quelle: [Forum Beitrag von Absurd][post-3]

## Empfehlungen

- Starten Sie Ihr Experiment mit einem "Null"-Trigger, um sicherzustellen, dass alle Pins auf Null gesetzt sind.
- Es wird empfohlen, die [psycho] oder [xpyriment] Backends anstelle des [legacy] Backends (unter Verwendung von PyGame) für zeitkritische Experimente zu verwenden. Dies liegt daran, dass [psycho] und [xpyriment] die Bildwiederholrate des Monitors bei der Rückgabe von Zeitstempeln berücksichtigen, während [legacy] dies nicht tut. Weitere Informationen finden Sie unter [miscellaneous/timing].
- Senden Sie den Trigger-Code direkt nach (anstatt kurz vor) der Präsentation Ihres Stimulus (unter der Annahme, dass Sie den Beginn des Stimulus markieren möchten). Dadurch stellen Sie sicher, dass der Zeitstempel so genau wie möglich ist und nicht unter einer kleinen zufälligen Schwankung aufgrund der Bildwiederholrate Ihres Monitors leidet. [Quelle: lvanderlinden][post-2]

## Fehlerbehebung

Es gibt eine Reihe relevanter Forenthemen, in denen triggerbezogene Probleme diskutiert (und für die meisten, gelöst!) werden.

- Ein Beitrag über Geistertrigger, d. h. unerwünschte Trigger, die auf mysteriöse Weise von der EEG-Apparatur registriert werden: [link][post-2]
- Ein Beitrag mit ausführlichen Installationsanleitungen für DLPortIO unter Windows 7 ([Quelle: absurd][post-3]).

Zögern Sie bitte nicht, Fragen im Forum zu stellen oder uns von Ihren Erfahrungen (gut oder schlecht) zu berichten.

[win32-dll]: http://files.cogsci.nl/misc/dlportio.zip
[win7-dll]: http://real.kiev.ua/avreal/download/#DLPORTIO_TABLE
[dseo]: http://www.ngohq.com/home.php?page=dseo
[post-2]: http://forum.cogsci.nl/index.php?p=/discussion/comment/780#Comment_780
[post-3]: http://forum.cogsci.nl/index.php?p=/discussion/comment/745#Comment_745
[miscellaneous/timing]: /miscellaneous/timing
[legacy]: /backends/legacy
[xpyriment]: /backends/xpyriment
[psycho]: /backends/psycho