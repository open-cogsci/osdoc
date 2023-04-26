title: Zeitsteuerung
reviewed: false
hash: 220d36e32fac1e6b240a9d60c9d1a9e560276d629ba1cf584425ef078b5c3c85
locale: de
language: German

Diese Seite beschreibt verschiedene Probleme im Zusammenhang mit der Zeitsteuerung und bietet Benchmark-Ergebnisse sowie Tipps zum Testen Ihres eigenen Systems. Wenn Sie Probleme mit der Zeitsteuerung feststellen, nehmen Sie sich bitte die Zeit, diese Seite zu lesen. Viele Probleme werden durch Berücksichtigung von Aspekten wie der Stimulusvorbereitung und den Eigenschaften Ihres Monitors behoben.

[TOC]

## Ist OpenSesame in der Lage, Timing in Millisekunden-Präzision durchzuführen?

Die kurze Antwort ist: ja. Die lange Antwort ist der Rest dieser Seite.


## Wichtige Überlegungen für zeitkritische Experimente

### Überprüfen Sie Ihr Timing!

OpenSesame ermöglicht es Ihnen, die Zeitsteuerung Ihres Experiments sehr genau zu kontrollieren. Das garantiert jedoch nicht in jedem spezifischen Experiment eine genaue Zeitsteuerung! Aus verschiedenen Gründen, von denen viele auf dieser Seite beschrieben sind, können Sie Probleme mit der Zeitsteuerung haben. Daher sollten Sie in zeitkritischen Experimenten immer überprüfen, ob das Timing in Ihrem Experiment wie vorgesehen ist. Der einfachste Weg, dies zu tun, besteht darin, die von OpenSesame gemeldeten Bildschirmtimestamps zu überprüfen.

Jedes SKETCHPAD-Element hat eine Variable namens `time_[sketchpad name]`, die den Zeitstempel des letzten Moments enthält, in dem das SKETCHPAD angezeigt wurde. Wenn Sie also möchten, dass das SKETCHPAD *Ziel* (engl. "target") für 100 ms angezeigt wird, gefolgt von dem SKETCHPAD *Maske* (engl. "mask"), sollten Sie überprüfen, ob `time_mask` - `time_target` tatsächlich 100 ist. Bei Verwendung von Python-Inline-Code können Sie die Tatsache nutzen, dass `canvas.show()` den Bildschirmtimestamp zurückgibt.


### Ihren Monitor verstehen

Computermonitore aktualisieren sich periodisch. Wenn beispielsweise die Aktualisierungsrate Ihres Monitors 100 Hz beträgt, wird das Display alle 10 ms (1000 ms / 100 Hz) aktualisiert. Das bedeutet, dass ein visueller Reiz immer für eine Dauer präsentiert wird, die ein Vielfaches von 10 ms ist und Sie können einen Reiz nicht für z.B. 5 oder 37 ms darstellen. Die häufigste Aktualisierungsrate beträgt 60 Hz (= 16,67 ms Aktualisierungszyklus), obwohl Monitore mit wesentlich höheren Aktualisierungsraten manchmal für Experimentalsysteme verwendet werden.

In %VidRefresh können Sie sehen, wie ein Monitorupdate in Zeitlupe aussieht. Bei CRT-Monitoren (d. h. nicht-Flachbildschirm, Mitte) ist das Update ein einzelner Pixel, der sich von links nach rechts und von oben nach unten über den Monitor bewegt. Daher wird nur ein Pixel gleichzeitig beleuchtet, weshalb CRT-Monitore leicht flackern. Bei LCD- oder TFT-Monitoren (Flachbildschirm, links und rechts) erfolgt die Aktualisierung als "Flood Fill" von oben nach unten. Daher flackern LCD- und TFT-Monitore nicht. (Es sei denn, Sie präsentieren einen flackernden Reiz, natürlich.)

%--
video:
 id: VidRefresh
 source: vimeo
 videoid: 24216910
 width: 640
 height: 240
 caption: Ein Zeitlupenvideo des Aktualisierungszyklus auf CRT (Mitte) und LCD/ TFT-Monitoren. Video mit freundlicher Genehmigung von Jarik den Hartog und dem technischen Support der VU University Amsterdam.
--%

Wenn ein neues Stimulus-Display präsentiert wird, während der Aktualisierungszyklus zur Hälfte durchlaufen ist, wird ein "Tearing" beobachtet. Das bedeutet, dass die obere Hälfte des Monitors das alte Display zeigt, während die untere Hälfte das neue Display zeigt. Dies wird im Allgemeinen als unerwünscht angesehen, und daher sollte ein neues Display genau in dem Moment präsentiert werden, in dem der Aktualisierungszyklus von oben beginnt. Dies wird als "Synchronisation mit der vertikalen Aktualisierung" oder einfach "V-Sync" bezeichnet. Wenn V-Sync aktiviert ist, ist Tearing nicht mehr sichtbar, da der Riss mit dem oberen Rand des Monitors zusammenfällt. V-Sync ändert jedoch nichts an der Tatsache, dass ein Monitor nicht sofort aktualisiert wird und daher immer für einige Zeit sowohl das alte als auch das neue Display zeigt.

Ein weiteres wichtiges Konzept ist das des "Blockierens beim vertikalen Retrace" oder des "blockierenden Flip". Normalerweise, wenn Sie einen Befehl senden, um eine neue Anzeige anzuzeigen, wird der Computer diesen Befehl sofort akzeptieren und die anzuzeigende Anzeige in eine Warteschlange stellen. Die Anzeige erscheint jedoch möglicherweise erst später auf dem Monitor, in der Regel erst zum Beginn des nächsten Aktualisierungszyklus (vorausgesetzt, die V-Sync ist aktiviert). Daher wissen Sie nicht genau, wann die Anzeige erschienen ist, da Ihre Zeitstempel den Moment widerspiegeln, in dem die Anzeige in die Warteschlange gestellt wurde, und nicht den Moment, in dem sie präsentiert wurde. Um dieses Problem zu umgehen, können Sie einen sogenannten "blockierenden Flip" verwenden. Dies bedeutet im Grunde, dass der Computer beim Senden eines Befehls zur Anzeige einer neuen Anzeige einfriert, bis die Anzeige tatsächlich erscheint. Dies ermöglicht Ihnen sehr genaue Anzeigezeitstempel, zu Lasten einer erheblichen Leistungseinbuße, da der Computer während des Wartens auf die Anzeige eines Displays zum großen Teil eingefroren ist. Für Experimentzwecke gilt der blockierende Flip jedoch im Allgemeinen als optimale Strategie.

Schließlich können LCD-Monitore unter "Eingangslatenz" leiden. Dies bedeutet, dass es eine zusätzliche und manchmal variable Verzögerung zwischen dem Moment gibt, in dem der Computer "denkt", dass eine Anzeige erscheint, und dem Moment, in dem die Anzeige tatsächlich erscheint. Diese Verzögerung resultiert aus verschiedenen Formen der digitalen Verarbeitung, die vom Monitor durchgeführt werden, wie beispielsweise Farbkorrektur oder Bildglättung. Soweit ich weiß, kann die Eingangslatenz nicht programmgesteuert gelöst werden, und Sie sollten Monitore mit einer signifikanten Eingangslatenz für zeitkritische Experimente vermeiden.

Für eine verwandte Diskussion siehe:

- <http://docs.expyriment.org/Timing.html#visual>


### Die Aktualisierungsfrist einhalten

Stellen Sie sich vor, Sie kommen um 10:30 Uhr am Bahnhof an. Ihr Zug fährt um 11:00 Uhr ab, das gibt Ihnen genau 30 Minuten Zeit, um einen Kaffee zu holen. Wenn Sie jedoch genau 30 Minuten lang Kaffee trinken, erreichen Sie die Plattform genau rechtzeitig, um Ihren Zug abfahren zu sehen, und Sie müssen auf den nächsten Zug warten. Wenn Sie also 30 Minuten Zeit haben, sollten Sie etwas weniger als 30 Minuten lang Kaffee trinken, wie zum Beispiel 25 Minuten.

Die Situation ähnelt der Angabe von Intervallen für die Präsentation visueller Reize. Angenommen, Sie haben einen 100-Hz-Monitor (also 1 Aktualisierung alle 10 ms) und möchten einen Zielreiz für 100 ms darstellen, gefolgt von einer Maske. Ihre erste Neigung könnte sein, ein Intervall von genau 100 ms zwischen dem Ziel und der Maske anzugeben, denn das ist schließlich, was Sie wollen. Wenn Sie jedoch genau ein Intervall von 100 ms angeben, wird die Maske höchstwahrscheinlich die "Aktualisierungsfrist verpassen" und erst im nächsten Aktualisierungszyklus präsentiert, der 10 ms später ist (vorausgesetzt, V-Sync ist aktiviert). Wenn Sie also ein Intervall von 100 ms angeben, erhalten Sie in den meisten Fällen ein Intervall von 110 ms!

Die Lösung ist einfach: Sie sollten ein Intervall angeben, das etwas kürzer ist als das, was Sie erreichen möchten, beispielsweise 95 ms. Machen Sie sich keine Sorgen, dass das Intervall zu kurz ist, denn auf einem 100-Hz-Monitor ist das Intervall zwischen zwei Reizanzeigen zwangsläufig ein Vielfaches von 10 ms. Daher werden 95 ms zu 100 ms (10 Frames), 1 ms werden zu 10 ms (1 Frame) usw. Anders ausgedrückt, Intervalle werden aufgerundet (niemals abgerundet!) zum nächstgelegenen Intervall, das mit der Bildwiederholfrequenz Ihres Monitors vereinbar ist.

### Deaktivieren von Desktop-Effekten

Viele moderne Betriebssysteme nutzen grafische Desktop-Effekte. Diese bieten beispielsweise die Transparenzeffekte und die sanften Minimierungs- und Maximierungseffekte von Fenstern, die Sie auf den meisten modernen Betriebssystemen sehen. Obwohl die Software, aus denen diese Effekte bestehen, von System zu System variiert, bilden sie im Allgemeinen eine zusätzliche Schicht zwischen Ihrer Anwendung und der Anzeige. Diese zusätzliche Schicht kann verhindern, dass OpenSesame sich mit dem vertikalen Neuaufbau synchronisiert und / oder einen blockierenden Flip implementiert.

Obwohl Desktop-Effekte *möglicherweise* Probleme verursachen, tun sie dies normalerweise nicht. Dies scheint von System zu System und von Grafikkarte zu Grafikkarte unterschiedlich zu sein. Trotzdem ist es am besten, Desktop-Effekte auf Systemen, die für experimentelle Tests verwendet werden, zu deaktivieren, wenn das Betriebssystem dies zulässt.

Einige Tipps zu Desktop-Effekten für die verschiedenen Betriebssysteme:

- Unter *Windows XP* gibt es überhaupt keine Desktop-Effekte.
- Unter *Windows 7* können Desktop-Effekte deaktiviert werden, indem eines der unter "Einfache und hoher Kontrast Designs" aufgeführten Designs in der "Personalisierung" ausgewählt wird.
- Unter *Windows 10* gibt es keine Möglichkeit, Desktop-Effekte vollständig zu deaktivieren.
- Unter *Ubuntu und anderen Linux-Distributionen, die Gnome 3 verwenden*, gibt es keine Möglichkeit, Desktop-Effekte vollständig zu deaktivieren.
- Unter *Linux-Distributionen, die KDE verwenden*, können Sie Desktop-Effekte im Abschnitt "Desktop-Effekte" der Systemeinstellungen deaktivieren.
- Unter *Mac OS* gibt es anscheinend keine Möglichkeit, Desktop-Effekte vollständig zu deaktivieren.


### Stimulus-Vorbereitungszeit / die Prepare-Run-Struktur berücksichtigen

Wenn Ihnen genaues Timing während der visuellen Stimuluspräsentation wichtig ist, sollten Sie Ihre Stimuli im Voraus vorbereiten. Auf diese Weise erhalten Sie während der zeitkritischen Teile Ihres Experiments keine unvorhersehbaren Verzögerungen durch die Stimulusvorbereitung.

Betrachten wir zunächst ein Skript (Sie können dies in ein INLINE_SCRIPT-Element einfügen), das die Stimulus-Vorbereitungszeit im Intervall zwischen `canvas1` und `canvas2` einschließt (% LstStimPrepBad). Das angegebene Intervall beträgt 95 ms, so dass - unter Berücksichtigung der in [Making the refresh deadline] beschriebenen 'Aufrundungsregel' - ein Intervall von 100 ms auf meinem 60-Hz-Monitor zu erwarten wäre. Auf meinem Testsystem führt das unten stehende Skript jedoch zu einem Intervall von 150 ms, was 9 Frames auf einem 60-Hz-Monitor entspricht. Dies ist eine unerwartete Verzögerung von 50 ms oder 3 Frames aufgrund der Vorbereitung von `canvas2`.

%--
code:
 id: LstStimPrepBad
 syntax: python
 source: stimulus-preparation-bad.py
 caption: "In diesem Skript ist die Dauer zwischen `canvas1` und `canvas2` durch die Stimulus-Vorbereitungszeit beeinträchtigt."
--%

Betrachten wir nun eine einfache Variation des oben genannten Skripts (%LstStimPrepGood). Dieses Mal bereiten wir zunächst sowohl `canvas1` als auch `canvas2` vor und präsentieren sie erst danach. Auf meinem Testsystem ergibt dies ein konstantes Intervall von 100 ms, genau wie es sein sollte!

%--
code:
 id: LstStimPrepGood
 syntax: python
 source: stimulus-preparation-good.py
 caption: "In diesem Skript ist die Dauer zwischen `canvas1` und `canvas2` nicht durch die Stimulus-Vorbereitungszeit beeinträchtigt."
--%

Bei Verwendung der grafischen Benutzeroberfläche gelten die gleichen Überlegungen, aber OpenSesame hilft Ihnen, indem es die meiste Stimulus-Vorbereitung automatisch im Voraus behandelt. Sie müssen jedoch berücksichtigen, dass diese Vorbereitung auf Ebene der SEQUENCE-Elemente und nicht auf Ebene der LOOP-Elemente erfolgt. Praktisch gesehen bedeutet dies, dass das Timing * innerhalb * einer SEQUENCE nicht durch die Stimulus-Vorbereitungszeit beeinträchtigt wird. Das Timing * zwischen * SEQUENCEs jedoch schon.

Um dies konkreter zu machen, betrachten wir die unten gezeigte Struktur (%FigStimPrepBad). Nehmen wir an, die Dauer des SKETCHPAD-Elements ist auf 95 ms eingestellt, um eine Dauer von 100 ms anzustreben, oder 6 Frames auf einem 60-Hz-Monitor. Auf meinem Testsystem beträgt die tatsächliche Dauer 133 ms oder 8 Bilder, weil das Timing durch die Vorbereitung des SKETCHPAD-Elements beeinträchtigt wird, das jedes Mal ausgeführt wird, wenn die Sequenz ausgeführt wird. Dies ist also ein Beispiel dafür, wie Sie zeitkritische Teile Ihres Experiments *nicht* implementieren sollten.

%--
 Abbildung:
  ID: FigStimPrepBad
  Quelle: stimulus-preparation-incorrect.png
  Beschriftung: "Ein Beispiel für eine Versuchsstruktur, bei der das Timing zwischen aufeinanderfolgenden Präsentationen von SKETCHPAD durcheinander gebracht wird durch die Stimulus-Vorbereitungszeit. Die Abfolge der Ereignisse in diesem Fall ist: SKETCHPAD vorbereiten (2 Frames), SKETCHPAD zeigen (6 Frames), SKETCHPAD vorbereiten (2 Frames), SKETCHPAD zeigen (6 Frames), etc."
--%

Betrachten wir jetzt die unten gezeigte Struktur (%FigStimPrepGood). Angenommen, die Dauer von `sketchpad1` beträgt 95 ms, mit dem Ziel, ein 100 ms Intervall zwischen `sketchpad1` und `sketchpad2` zu erreichen. In diesem Fall werden beide Elemente als Teil derselben SEQUENCE angezeigt, und das Timing wird nicht durch Stimulus-Vorbereitungszeit beeinflusst. Auf meinem Testsystem beträgt das tatsächliche Intervall zwischen `sketchpad1` und `sketchpad2` daher tatsächlich 100 ms oder 6 Frames auf einem 60-Hz-Monitor.

Beachten Sie, dass dies nur für das Intervall zwischen `sketchpad1` und `sketchpad2` gilt, da sie in dieser Reihenfolge als Teil derselben Sequenz ausgeführt werden. Das Intervall zwischen `sketchpad2` beim Durchlauf *i* und `sketchpad1` beim Durchlauf *i+1* wird wieder durch Stimulus-Vorbereitungszeit beeinflusst.

%--
 Abbildung:
  ID: FigStimPrepGood
  Quelle: stimulus-preparation-correct.png
  Beschriftung: "Ein Beispiel für eine Versuchsstruktur, bei der das Timing zwischen der Präsentation von `sketchpad1` und `sketchpad2` nicht durch die Stimulus-Vorbereitungszeit beeinflusst wird. Die Abfolge der Ereignisse in diesem Fall ist wie folgt: `sketchpad1` vorbereiten (2 Frames), `sketchpad2` vorbereiten (2 Frames), `sketchpad1` zeigen (6 Frames), `sketchpad2` zeigen (6 Frames), `sketchpad1` vorbereiten (2 Frames), `sketchpad2` vorbereiten (2 Frames), `sketchpad1` zeigen (6 Frames), `sketchpad2` zeigen (6 Frames), etc."
--%

Für weitere Informationen siehe:

- [usage/prepare-run]

### Unterschiede zwischen Backends

OpenSesame ist nicht an eine bestimmte Art der Steuerung von Display, System-Timer usw. gebunden. Daher hat OpenSesame *per se* keine spezifischen Timing-Eigenschaften, da diese vom verwendeten Backend abhängen. Die Leistungsmerkmale der verschiedenen Backends sind nicht perfekt korreliert: Es ist möglich, dass auf einem System das [psycho]-Backend am besten funktioniert, während auf einem anderen System das [xpyriment]- Backend am besten funktioniert. Eine der großen Vorteile von OpenSesame ist daher, dass Sie auswählen können, welches Backend für Sie am besten funktioniert!

Im Allgemeinen sind die [xpyriment] und [psycho] Backends für zeitkritische Experimente vorzuziehen, da sie einen blockierenden Flip verwenden. Auf der anderen Seite ist das [legacy] Backend etwas stabiler und auch deutlich schneller bei der Verwendung von [forms].

Unter normalen Umständen haben die drei aktuellen OpenSesame-Backends die in %TblBackendInfo gezeigten Eigenschaften.

%--
 Tabelle:
  ID: TblBackendInfo
  Quelle: backend-info.csv
  Beschriftung: Eigenschaften der Backends.
--%

Siehe auch:

- [backends]

## Benchmark-Ergebnisse und Tipps für das Testen Ihres eigenen Systems

### Überprüfung, ob V-Sync aktiviert ist

Wie unter [Verständnis für Ihren Monitor] beschrieben, sollte die Präsentation eines neuen Displays idealerweise mit dem Beginn eines neuen Aktualisierungszyklus (d. h. 'V-Sync') übereinstimmen. Sie können testen, ob dies der Fall ist, indem Sie Displays unterschiedlicher Farben in schneller Abfolge präsentieren. Wenn V-Sync nicht aktiviert ist, werden Sie deutlich horizontale Linien sehen, die über den Monitor laufen (d. h. 'Tearing'). Um diesen Test durchzuführen, führen Sie ein Experiment mit dem folgenden Skript in einem INLINE_SCRIPT- Element aus (%LstVSync):

%--
 Code:
  ID: LstVSync
  Syntax: Python
  Quelle: v-sync-check.py
  Beschriftung: Ein Skript, das gelbe und blaue Displays in schneller Abfolge präsentiert. Eine fehlende Synchronisation mit der vertikalen Aktualisierung kann als horizontale Linien beobachtet werden, die über den Monitor laufen.
--%

### Präzision und Genauigkeit der Zeitmessung testen

Die Zeitmessung ist präzise oder konsistent, wenn Sie visuelle Reize immer wieder mit der gleichen Zeit präsentieren können. Zeitstempel sind genau, wenn sie genau widerspiegeln, wann visuelle Reize auf dem Monitor erscheinen. Das untenstehende Skript zeigt, wie Sie die Präzision und Genauigkeit der Zeitmessung überprüfen können. Dieser Test kann sowohl mit als auch ohne eine externe Fotodiode durchgeführt werden, obwohl die Verwendung einer Fotodiode eine zusätzliche Überprüfung bietet.

Um die Dinge einfach zu halten, nehmen wir an, dass Ihr Monitor mit 100 Hz arbeitet, was bedeutet, dass eine einzelne Bildwiederholung 10 ms dauert. Das Skript präsentiert dann eine weiße Leinwand für 1 Bildwiederholung (10 ms). Als nächstes präsentiert das Skript eine schwarze Leinwand für 9 Bildwiederholungen (90 ms). Beachten Sie, dass wir eine Dauer von 85 angegeben haben, die aufgerundet wird, wie unter [Making the refresh deadline] erklärt. Daher erwarten wir, dass das Intervall zwischen dem Beginn von zwei aufeinanderfolgenden weißen Anzeigen 10 Bildwiederholungen oder 100 ms beträgt (= 10 ms + 90 ms).

Wir können zwei Methoden verwenden, um zu überprüfen, ob das Intervall zwischen zwei weißen Anzeigen tatsächlich 100 ms beträgt:

1. Mit den von OpenSesame gemeldeten Zeitstempeln. Dies ist der einfachste Weg und im Allgemeinen genau, wenn das Backend ein blockierendes Flip verwendet.
2. Mit einer Fotodiode, die auf den Beginn der weißen Anzeigen reagiert und die Zeitstempel dieser Anfänge auf einem externen Computer protokolliert. Dies ist der beste Weg, um die Zeitmessung zu überprüfen, da er nicht auf die Selbstbeobachtung der Software angewiesen ist. Bestimmte Probleme, wie z. B. TFT-Input-Lag, die oben diskutiert wurden, treten nur mit der externen Fotodiodenmessung auf.

%--
code:
 id: LstIntervalBenchmark
 syntax: python
 source: interval-benchmark.py
 caption: Ein Python-Skript zum Testen der Zeitmessungs-Konsistenz und -Genauigkeit von Anzeigezeitstempeln. Sie können diesen Code in ein INLINE_SCRIPT-Element einfügen.
--%

Ich habe %LstIntervalBenchmark unter Windows XP mit allen drei Backends ausgeführt. Ich habe auch die Beginn der weißen Anzeigen mit einer Fotodiode aufgenommen, die an einen zweiten Computer angeschlossen war. Die Ergebnisse sind in %TblBenchmarkResults zusammengefasst.

%--
table:
 id: TblBenchmarkResults
 source: benchmark-results.csv
 caption: Benchmark-Ergebnisse für %LstIntervalBenchmark. Getestet mit Windows XP, HP Compaq dc7900, Intel Core 2 Quad Q9400 @ 2.66Ghz, 3GB, 21" ViewSonic P227f CRT. Jeder Test wurde zweimal durchgeführt (d. h. zwei Sitzungen). Die Spalte `Session` entspricht verschiedenen Testläufen. Die Spalte `Source` zeigt an, ob die Messungen von einer externen Fotiodiode stammen oder auf den internen Zeitstempeln von OpenSesame basieren.
--%

Wie Sie sehen können, zeigen die [xpyriment] und [psycho] Backends konsistent ein 100 ms Intervall. Das ist gut und entspricht unseren Erwartungen. Das [legacy] Backend zeigt jedoch ein 90 ms Intervall. Diese Diskrepanz ist darauf zurückzuführen, dass das [legacy] Backend kein blockierendes Flip verwendet (siehe [Understanding your monitor]), was zu einer gewissen Unvorhersehbarkeit in der Anzeigezeit führt. Beachten Sie auch, dass die Zeitstempel, die von der externen Fotodiode aufgezeichnet wurden, und die von OpenSesame gemeldeten Zeitstempel eng übereinstimmen. Diese Übereinstimmung zeigt, dass OpenSesame's Zeitstempel zuverlässig sind, obwohl sie für das [legacy] Backend aufgrund des fehlenden blockierenden Flips etwas weniger zuverlässig sind.

## Expyriment Benchmarks und Test-Suite

Ein sehr schönes Set von Benchmarks ist auf der Expyriment-Website verfügbar. Diese Informationen sind anwendbar auf OpenSesame-Experimente mit dem [xpyriment] Backend.

- <http://docs.expyriment.org/Timing.html>

Expyriment enthält eine sehr nützliche Test-Suite. Sie können diese Test-Suite starten, indem Sie das Beispiel-Experiment `test_suite.opensesame` ausführen oder Ihrem Experiment ein einfaches INLINE_SCRIPT mit den folgenden Codezeilen hinzufügen (%LstExpyrimentTestSuite):

%--
code:
 id: LstExpyrimentTestSuite
 syntax: python
 source: expyriment-test-suite.py
 caption: Ein Skript zum Starten der Expyriment-Test-Suite.
--%

For more information, please visit:

- <http://docs.expyriment.org/Testsuite.html>

## PsychoPy Benchmarks und zeitbezogene Informationen

Einige Informationen über die Zeitsteuerung finden Sie auf der PsychoPy-Dokumentationsseite. Diese Informationen gelten für OpenSesame Experimente, die das [psycho] Backend verwenden.

- <http://www.psychopy.org/general/timing/timing.html>

[psycho]: /backends/xpyriment/
[xpyriment]: /backends/xpyriment/
[legacy]: /backends/legacy/
[miscellaneous/clock-drift]: /miscellaneous/clock-drift
[usage/prepare-run]: /usage/prepare-run
[backends]: /backends
[forms]: /forms
