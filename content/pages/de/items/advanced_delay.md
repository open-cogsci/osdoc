title: Advanced_delay
hash: 05d5215072bc5c76e2fd177cc099d6281a44d87cde42c43e79a945b2ac83b98f
locale: de
language: German

Das `advanced_delay` Plug-in verzögert das Experiment um eine vorab festgelegte durchschnittliche Dauer plus einen zufälligen Spielraum.

- *Dauer* ist die durchschnittliche Dauer der Verzögerung in Millisekunden.
- *Schwankungsbreite* ist die Größe der Variation in der Verzögerung in Millisekunden.
- *Schwankungsmodus* ist die Art und Weise, wie die Schwankungsbreite berechnet wird:
	- *Standardabweichung* zieht die Variation aus einer Gaußschen Verteilung mit der Schwankungsbreite als Standardabweichung.
	- *Gleichmäßig* zieht die Variation in der Dauer aus einer gleichmäßigen Verteilung.