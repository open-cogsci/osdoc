title: Tastaturantworten
hash: 23ed6413bd7bc9180b1e3a384c25c3f89c817414a4460a00260be06f5698474a
locale: de
language: German

Tastaturantworten werden mit dem KEYBOARD_RESPONSE-Element erfasst.

[TOC]


## Antwortvariablen

Das KEYBOARD_RESPONSE setzt die Standardantwortvariablen, wie hier beschrieben:

- %link:manual/variables%

## Tastennamen

Tasten werden in der Regel durch ihre Zeichen und/ oder ihre Beschreibung identifiziert (je nachdem, was zutrifft). Zum Beispiel:

- Die `/`-Taste heißt 'slash' und '/'. Sie können eine der beiden Bezeichnungen verwenden.
- Die `a`-Taste heißt 'a'.
- Die linke Pfeiltaste heißt 'left'.

Wenn Sie nicht wissen, wie eine bestimmte Taste heißt, können Sie:

- Klicken Sie auf die Schaltfläche "Verfügbare Tasten auflisten"; oder
- Erstellen Sie ein einfaches Experiment, in dem ein KEYBOARD_RESPONSE sofort von einem FEEDBACK-Element mit dem Text '{response}' gefolgt wird. Dies zeigt den Namen der zuvor erfassten Antwort.


## Richtige Antwort

Das Feld *Richtige Antwort* gibt an, welche Antwort als richtig angesehen wird. Nach einer richtigen Antwort wird die Variable `correct` automatisch auf 1 gesetzt; nach einer falschen Antwort (d. h. allem anderen) wird `correct` auf 0 gesetzt; wenn keine richtige Antwort angegeben ist, wird `correct` auf 'undefiniert' gesetzt.

Sie können die richtige Antwort auf drei Hauptarten angeben:

- *Lassen Sie das Feld leer.* Wenn Sie das Feld *Richtige Antwort* leer lassen, überprüft OpenSesame automatisch, ob eine Variable namens `correct_response` definiert wurde und verwendet diese Variable für die richtige Antwort, falls vorhanden.
- *Geben Sie einen festen Wert ein.* Sie können explizit z. B. 'left' für einen KEYBOARD_RESPONSE-Artikel eingeben. Dies ist nur sinnvoll, wenn die richtige Antwort festgelegt ist.
- *Geben Sie einen Variablennamen ein.* Sie können eine Variable eingeben, z. B. '{cr}'. In diesem Fall wird diese Variable für die richtige Antwort verwendet.


## Erlaubte Antworten

Das Feld *Erlaubte Antworten* zeigt eine Liste der erlaubten Antworten an. Alle anderen Antworten werden ignoriert, mit Ausnahme von 'Escape', das das Experiment pausiert. Die erlaubten Antworten sollten eine durch Semikolon getrennte Liste von Antworten sein, wie 'a;left;/' für ein KEYBOARD_RESPONSE. Um alle Antworten zu akzeptieren, lassen Sie das Feld *Erlaubte Antworten* leer.


%--include: include/timeout.md--%

## Tastaturantworten in Python erfassen

Sie können das `keyboard`-Objekt verwenden, um Tastaturantworten in Python zu erfassen:

- %link:manual/python/keyboard%