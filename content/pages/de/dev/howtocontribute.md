title: Wie man beiträgt
uptodate: false
hash: cdf0ef5efe4027ec45865c8235a04695c3ed9e91a1c8db4ffab4c5351d8c05d5
locale: de
language: German

[TOC]

## Den neuesten Quellcode erhalten

Der OpenSesame-Quellcode wird auf GitHub gehostet:

- <https://github.com/smathot/OpenSesame>.

GitHub bietet eine unkomplizierte Möglichkeit, an einem Projekt zusammenzuarbeiten. Wenn Sie mit GitHub nicht vertraut sind, sollten Sie sich die Hilfe-Seite ansehen: <http://help.github.com/>.

Der beste (und einfachste) Weg, Code beizutragen, ist wie folgt:

1. Erstellen Sie ein GitHub-Konto.
2. Erstellen Sie einen Fork von OpenSesame <https://github.com/smathot/OpenSesame>.
3. Modifizieren Sie Ihren Fork.
4. Senden Sie eine "Pull-Anfrage", in der Sie darum bitten, dass Ihre Änderungen in das Hauptrepository zurückgeführt werden.

Jede Hauptversion von OpenSesame hat ihren eigenen Zweig. Der `ising`-Zweig enthält beispielsweise den Code für die 3.0 *Interactive Ising*. Der `master`-Zweig enthält den Code für die neueste stabile Veröffentlichung.

## Ein Plugin oder eine Erweiterung entwickeln

Für die Plugin- oder Erweiterungsentwicklung sehen Sie:

- %link:dev/plugin%
- %link:dev/extension%

## Übersetzen der Benutzeroberfläche

Anweisungen zum Übersetzen der Benutzeroberfläche finden Sie unter:

- %link:dev/translate%

## Richtlinien zum Programmierstil

Ziel ist es, eine lesbare und einheitliche Codebasis aufrechtzuerhalten. Bitte beachten Sie daher die folgenden Stilrichtlinien, wenn Sie Code beitragen:

### Exception-Handling

Exceptions sollten über die `libopensesame.exceptions.osexception`-Klasse behandelt werden. Zum Beispiel:

~~~ .python
from libopensesame.exceptions import osexception
raise osexception(u'Ein Fehler ist aufgetreten')
~~~

### Debug-Ausgabe drucken

Debug-Ausgaben sollten über `libopensesame.debug.msg()` gehandhabt werden und werden nur angezeigt, wenn OpenSesame mit dem `--debug`-Befehlszeilenargument gestartet wird. Zum Beispiel:

~~~ .python
from libopensesame import debug
debug.msg(u'Das wird nur im Debug-Modus angezeigt')
~~~

### Einrückung

Die Einrückung sollte auf Tabulatoren basieren. *Dies ist die wichtigste aller Stilrichtlinien*, da gemischte Einrückung Probleme verursacht und zeitintensiv zu korrigieren ist.

### Namen, Doc-Strings und Zeilenumbrüche

- Namen sollten klein geschrieben sein, mit Unterstrichen zwischen den Wörtern.
- Jeder Funktion sollte ein informativer Docstring beigefügt sein, im unten gezeigten Format. Wenn ein Docstring überflüssig ist, z. B. weil eine Funktion eine andere Funktion überschreibt, die einen Docstring hat, geben Sie bitte an, wo der vollständige Docstring zu finden ist.
- Bitte lassen Sie Codezeilen nicht über 79 Zeichen hinausgehen (wobei ein Tabulator als 4 Zeichen zählt), mit Ausnahme von langen Zeichenketten, die schwer zu trennen sind.

~~~ .python
def a_function(argument, keyword=None):

	"""
	desc:
		Dies ist ein YAMLDoc-Stil-Docstring, der eine vollständige Spezifikation
		der Argumente ermöglicht. Siehe auch <https://github.com/smathot/python-yamldoc>.

	arguments:
		argument:   Dies ist ein Argument.

	keywords:
		keyword:    Dies ist ein Stichwort.

	returns:
		Diese Funktion gibt einige Werte zurück.
	"""

	pass

def a_simple_function():

	"""Dies ist ein einfacher Doc-String"""

	pass

~~~

### Python 2 und 3 kompatiblen Code schreiben

Der Code sollte mit Python 2.7 und 3.4 und höher kompatibel sein. Um das Schreiben von Python 2 und 3 kompatiblen Code zu erleichtern, sind einige Tricks im `py3compat`-Modul enthalten, das *immer* in Ihrem Skript wie folgt importiert werden sollte:

~~~ .python
from libopensesame.py3compat import *
~~~

Dieses Modul:

- Ordnet die Python-2-Typen `str` und `unicode` den (ungefähr) äquivalenten Python-3-Typen `bytes` und `str` zu. Sie sollten daher in den meisten Fällen mit `str`-Objekten und in besonderen Fällen mit `bytes`-Objekten arbeiten.
- Fügt die folgenden Funktionen hinzu:
  - `safe_decode(s, enc='utf-8', errors='strict')` wandelt jedes Objekt in ein `str`-Objekt um
  - `safe_encode(s, enc='utf-8', errors='strict')` wandelt jedes Objekt in ein `bytes`-Objekt um
- Fügt eine `py3`-Variable hinzu, die bei Ausführung auf Python 3 `True` und bei Ausführung auf Python 2 `False` ist.
- Fügt auf Python 3 ein `basestr`-Objekt hinzu.

### Unicode und Zeichenketten

Stellen Sie sicher, dass alle Funktionen Unicode-sicher sind. Verwenden Sie für neuen Code *nur* Unicode-Zeichenketten intern.

~~~ .python
my_value = 'a string' # nicht bevorzugt
my_value = u'a string' # bevorzugt
~~~

Für weitere Informationen, siehe:

- <http://docs.python.org/2/howto/unicode.html>

### Sonstige

Mit Ausnahme der oben gezeigten Richtlinien, bitte halten Sie sich an die folgende Norm:

- <http://www.python.org/dev/peps/pep-0008/#a-foolish-consistency-is-the-hobgoblin-of-little-minds>