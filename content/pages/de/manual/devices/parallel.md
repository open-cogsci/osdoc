title: Parallelport (EEG-Trigger)
reviewed: false
hash: 173d67c1a3fbe4fb17b8a936fe30584d71443f518bf86bd65c9ad6da21c4e229
locale: de
language: German

In EEG/ ERP-Studien ist es üblich, Trigger zu senden, um den Zeitstempel für bedeutende Ereignisse zu markieren (z. B. den Beginn eines Versuchs, die Darstellung eines bestimmten Stimulus usw.). Trigger sind in der Regel Bytes, die über den Parallelport an das EEG-Gerät gesendet werden.

[TOC]


## Verwendung des `parallel_port_trigger` Plugins

Parallel_port_trigger ist ein Plugin von Drittanbietern und wird nicht vom OpenSesame-Team gepflegt.
{: .page-notification}

Ein OpenSesame-Plugin zum Senden von Stimulussynchronisationstriggern über den Parallelport an Datenerfassungssysteme.

- <https://github.com/dev-jam/opensesame-plugin-parallel_port_trigger/>

Sie können das `parallel_port_trigger` Plugin von PyPi installieren:

```
pip install pip install opensesame-plugin-parallel-port-trigger
```


## Verwendung von `dportio.dll` in einem Python Inline-Skript (nur Windows)

Anstelle des `parallel_port_trigger` Plugins ist es auch möglich, Trigger mit `dlportio.dll` über ein Python Inline-Skript zu senden. Dieser Ansatz ist auf Windows beschränkt. Fügen Sie dazu zunächst ein INLINE_SCRIPT am Anfang des Experiments mit dem folgenden Code in der Vorbereitungsphase hinzu:

~~~ .python
try:
	from ctypes import windll
	global io
	io = windll.dlportio # erfordert dlportio.dll !!!
except:
	print('Der Parallelport konnte nicht geöffnet werden')
~~~

Dies lädt `dlportio.dll` als globales Objekt namens `io`. Bitte beachten Sie, dass ein Fehler das Experiment nicht zum Absturz bringt, überprüfen Sie also das Debug-Fenster auf Fehlermeldungen!

Verwenden Sie jetzt den folgenden Code in einem INLINE_SCRIPT irgendwo im Experiment, um einen Trigger zu senden:

~~~ .python
global io
trigger = 1
port = 0x378
try:
	io.DlPortWritePortUchar(port, trigger)
except:
	print('Es wurde versucht, einen Trigger zu senden!')
~~~

Beachten Sie, dass dies den Trigger 1 an Port 0x378 (=888) sendet. Ändern Sie diese Werte je nach Ihrer Einrichtung.

## Zugriff auf den Parallelport erhalten

### Linux

Unter Linux verwenden wir das `parport_pc` Modul (getestet in Debian Wheezy) und müssen uns Berechtigungen dafür geben. Dies kann durch Ausführen der folgenden Befehle erreicht werden:

	sudo rmmod lp
	sudo rmmod parport_pc
	sudo modprobe parport_pc
	sudo adduser [user] lp

Hier sollte `[user]` durch Ihren Benutzernamen ersetzt werden. Danach loggen Sie sich aus und wieder ein, und Sie können loslegen!

### Windows XP und Windows Vista (32 Bit)

1. Laden Sie den 32-Bit DLPortIO Treiber von [hier][win32-dll] herunter und entpacken Sie das Zip-Archiv.
2. Gehen Sie zum `DriverLINX/drivers` Ordner und kopieren Sie `dlportio.dll` und `dlportio.sys` in den `install` Ordner. Dies ist der Ordner, in dem `install.exe` liegt. Führen Sie dann `install.exe` aus.
3. Sie müssen `dlportio.dll` in den OpenSesame Ordner kopieren (d.h., den gleichen Ordner, der `opensesame.exe` enthält).

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