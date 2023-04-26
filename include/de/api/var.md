<div class="ClassDoc YAMLDoc" markdown="1">

# Instanz __var__

__Neu in 4.0.0__: Ab OpenSesame 4.0 sind alle experimentellen Variablen
auch im Python-Arbeitsbereich verfügbar. Das bedeutet, dass Sie das `var`-Objekt nicht mehr benötigen.

Das `var`-Objekt ermöglicht den Zugriff auf experimentelle Variablen.
Experimentelle Variablen sind die Variablen, die in der GUI leben und
häufig als unabhängige Variablen im LOOP-Element gesetzt werden, mit
der geklammerten (`{my_variable}`) Schreibweise verwiesen werden und vom
LOGGER-Element protokolliert werden.

Ein `var`-Objekt wird automatisch erstellt, wenn das Experiment beginnt.
Zusätzlich zu den unten aufgelisteten Funktionen werden die folgenden Semantiken unterstützt:

__Beispiel__:

~~~ .python
# Eine experimentelle Variable setzen
var.my_variable = u'my_value'
# Eine experimentelle Variable abrufen
print(u'Subject nr = %d' % var.subject_nr)
# Löschen (zurücksetzen) einer experimentellen
Variable
del var.my_variable
# Überprüfen, ob eine experimentelle Variable existiert
if
u'my_variable' in var:
    print(u'my_variable existiert!')
# Schleife durch alle
experimentellen Variablen
for var_name in var:
        print(u'gefundene Variable:
%s' % var_name)
~~~

[TOC]

## clear(preserve=[])

*Neu in 3.1.2*

Löscht alle experimentellen Variablen.

__Parameter__

- **preserve**: Eine Liste von Variablennamen, die nicht gelöscht werden sollen.

__Beispiel__

~~~ .python
var.clear()
~~~


## get(var, default=None, _eval=True, valid=None)

Ruft eine experimentelle Variable ab.


__Parameter__

- **var**: Die abzurufende Variable.
- **default**: Ein Standardwert, falls die Variable nicht existiert, oder `None` für
keinen Standardwert.
- **_eval**: Bestimmt, ob der zurückgegebene Wert auf Variablenverweise ausgewertet werden soll.
- **valid**: Eine Liste der gültigen Werte oder `None`, um alle Werte zuzulassen.

__Beispiel__

~~~ .python
print(u'my_variable = %s' % var.get(u'my_variable'))
# entspricht:
print(u'my_variable = %s' % var.my_variable)
# Wenn Sie jedoch Schlüsselwortargumente übergeben möchten, müssen Sie `get()` verwenden:
var.get(u'my_variable', default=u'a_default_value')
~~~


## has(var)

Überprüft, ob eine experimentelle Variable existiert.

__Parameter__

- **var**: Die zu prüfende Variable.

__Beispiel__

~~~ .python
if var.has(u'my_variable'):
        print(u'my_variable wurde definiert!')
# entspricht:
if u'my_variable' in var:
        print(u'my_variable wurde definiert!')
~~~


## inspect(self)

Erzeugt eine Beschreibung aller experimentellen Variablen, sowohl lebendiger
als auch hypothetischer.



__Gibt zurück__

- Ein Wörterbuch, bei dem die Variablennamen Schlüssel sind und die Werte Wörterbücher mit den
Quelle, Wert und lebendigen Schlüsseln sind.


## items(self)

Gibt eine Liste von (variable_name, value) Tupeln zurück. Siehe `var.vars()`
für eine Anmerkung zur Nicht-Erschöpflichkeit dieser Funktion.



__Gibt zurück__

- Eine Liste von (variable_name, value) Tupeln.

__Beispiel__

~~~ .python
for varname, value in var.items():
        print(varname, value)
~~~


## set(var, val)

Setzt eine experimentelle Variable.


__Parameter__

- **var**: Die zuzuweisende Variable.
- **val**: Der zuzuweisende Wert.

__Beispiel__

~~~ .python
var.set(u'my_variable', u'my_value')
# Entsprechend
var.my_variable = u'my_value'
~~~


## unset(var)

Löscht eine Variable.


__Parameter__

- **var**: Die zu löschende Variable.

__Beispiel__

~~~ .python
var.unset(u'my_variable')
# Entsprechend:
del var.my_variable
~~~


## vars(self)

Gibt eine Liste der experimentellen Variablen zurück. Da experimentelle
Variablen an mehreren Stellen gespeichert werden können, ist diese Liste möglicherweise nicht
erschöpfend. Das heißt, `u'my_var' in var` kann `True` zurückgeben, während
u'my_var' nicht in der Liste der Variablen enthalten ist, die von dieser Funktion zurückgegeben werden.



__Gibt zurück__

- Eine Liste der Variablennamen.

__Beispiel__

~~~ .python
for varname in var.vars():
        print(varname)
~~~


</div>