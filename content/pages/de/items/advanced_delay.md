title: Advanced_delay
hash: 54879490fe7472c89ac95be6dc21911ffcdddabbe58ec3de0baf4b660ad5dc89
locale: de
language: German

Das `advanced_delay` Plug-in verzögert das Experiment um eine vorgegebene durchschnittliche Dauer plus eine zufällige Schwankung.

- *Duration* ist die durchschnittliche Dauer der Verzögerung in Millisekunden.
- *Jitter* ist die Größe der Schwankung in der Verzögerung in Millisekunden.
- *Jitter mode* bestimmt, wie die Schwankung definiert ist:
  - *Standard deviation* zieht Werte aus einer Gaußschen Verteilung, wobei Jitter die Standardabweichung ist.
  - *Uniform* zieht Werte aus einer Gleichverteilung, zentriert auf Duration, wobei Jitter die Breite ist.