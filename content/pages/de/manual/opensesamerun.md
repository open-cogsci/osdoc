title: OpenSesameRun (keine GUI)
hash: 435d6b0358c5bdd011dbe66206d56d78258410aadf1b385e46d7c8fedd2aecb2
locale: de
language: German

## Über

`opensesamerun` ist ein einfaches Werkzeug, mit dem Sie OpenSesame-Experimente mit einer minimalen GUI oder direkt ausführen können, indem Sie alle erforderlichen Optionen über die Befehlszeile angeben. Eine minimale GUI wird automatisch angezeigt, wenn nicht alle Befehlszeilenoptionen angegeben wurden, insbesondere die Experimentdatei, die Versuchspersonennummer und die Protokolldatei.

~~~
Verwendung: opensesamerun [Experiment] [Optionen]

Optionen:
  --version             Programmversionsnummer anzeigen und beenden
  -h, --help            Zeigen Sie diese Hilfe-Nachricht an und beenden Sie

  Versuchspersonen- und Protokolldatei-Optionen:
    -s SUBJECT, --subject=SUBJECT
                        Versuchspersonennummer
    -l LOGFILE, --logfile=LOGFILE
                        Protokolldatei

  Anzeigeoptionen:
    -f, --fullscreen    Vollbildmodus ausführen
    -c, --custom_resolution
                        Verwenden Sie nicht die in der Experimentdatei angegebene Bildschirmauflösung
    -w WIDTH, --width=WIDTH
                        Bildschirmbreite
    -e HEIGHT, --height=HEIGHT
                        Bildschirmhöhe

  Sonstige Optionen:
    -d, --debug         Drucken Sie viele Debug-Meldungen auf die Standardausgabe
    --stack             Stack-Informationen drucken

  Sonstige Optionen:
    --pylink            Laden Sie PyLink vor PyGame (notwendig für die Verwendung der Eyelink-Plug-ins im Nicht-Dummy-Modus)
~~~

## Beispiel

Angenommen, Sie möchten das Gaze-Cuing-Beispiel-Experiment für Versuchsperson #1 ausführen und die Protokolldatei in Ihrem Dokumente-Ordner speichern (dieses Beispiel geht von Linux aus, funktioniert aber analog auf anderen Plattformen):

~~~
opensesamerun /usr/share/opensesame/examples/gaze_cuing.opensesame.tar.gz -s 1 -l /home/sebastiaan/Documents/Proband1.tsv -f 
~~~

## Alternative `libopensesame`

Sie können Experimente auch ohne die GUI über das `libopensesame`-Python-Modul starten:

- %link:Bedienungsanleitung/python/nogui%