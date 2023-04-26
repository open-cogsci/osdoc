<div class="ClassDoc YAMLDoc" markdown="1">

# Instanz __log__

Das `log`-Objekt ermöglicht das Protokollieren von Daten. Ein `log`-Objekt wird
automatisch erstellt, wenn das Experiment beginnt.

__Beispiel__

~~~ .python
# Eine Zeile Text schreiben
log.write('Meine benutzerdefinierte Log-Nachricht')
# Alle Variablen schreiben
log.write_vars()
~~~

[TOC]

## close(self)

Schließt das aktuelle Protokoll.



__Beispiel__

~~~ .python
log.close()
~~~



## open(path)

Öffnet das aktuelle Protokoll. Wenn bereits ein Protokoll geöffnet war, wird es automatisch geschlossen
und erneut geöffnet.


__Parameter__

- **path**: Der Pfad zur aktuellen Protokolldatei. In den meisten Fällen (sofern keine benutzerdefinierte
Protokoll-Back-End verwendet wird) wird dies ein Dateiname sein.

__Beispiel__

~~~ .python
# Ein neues Protokoll öffnen
log.open('/pfad/zum/neuen/protokollfile.csv')
~~~



## write(msg, newline=True)

Schreibt eine Nachricht in das Protokoll.


__Parameter__

- **msg**: Eine Textnachricht. Bei Verwendung von Python 2 sollte dies entweder
`unicode` oder ein utf-8-codiertes `str` sein. Bei Verwendung von Python 3 sollte dies entweder `str` oder ein utf-8-codiertes `bytes` sein.
- **newline**: Gibt an, ob nach der Nachricht ein Zeilenumbruch geschrieben werden soll.

__Beispiel__

~~~ .python
# Einen einzelnen Textstring schreiben
log.write(f'Zeit = {clock.time()}')
~~~



## write_vars(var_list=None)

Schreibt Variablen in das Protokoll.


__Parameter__

- **var_list**: Eine Liste von Variablennamen zum Schreiben oder None, um alle Variablen
zu schreiben, die im Experiment existieren.

__Beispiel__

~~~ .python
# Schreiben Sie alle Variablen in die Protokolldatei
log.write_vars()
~~~



</div>