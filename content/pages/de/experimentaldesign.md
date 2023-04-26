title: Notation für experimentelles Design
hash: 060f0c16a9d8bf841b056d49c16778928d77563cfa43fa451a8ff159ed884b3b
locale: de
language: German

Von einer abstrakten Forschungsfrage zu einem konkreten experimentellen Design zu gelangen, kann schwierig sein. Sie können das Design für sich selbst verdeutlichen, indem Sie es in einer formalen Notation niederschreiben. Es gibt viele solcher Notationen, aber hier verwenden wir die von [Rouanet und Lepine (1977)][references] vorgeschlagene. Diese Notation ist einfach, aber flexibel genug, um die meisten experimentellen Designs abzudecken, denen Sie im realen Leben begegnen werden.

[TOC]

## Die grundlegende Notation

In dieser Notation werden Bedingungen (oder Faktoren) durch einen einzelnen Buchstaben mit einer kleinen Zahl bezeichnet, die angibt, wie viele Ebenen es gibt. Wenn Sie zum Beispiel drei Stimulusdauern haben, könnten Sie dies als D<sub>3</sub> angeben. Eine besondere Bedingung ist 'Teilnehmer'. Wenn Sie *N* Teilnehmer haben, geben Sie dies als <u>S</u><sub>N</sub> an. Es mag seltsam klingen, den Teilnehmer als Bedingung zu bezeichnen, aber im Grunde ist das genau das, was es ist.

Es gibt zwei Operatoren:

- &lt; &gt; zeigt das 'Einschließen', typischerweise verwendet für Bedingungen, die zwischen den Teilnehmern variieren
- × zeigt das 'Kreuzen', typischerweise verwendet für Bedingungen, die innerhalb der Teilnehmer variieren

Es gibt oft mehrere Möglichkeiten, ein experimentelles Design zu beschreiben. Beispielsweise können Sie Bedingungen weglassen, die für Ihre Forschungsfrage nicht relevant sind, wie zum Beispiel, ob ein Stimulus auf der linken oder rechten Seite der Anzeige erscheint.

## Within-subject Designs

In einem Within-subject-Design absolvieren alle Teilnehmer alle Bedingungen. Dies ist die leistungsfähigste Art von Design, da es nicht stark durch Variabilität zwischen den Teilnehmern betroffen ist: Sie können die Leistung eines Teilnehmers in Bedingung A mit seiner Leistung in Bedingung B vergleichen.

Betrachten Sie ein Posner-Cuing-Paradigma [(Posner, 1980)][references], bei dem ein Pfeil auf die linke oder rechte Seite der Anzeige zeigt. Dem Pfeil folgt ein Ziel, das ebenfalls auf der linken oder rechten Seite der Anzeige erscheint. Wir haben also zwei Bedingungen, die innerhalb der Teilnehmer variieren:

- *Cue-Seite* mit zwei Ebenen (links, rechts), oder C<sub>2</sub>
- *Zielseite* mit zwei Ebenen (links, rechts), oder T<sub>2</sub>

Wir können dieses Design als <u>S</u><sub>N</sub>×C<sub>2</sub>×T<sub>2</sub> schreiben

## Between-subject Designs

In einem Between-subject-Design absolvieren unterschiedliche Teilnehmer unterschiedliche experimentelle Bedingungen. Dies ist weniger leistungsfähig als ein Within-subject-Design, da Unterschiede zwischen den Teilnehmern eine wichtige Lärmquelle sind: Wenn die Leistung von Teilnehmer 1 in Bedingung A besser ist als die von Teilnehmer 2 in Bedingung B, wissen Sie nicht, ob dies auf einen Bedingungseffekt zurückzuführen ist oder einfach daran liegt, dass Teilnehmer 1 tendenziell besser abschneidet als Teilnehmer 2. Aus diesem Grund erfordern Between-subject-Designs eine große Anzahl von Teilnehmern.

Betrachten Sie [Bargh's (1996)][references] berühmtes (und umstrittenes) soziales Priming-Experiment, in dem einige Teilnehmer Wörter lasen, die mit hohem Alter assoziiert sind (z. B. 'rentner'), während andere Teilnehmer altersneutrale Wörter lasen (z. B. 'durstig').

Wir haben also eine Bedingung, die zwischen den Teilnehmern variiert:

- *Prime-Typ* mit zwei Ebenen (alt, neutral), oder P<sub>2<sub>

Wir können dieses Design als <u>S</u><sub>N</sub> &lt; P<sub>2</sub> &gt; schreiben

Rouanet und Lepine nennen dies *emboîtement* oder 'Einschließen'. Das bedeutet einfach, dass beide Ebenen von P ihre eigene Gruppe von N Teilnehmern haben. Daher beträgt die Gesamtzahl der Teilnehmer 2*N.

## Komplizierte Designs

Gelegentlich werden Sie auf kompliziertere Designs stoßen, die sich nicht leicht als entweder Within- oder Between-subject klassifizieren lassen. Psycholinguistische Experimente sind gute Beispiele dafür.

Betrachten Sie ein semantisches Priming-Experiment, bei dem einem Zielwort entweder ein semantisch verwandtes Prime (z. B. 'Garten' -> 'Blume' oder 'Katze' -> 'Hund') oder ein unzusammenhängendes Prime (z. B. 'Geld' -> 'Blume' oder 'Ja' -> 'Hund') vorangestellt ist. Um zu verhindern, dass ein Teilnehmer ein Wort mehrmals sieht, können Sie die Bedingungen zwischen den Wörtern "rotieren":

- Ungerade Teilnehmer (1, 3, 5, usw.) machen Rotation A:
    - 'Blume' ist in der verwandten Bedingung
    - 'Hund' ist in der unverwandten Bedingung
- Gerade Teilnehmer (2, 4, 6, usw.) machen Rotation B:
    - 'Blume' ist in der unverwandten Bedingung
    - 'Hund' ist in der verwandten Bedingung

Wir haben also zwei Bedingungen:

- *Prime-Typ* mit zwei Stufen (verwandt, unverwandt), oder P<sub>2</sub>; dies variiert innerhalb der Versuchspersonen
- *Rotation* mit zwei Stufen (A, B), oder R<sub>2</sub>; dies variiert zwischen den Teilnehmern

Daher ist das Design <u>S</u><sub>n</sub> &lt; R<sub>2</sub> &gt; × P<sub>2</sub>

## Einschränkungen

Diese Notation hat mehrere Einschränkungen, einschließlich:

- Man kann nicht angeben, wie oft bestimmte Bedingungen auftreten. Zum Beispiel treten in einer Posner-Cuing-Aufgabe gültige Trials (d.h. Cue und Ziel auf der gleichen Seite) in der Regel häufiger auf als ungültige Trials (d.h. Cue und Ziel auf gegenüberliegenden Seiten). Dies kann in der hier beschriebenen Notation nicht dargestellt werden.
- Es ist schwierig, die Rolle des 'Elements' in einem Design anzugeben. Zum Beispiel spielt das Zielwort in dem Design unter [Komplizierte Designs] eine ähnliche Rolle wie die des Teilnehmers. Es ist möglich, ein elementzentrisches Design oder ein teilnehmerzentrisches Design zu schreiben (wie im Beispiel), aber ich habe keine zufriedenstellende Möglichkeit gefunden, beides zu tun.

## Referenzen

<div class="reference" markdown="1">

Bargh, J. A., Chen, M., & Burrows, L. (1996). Automaticity of social behavior: Direct effects of trait construct and stereotype activation on action. *Journal of Personality and Social Psychology*, *71*(2), 230.

Posner, M. I. (1980). Orienting of attention. *Quarterly Journal of Experimental Psychology*, *32*(1), 3–25. doi:10.1080/00335558008248231

Rouanet, H., & Lepine, D. (1977). Structures linéaires et analyse des comparaisons. *Mathématiques et Sciences Humaines*, *56*, 5–46. Retrieved from: <http://www.numdam.org/item?id=MSH_1977__56__5_0>

</div>