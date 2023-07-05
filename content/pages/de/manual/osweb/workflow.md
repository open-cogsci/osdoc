title: Online-Experimente mit OSWeb durchführen
hash: f0cc1f57958c34a65409a874ee511e03fee4f8ee35bc0bef55d0af11ac74f56e
locale: de
language: German

[TOC]


## Der Arbeitsablauf

Für eine Einführung in den Arbeitsablauf, siehe auch:

Mathôt, S., & March, J. (2022). Durchführung sprachlicher Experimente online mit OpenSesame und OSWeb. *Sprachliches Lernen*. doi:10.1111/lang.12509
<br /><small>[Verwandtes Preprint (nicht identisch mit veröffentlichtem Manuskript)](https://doi.org/10.31234/osf.io/wnryc)</small>


### Entwicklung Ihres Experiments

Zuerst entwickeln Sie Ihr Experiment wie gewohnt mit der OpenSesame Desktop-Anwendung. Nicht alle Funktionen sind in Online-Experimenten verfügbar. Insbesondere können Sie keine Python INLINE_SCRIPT Elemente verwenden, sondern müssen stattdessen JavaScript INLINE_JAVASCRIPT Elemente verwenden. Während der Entwicklung Ihres Experiments ist es daher wichtig zu überprüfen, ob Ihr Experiment mit OSWeb kompatibel ist.

- %link:manual/osweb/osweb%
- %link:manual/javascript/about%


### Hochladen Ihres Experiments zu JATOS

Sobald Sie Ihr Experiment entwickelt haben, veröffentlichen Sie es in JATOS. JATOS ist ein Webserver, der Experimente verwaltet: Es ermöglicht Ihnen Links zu generieren, die Sie an die Teilnehmer verteilen können, und speichert Daten, die gesammelt wurden.

Es gibt nicht einen einzigen JATOS-Server. Vielmehr unterhalten viele Institutionen ihren eigenen JATOS-Server. Darüber hinaus ist <https://mindprobe.eu> ein kostenloser JATOS-Server, gesponsert von ESCoP und OpenSesame.

- %link:jatos%


### Datenerhebung

Sobald Sie Ihr Experiment auf JATOS veröffentlicht haben, können Sie mit der Datenerhebung beginnen. Sie können dies tun, indem Sie manuell Links an die Teilnehmer senden, zum Beispiel per E-Mail. Oder Sie können eine Plattform zur Teilnehmerrekrutierung nutzen, wie Prolific, Mechanical Turk oder Sona Systems.

- %link:prolific%
- %link:mturk%
- %link:sonasystems%


### Datenanalyse

Sobald die Datenerhebung abgeschlossen ist, können Sie die Daten von JATOS herunterladen und sie für weitere Analysen in `.xlsx` oder `.csv` Format konvertieren:

- %link:manual/osweb/data%


## Anleitungen

- %link:tutorials/intermediate-javascript%
- %link:wcst%