title: Die Benutzeroberfläche nutzen
hash: 76f98fb7d0797037375f61ab159fef066c3fe407e469e0f97494e76d38e6177e
locale: de
language: German

OpenSesame verfügt über eine leistungsstarke grafische Benutzeroberfläche, die aus mehreren Komponenten besteht (%FigInterface).

%--
figure:
 id: FigInterface
 source: interface.png
 caption: Die OpenSesame-Benutzeroberfläche.
--%


[TOC]

## Symbolleisten und Menüleiste

### Die Menüleiste

Die Menüleiste (%FigMenubar) wird oben im Fenster angezeigt oder ist bei einigen Betriebssystemen in den Fensterrahmen integriert. Die Menüleiste enthält allgemeine Funktionen wie das Speichern und Öffnen von Experimenten, das Ausführen von Experimenten usw.

%--
figure:
 id: FigMenubar
 source: menubar.png
 caption: Die Menüleiste.
--%

### Die Haupt-Symbolleiste

Die Haupt-Symbolleiste (%FigMainToolbar) wird standardmäßig oben im Fenster direkt unter der Menüleiste angezeigt. Die Haupt-Symbolleiste enthält eine Auswahl der relevantesten Funktionen aus der Menüleiste.

%--
figure:
 id: FigMainToolbar
 source: main-toolbar.png
 caption: Die Haupt-Symbolleiste.
--%

### Die Element-Symbolleiste

Die Element-Symbolleiste (%FigItemToolbar) wird standardmäßig auf der linken Seite des Fensters angezeigt. Die Element-Symbolleiste enthält alle Elemente, das heißt, alle Bausteine eines Experiments. Sie können Elemente zu Ihrem Experiment hinzufügen, indem Sie sie aus der Element-Symbolleiste in den Übersichtsbereich ziehen.

%--
figure:
 id: FigItemToolbar
 source: item-toolbar.png
 caption: Die Element-Symbolleiste.
--%

## Der Tab-Bereich

Der Tab-Bereich ist der zentrale Teil des Fensters (%FigTabArea). Im Tab-Bereich werden Elementsteuerungen, Dokumentationen, wichtige Nachrichten usw. angezeigt. Der Tab-Bereich kann mehrere Tabs enthalten und funktioniert wie ein Browser mit Tabs.

%--
figure:
 id: FigTabArea
 source: tab-area.png
 caption: Der Tab-Bereich.
--%

## Der Übersichtsbereich

Der Übersichtsbereich (%FigOverviewArea) wird standardmäßig auf der linken Seite des Fensters rechts von der Element-Symbolleiste angezeigt. Der Übersichtsbereich zeigt die Struktur Ihres Experiments als Baum an. Sie können die Elemente in Ihrem Experiment neu anordnen, indem Sie sie in der Übersicht von einer Position zu einer anderen ziehen.

- Tastenkombination zum Ausblenden/ Einblenden: `Strg+\`

%--
figure:
 id: FigOverviewArea
 source: overview-area.png
 caption: Der Übersichtsbereich.
--%

## Der Dateipool

Der Dateipool (%FigFilePool) wird standardmäßig auf der rechten Seite des Fensters angezeigt. Er bietet eine Übersicht über alle Dateien, die dem Experiment beigefügt sind.

- Tastenkombination zum Ausblenden/ Einblenden: `Strg+P`

%--
figure:
 id: FigFilePool
 source: file-pool.png
 caption: Der Dateipool.
--%

## Das Debug-Fenster

Das Debug-Fenster (%FigDebugWindow) wird standardmäßig am unteren Rand des Fensters angezeigt. Es stellt einen [IPython-Interpreter](https://ipython.org/) zur Verfügung und wird als Standardausgabe verwendet, während ein Experiment läuft. Das heißt, wenn Sie die Python `print()`-Funktion verwenden, wird das Ergebnis im Debug-Fenster angezeigt.

- Tastenkombination zum Ausblenden/ Einblenden: `Strg+D`

%--
figure:
 id: FigDebugWindow
 source: debug-window.png
 caption: Das Debug-Fenster.
--%

## Der Variablen-Inspektor

Der Variablen-Inspektor (%FigVariableInspector) wird standardmäßig auf der rechten Seite des Fensters angezeigt. Er bietet eine Liste aller Variablen, die in Ihrem Experiment erkannt werden. Während Sie ein Experiment ausführen, bietet der Variablen-Inspektor auch eine Echtzeitübersicht der Variablen und ihrer Werte.

- Tastenkombination zum Ausblenden/ Einblenden: `Strg+I`

%--
figure:
 id: FigVariableInspector
 source: variable-inspector.png
 caption: Der Variablen-Inspektor.
--%

## Tastaturkürzel

Die unten aufgeführten Tastaturkürzel sind Standardwerte. Viele davon können über *Menü → Extras → Einstellungen* geändert werden.

### Allgemeine Tastenkürzel

Die folgenden Tastaturkürzel sind überall verfügbar:

- Schneller Wechsler: `Strg+Leertaste`
- Befehlspalette: `Strg+Umschalt+P`
- Neues Experiment: `Strg+N`
- Experiment öffnen: `Strg+O`
- Experiment speichern: `Strg+S`
- Experiment speichern als: `Strg+Umschalt+S`
- Rückgängig machen: `Strg+Alt+Z`
- Wiederherstellen: `Strg+Alt+Umschalt+Z`
- Experiment im Vollbildmodus ausführen: `Strg+R`
- Experiment im Fenster ausführen: `Strg+W`
- Schnellstart-Experiment: `Strg+Umschalt+W`
- Testexperiment im Browser: `Alt+Strg+W`
- Übersichtsbereich ein-/ ausblenden: `Strg+\`
- Debug-Fenster ein-/ ausblenden: `Strg+D`
- Dateipool ein-/ ausblenden: `Strg+P`
- Variableninspektor ein-/ ausblenden: `Strg+I`
- Fokus auf Übersichtsbereich: `Strg+1`
- Fokus auf Tab-Bereich: `Strg+2`
- Fokus auf Debug-Fenster: `Strg+3`
- Fokus auf Dateipool: `Strg+4`
- Fokus auf Variableninspektor: `Strg+5`

### Editor-Shortcuts

Die folgenden Tastaturkürzel sind in Editor-Komponenten verfügbar, wie zum Beispiel dem INLINE_SCRIPT:

- Zeile(n) (aus)kommentieren: `Strg+/`
- Text suchen: `Strg+F`
- Text ersetzen: `Strg+H`
- Suchen/Ersetzen-Dialog ausblenden: `Escape`
- Zeile duplizieren: `Strg+Umschalt+D`
- Rückgängig machen: `Strg+Z`
- Wiederherstellen: `Strg+Umschalt+Z`
- Kopieren: `Strg+C`
- Ausschneiden: `Strg+X`
- Einfügen: `Strg+V`

### Tab-Bereich-Shortcuts

Die folgenden Tastaturkürzel sind im Tab-Bereich verfügbar:

- Nächster Tab: `Strg+Tab`
- Vorheriger Tab: `Strg+Umschalt+Tab`
- Andere Tabs schließen: `Strg+T`
- Alle Tabs schließen: `Strg+Alt+T`
- Aktuellen Tab schließen: `Alt+T`

### Übersichts- und Sequenz-Shortcuts

Die folgenden Tastaturkürzel sind im Übersichtsbereich und dem SEQUENCE-Element verfügbar:

- Kontextmenü: `+`
- Element unverknüpft kopieren: `Strg+C`
- Element verknüpft kopieren: `Strg+Umschalt+C`
- Element einfügen: `Strg+V`
- Element löschen: `Entf`
- Element dauerhaft löschen: `Umschalt+Entf`
- Umbenennen: `F2`
- Run-if-Anweisung ändern (falls zutreffend): `F3`