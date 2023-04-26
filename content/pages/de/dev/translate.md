title: the following text into German:

Welcome to the OpenSesame experiment!

This is an example of how to create a simple experiment using OpenSesame. We will be using various components, such as sketchpads, keyboard_responses, and samplers to create a basic psychology experiment.

In this experiment, participants will see a series of images on the screen and will have to press a key to indicate whether the image is a face or a house. The images will be presented in random order.

Before starting the experiment, we will ask participants to provide informed consent by reading a form_consent and ticking a box to confirm that they agree to participate.

During the experiment, we will use inline_javascript to randomize the presentation order of the images and to keep track of the participant's performance.

At the end of the experiment, we will thank the participants for their participation and inform them of the percentage of correct responses.

Please pay attention to the use of OpenSesame components and the structure of the experiment, as it will help you design your own experiments in the future.

Thanks for using OpenSesame, and good luck with your experiments!

Note: Remember to always test your experiment before collecting data, as it helps to identify and fix any issues beforehand.
hash: 6c70867370aa97b006209d57e083504cd28b4f73a9eb715aae26ff5532faaf08
locale: de
language: German


Wenn Sie eine Übersetzung anbieten möchten, wird empfohlen, zuerst eine Anfrage an <s.mathot@cogsci.nl> zu senden oder eine Nachricht im [Forum](https://forum.cogsci.nl/) zu posten, um sicherzustellen, dass Ihre Sprache noch nicht bearbeitet wird.

Um eine Übersetzung beizutragen, sind sehr wenige technische Kenntnisse erforderlich!

[TOC]


## OpenSesame mit einer bestimmten Sprache starten

Standardmäßig verwendet OpenSesame die Standardsprache Ihres Betriebssystems, wenn eine Übersetzung verfügbar ist, und wechselt zu Englisch, wenn keine Übersetzung verfügbar ist. Um OpenSesame mit einer bestimmten Sprache zu starten, können Sie die Sprachoption unter Menü → Extras → Einstellungen ändern.


## Wie man übersetzt


### Übersetzen von Markdown-Tabs


#### Übersetzen von Markdown-Tabs

Markdown-Tabs sind die websiteähnlichen Tabs, die Text und grundlegende Optionen darstellen. Ein Beispiel für einen Markdown-Tab ist der "Erste Schritte"-Tab, den Sie sehen, wenn Sie OpenSesame starten.

Um einen Markdown-Tab zu übersetzen, suchen Sie zunächst die nicht übersetzte (englische) `.md`-Datei. Im Fall des "Erste Schritte"-Tabs ist dies:

- `opensesame_extensions\get_started\get_started.md`

Kopieren Sie anschließend diese Originaldatei zu `[ursprünglicher Ordner]\locale\[Ihr Gebietsschema-Code]\get_started.md`. Wenn Sie also an einer französischen (`fr_FR`) Übersetzung arbeiten, würden Sie die originale `get_started.md` kopieren nach (Unterordner erstellen, wenn sie noch nicht vorhanden sind):

- `opensesame_extensions\get_started\locale\fr_FR\get_started.md`

Öffnen Sie abschließend die zu übersetzende `get_started.md`-Datei in einem Texteditor und übersetzen Sie sie.


#### Eine Liste der zu übersetzenden Markdown-Tabs

Im [OpenSesame-Quellcode](https://github.com/smathot/opensesame):

- `opensesame_extensions/update_checker/failed.md`
- `opensesame_extensions/update_checker/update-available.md`
- `opensesame_extensions/update_checker/up-to-date.md`
- `opensesame_extensions/toolbar_menu/system-information.md`
- `opensesame_extensions/help/offline_help.md`
- `opensesame_extensions/bug_report/failure.md`
- `opensesame_extensions/bug_report/report.md`
- `opensesame_extensions/bug_report/success.md`
- `opensesame_extensions/after_experiment/finished.md`
- `opensesame_extensions/system_information/system-information.md`
- `opensesame_extensions/get_started/get_started.md`
- `opensesame_extensions/opensesame_3_notifications/new-user.md`
- `opensesame_extensions/opensesame_3_notifications/old-experiment.md`
- `opensesame_extensions/opensesame_3_notifications/new-experiment.md`
- `opensesame_plugins/notepad/notepad.md`
- `opensesame_plugins/port_reader/port_reader.md`
- `opensesame_plugins/repeat_cycle/repeat_cycle.md`
- `opensesame_plugins/quest_staircase_init/quest_staircase_init.md`
- `opensesame_plugins/parallel/parallel.md`
- `opensesame_plugins/advanced_delay/advanced_delay.md`
- `opensesame_plugins/joystick/joystick.md`
- `opensesame_plugins/reset_feedback/reset_feedback.md`
- `opensesame_plugins/fixation_dot/fixation_dot.md`
- `opensesame_plugins/touch_response/touch_response.md`
- `opensesame_plugins/external_script/external_script.md`
- `opensesame_plugins/quest_staircase_next/quest_staircase_next.md`
- `opensesame_plugins/video_player/video_player.md`
- `opensesame_resources/help/missing.md`
- `opensesame_resources/help/new_item_warning.md`

Im [Rapunzel-Quellcode](https://github.com/smathot/rapunzel):

- `opensesame_extensions/RapunzelWelcome/rapunzel_welcome.md`


### Übersetzen des Quellcodes und der Benutzeroberfläche


#### Schritt 1: Herunterladen von translatables.ts

Wenn Sie eine Übersetzung von Grund auf neu beginnen, dann starten Sie mit `translatables.ts`, das alle zu übersetzenden Zeichenketten enthält. OpenSesame und Rapunzel haben jeweils ihre eigene Version dieser Datei, die beide übersetzt werden müssen.

Im [OpenSesame-Quellcode](https://github.com/smathot/OpenSesame/) finden Sie diese Datei unter:

- `opensesame_resources/ts/translatables.ts`

Im [Rapunzel-Quellcode](https://github.com/smathot/rapunzel/) finden Sie diese Datei unter:

- `opensesame_extensions/RapunzelLocale/translatables.ts`

Sie können entweder den Quellcode herunterladen oder klonen und diese Dateien direkt öffnen. Oder Sie können sie über GitHub anzeigen. In diesem Fall sehen Sie oben rechts in der Datei einen "Raw"-Link. Klicken Sie mit der rechten Maustaste auf diesen Link und wählen Sie "Datei speichern unter" (oder ähnliches, je nach Browser), um die Datei auf Ihrer Festplatte zu speichern.

#### Schritt 2: Installieren Sie Qt Linguist

Qt Linguist ist ein grafisches Tool, das Ihnen bei der Übersetzung helfen wird. Es ist benutzerfreundlich und ermöglicht es Ihnen, einfach einen englischen Text auszuwählen und eine Übersetzung einzugeben.

__Windows__

Sie können eine eigenständige Version von Qt Linguist von hier herunterladen:

- <https://github.com/thurask/Qt-Linguist/releases>

__Mac OS__

Sie können eine eigenständige Version von Qt Linguist von hier herunterladen:
- <https://github.com/lelegard/qtlinguist-installers/releases>

__Linux__

Unter Linux ist Qt Linguist in der Regel in den Repositories verfügbar. Beispielsweise kann es unter Ubuntu mit folgendem Befehl installiert werden:

	sudo apt-get install qttools5-dev-tools

#### Schritt 3: Öffnen Sie translatables.ts in Qt Linguist

Starten Sie nun Qt Linguist und öffnen Sie `translatables.ts`. Zuerst werden Sie aufgefordert, eine Quell- und Zielsprache einzugeben. Lassen Sie die Quelle wie sie ist: "POSIX/ Any country". Die Zielsprache sollte auf die Sprache eingestellt sein, in die Sie OpenSesame übersetzen werden. Lassen Sie die Option "Land/Region" auf "Any country". Sie können diese Einstellungen später über Menü → Bearbeiten → Übersetzungsdatei-Einstellungen ändern.

Jetzt können Sie mit dem Übersetzen beginnen! Auf der linken Seite sehen Sie eine Liste von "Kontexten". Diese zeigen an, in welchem Zusammenhang der Text angezeigt wird, was hilfreich ist. Um zu übersetzen, klicken Sie einfach auf die erste Quelltext-Zeichenkette im ersten Kontext, geben Sie eine passende Übersetzung ein und drücken Sie `Strg+Enter`, um zur nächsten Zeichenkette zu gelangen.

Einige Zeichenketten enthalten HTML-Tags, wie folgt:

	Size<br /><i>in pixels</i>

In diesem Fall ändern Sie nur den Text und lassen die HTML-Tags unverändert. Für eine deutsche Übersetzung würde dies werden:

	Größe<br /><i>in Pixeln</i>

Einige Zeichenketten enthalten Platzhalter, wie folgt:

	Tell me more about the %s item

Diese `%s` (und `%d`, `%f`, `{}`, usw.) Platzhalter sind Lücken, die von OpenSesame dynamisch ausgefüllt werden. Bitte beachten Sie diese (das Entfernen eines Platzhalters führt zum Absturz des Programms!) und versuchen Sie, eine passende Übersetzung um sie herum zu erstellen. Für eine deutsche Übersetzung würde dies werden:

	Erzähl mir mehr über das %s Element

#### Schritt 4: Übersetzung in `.qm` kompilieren und testen

OpenSesame verwendet nicht direkt die `.ts`-Datei, sondern erfordert eine Datei im `.qm`-Format. Sie können diese Datei leicht innerhalb von Qt Linguist erstellen, indem Sie "Datei → Release als" auswählen. Erstellen Sie eine `.qm`-Datei mit demselben Namen (außer der Erweiterung) wie die ursprüngliche Datei.

Für OpenSesame sollte diese Datei gespeichert werden als (ändern Sie `de_DE` in das entsprechende Gebietsschema):

- `opensesame_resources/locale/de_DE.qm`

Für Rapunzel sollte diese Datei gespeichert werden als (ändern Sie `de_DE` in das entsprechende Gebietsschema):

- `opensesame_extensions/RapunzelLocale/de_DE.qm`

## Speichern und übermitteln Sie Ihre Übersetzungen

### Per E-Mail senden

Wenn Sie mit Ihren Übersetzungen zufrieden sind, senden Sie die übersetzte `.ts`-Datei und alle übersetzten `md`-Dateien an <s.mathot@cogsci.nl>.

### Über GitHub einreichen

Sie können Ihre Übersetzung auch über GitHub einreichen (und aktualisieren). Fügen Sie zuerst Ihre Übersetzung Ihrer OpenSesame-Gabel hinzu, als `opensesame_resources/ts/ll_RR.ts`, wobei `ll` für die Sprache und `RR` für die Region steht. Zum Beispiel steht `en_US` für US-englisch, `fr_FR` für Französisch und `zh_CN` für Chinesisch. Eine Liste der gültigen Regionen und Sprachen finden Sie [hier](http://www.iana.org/assignments/language-subtag-registry).

Fügen Sie auf ähnliche Weise alle übersetzten `.md`-Dateien Ihrem OpenSesame-Fork hinzu.

Senden Sie schließlich eine Pull-Anfrage, um Ihre Übersetzung in OpenSesame aufzunehmen.

## Eine bestehende Übersetzung aktualisieren

Der Prozess zur Aktualisierung einer vorhandenen Übersetzung ähnelt dem oben beschriebenen Vorgang für das Erstellen einer neuen Übersetzung. Der entscheidende Unterschied besteht darin, dass Sie nicht mit `resources/ts/translatables.ts` beginnen, sondern mit einer nicht leeren Übersetzungsdatei, wie zum Beispiel `resources/ts/fr_FR.ts`.