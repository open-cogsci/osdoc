title: Dinge in Reihenfolge tun
hash: 15313148d00600657d102430c4e197e7a888d543ca35e349a350210120cb1e11
locale: de
language: German

Das SEQUENCE-Element hat zwei wichtige Funktionen:

- Es führt mehrere andere Elemente nacheinander aus.
- Es bestimmt, welche Elemente ausgeführt werden sollen und welche nicht.

SEQUENCEs werden von oben nach unten ausgeführt; das heißt, das Element oben wird zuerst ausgeführt. Die Reihenfolge einer SEQUENCE ist immer sequenziell.

## Run-if-Ausdrücke

Sie können Run-if-Ausdrücke verwenden, um zu bestimmen, ob ein bestimmtes Element ausgeführt werden soll oder nicht. Wenn Sie zum Beispiel möchten, dass eine Anzeige nur dann präsentiert wird, wenn ein Teilnehmer eine falsche Antwort gegeben hat, können Sie die Run-if-Ausdrücke für dieses Element auf folgendes setzen:

```python
{correct} == 0
```

Wenn Sie die Run-if-Ausdrücke leer lassen oder `True` eingeben, wird das Element immer ausgeführt. Run-if-Ausdrücke verwenden die gleiche Syntax wie andere bedingte Ausdrücke. Weitere Informationen finden Sie unter:

- %link:manual/variables%

Run-if-Ausdrücke beeinflussen nur, welche Elemente ausgeführt werden, nicht welche Elemente vorbereitet werden. Anders ausgedrückt wird die Prepare-Phase aller Elemente in einer SEQUENCE immer ausgeführt, unabhängig von den Run-if-Ausdrücken. Siehe auch:

- %link:prepare-run%


## Elemente deaktivieren

Um ein Element in einer SEQUENCE vollständig zu deaktivieren, klicken Sie mit der rechten Maustaste darauf und wählen Sie 'Disable'. Dies ist hauptsächlich während der Entwicklung Ihres Experiments nützlich, um zum Beispiel vorübergehend die Anweisungen zu umgehen.