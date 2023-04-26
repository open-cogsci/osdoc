title: Online-Experimente mit OSWeb durchführen
hash: d164c11575309f8213f7683999953e7c4d0eb5adf6c728cb34d716947a673fbf
locale: de
language: German

[TOC]

## Der Arbeitsablauf

Für eine Einführung in den Arbeitsablauf siehe auch:

Mathôt, S. & March, J. (2022). Durchführung sprachlicher Experimente online mit OpenSesame und OSWeb. *Language Learning*. doi:10.1111/lang.12509
<br /><small>[Verwandter Preprint (nicht identisch mit veröffentlichtem Manuskript)](https://doi.org/10.31234/osf.io/wnryc)</small>

### Entwicklung Ihres Experiments

Zuerst entwickeln Sie Ihr Experiment wie gewohnt mit der OpenSesame-Desktop-Anwendung. Nicht alle Funktionen sind in Online-Experimenten verfügbar. Insbesondere können Sie keine Python INLINE_SCRIPT-Elemente verwenden, sondern müssen stattdessen JavaScript INLINE_JAVASCRIPT-Elemente verwenden. Während der Entwicklung Ihres Experiments ist es daher wichtig zu überprüfen, ob Ihr Experiment mit OSWeb kompatibel ist.

- %link:manual/osweb/osweb%
- %link:manual/javascript/about%
- %link:manual/osweb/questionnaires%

### Hochladen Ihres Experiments auf JATOS

Nachdem Sie Ihr Experiment entwickelt haben, exportieren Sie es aus OpenSesame und laden es auf JATOS hoch. JATOS ist ein Webserver, der Experimente verwaltet: Er ermöglicht die Erstellung von Links, die Sie an Teilnehmer verteilen können, und speichert die gesammelten Daten.

Es gibt nicht einen einzigen JATOS-Server. Vielmehr unterhalten viele Institutionen ihren eigenen JATOS-Server. Darüber hinaus ist <https://mindprobe.eu> ein kostenloser JATOS-Server, unterstützt von ESCoP und OpenSesame.

-%link:jatos%

### Datenerfassung

Sobald Sie Ihr Experiment auf JATOS hochgeladen haben, können Sie mit der Datenerfassung beginnen. Dies können Sie tun, indem Sie manuell Links an Teilnehmer senden, beispielsweise per E-Mail. Oder Sie können eine Plattform zur Teilnehmerrekrutierung verwenden, wie zum Beispiel Prolific, Mechanical Turk oder Sona Systems.

- %link:prolific%
- %link:mturk%
- %link:sonasystems%

## Tutorials

- %link:tutorials/intermediate-javascript%
- %link:wcst%