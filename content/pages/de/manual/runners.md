title: Läufer
hash: 06242415e6cca1b1434321f7ba96e925abe4ccd2fd31cac48ab7ff6b64f73876
locale: de
language: German

[TOC]

## Über Runner

Es gibt mehrere technisch unterschiedliche Möglichkeiten, wie Sie Ihr Experiment ausführen können. Jede dieser Möglichkeiten entspricht einem *Runner*. Sie können einen Runner unter Menü → Extras → Einstellungen → Runner auswählen.

Sofern Sie keinen Grund haben, dies nicht zu tun, sollten Sie den *Multiprozess*-Runner verwenden. Wenn OpenSesame jedoch manchmal abstürzt, können Sie ausprobieren, ob die Auswahl eines anderen Runners dies behebt.

## Verfügbare Runner

### Multiprozess

Der *Multiprozess*-Runner führt Ihr Experiment in einem anderen Prozess aus. Der Vorteil dieses Ansatzes besteht darin, dass Ihr Experiment abstürzen kann, ohne dass dabei die Benutzeroberfläche abstürzt. Ein weiterer Vorteil des *Multiprozess*-Runners besteht darin, dass der Variableninspektor Ihre experimentellen Variablen während des Laufs des Experiments anzeigen kann.

### Im Prozess

Der *im Prozess* Runner führt das Experiment im gleichen Prozess wie die Benutzeroberfläche aus. Der Vorteil dieses Ansatzes besteht in seiner Einfachheit. Nachteil ist, dass die Benutzeroberfläche abstürzen kann, wenn das Experiment abstürzt, und umgekehrt.

### Extern

Der *externe* Runner führt das Experiment aus, indem opensesamerun als separate Anwendung gestartet wird. Der Vorteil dieses Ansatzes besteht darin, dass das Experiment abstürzen kann, ohne dass die Benutzeroberfläche damit heruntergefahren wird.