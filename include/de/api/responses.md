<div class="ClassDoc YAMLDoc" markdown="1">

# Instanz __responses__

Das `responses` Objekt enthält die Historie der Antworten, die während des Experiments gesammelt wurden.

Ein `responses` Objekt wird automatisch erstellt, wenn das Experiment startet.

Zusätzlich zu den unten aufgeführten Funktionen werden die folgenden Semantiken unterstützt:

__Beispiel__

~~~ .python
# Durchlaufe alle Antworten, wobei zuletzt gegebene Antworten zuerst kommen
# Jede Antwort hat korrekte, Antwort, Antwortzeit, Artikel- und Feedback-
# Attribute.
for response in responses:
    print(response.correct)
# Die beiden letzten gegebenen Antworten ausgeben
print('letzte_zwei Antworten:')
print(responses[:2])
~~~

[TOC]

## add(response=None, correct=None, response_time=None, item=None, feedback=True)

Fügt eine Antwort hinzu.


__Parameter__

- **response**: Der Antwortwert, zum Beispiel 'space' für die Leertaste, 0 für Joystick-Taste 0 usw.
- **correct**: Die Richtigkeit der Antwort.
- **response_time**: Die Antwortzeit.
- **item**: Der Artikel, der die Antwort erfasst hat.
- **feedback**: Gibt an, ob die Antwort in Feedback zur Genauigkeit und durchschnittlichen Antwortzeit enthalten sein soll.

__Beispiel__

~~~ .python
responses.add(response_time=500, correct=1, response='left')
~~~



## clear(self)

Löscht alle Antworten.



__Beispiel__

~~~ .python
responses.clear()
~~~



## reset_feedback(self)

Setzt den Feedback-Status aller Antworten auf False, sodass nur
neue Antworten im Feedback enthalten sein werden.



__Beispiel__

~~~ .python
responses.reset_feedback()
~~~



</div>