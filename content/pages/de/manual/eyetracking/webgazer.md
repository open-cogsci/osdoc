title: WebGazer.js
hash: 47ee55649881bcf2ff92c750daeac0bdea5feb3a8719e0e99c5309e49686ecc6
locale: de
language: German

Erfordert OSWeb v1.4.6.1
{:.page-notification}

[TOC]


## Über WebGazer

WebGazer.js ist eine in JavaScript geschriebene Eye-Tracking-Bibliothek. Sie können es in OSWeb einbinden, um Eye-Tracking in Online-Experimenten durchzuführen.

- <https://webgazer.cs.brown.edu/>


## Einbindung von WebGazer.js in das Experiment

WebGazer.js ist standardmäßig nicht in OSWeb enthalten. Sie können es jedoch als externe Bibliothek einbinden, indem Sie einen Link zu `webgazer.js` unter Externe JavaScript-Bibliotheken eingeben. Derzeit ist ein funktionaler Link:

```
https://webgazer.cs.brown.edu/webgazer.js
```

Siehe auch:

- %link:manual/osweb/osweb%


## Beispiel-Experiment

Unten können Sie ein Beispiel-Experiment herunterladen, das WebGazer.js verwendet. Den Teilnehmern wird zunächst gebeten, auf eine Gruppe von Punkten zu klicken und sie anzuschauen; dadurch führt WebGazer.js automatisch etwas Ähnliches wie ein Kalibrierungsverfahren durch. Anschließend zeigt das Experiment einen einfachen Bildschirm, um die Genauigkeit der Blickpositionserfassung zu testen. Im Allgemeinen ist ein feinkörniges Eye-Tracking nicht möglich, aber Sie können erkennen, in welchem Quadranten des Bildschirms ein Teilnehmer gerade schaut. Um dieses Experiment auszuführen, müssen Sie WebGazer.js in das Experiment einbinden, wie oben beschrieben.

- %static:attachments/webgazer.osexp%

Sie können das Experiment auch direkt im Browser starten:

- <https://jatos.mindprobe.eu/publix/BowSAFY2VWl>