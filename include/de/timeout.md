## Zeitüberschreitung

Das Feld *Timeout* gibt einen Timeout-Wert in Millisekunden an oder "unendlich" für keine Zeitüberschreitung. Wenn eine Zeitüberschreitung auftritt, geschieht Folgendes:

- `response_time` wird auf den Timeout-Wert gesetzt, oder eher auf die Zeit, die benötigt wird, um eine Zeitüberschreitung zu registrieren, die möglicherweise leicht von dem Timeout-Wert abweicht.
- `response` wird auf 'None' gesetzt. Das bedeutet, dass Sie 'None' als richtige Antwort angeben können, wenn eine Zeitüberschreitung eintreten soll; dies kann zum Beispiel in einer Go-/No-Go-Aufgabe nützlich sein, wenn der Teilnehmer bei No-Go-Versuchen keine Antwort geben soll.