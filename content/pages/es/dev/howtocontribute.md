title: Cómo contribuir
uptodate: false
hash: cdf0ef5efe4027ec45865c8235a04695c3ed9e91a1c8db4ffab4c5351d8c05d5
locale: es
language: Spanish

[TOC]

## Obtener el ultimo código fuente

El código fuente de OpenSesame está alojado en GitHub:

- <https://github.com/smathot/OpenSesame>.

GitHub proporciona una forma sencilla de colaborar en un proyecto. Si no estás familiarizado con GitHub, es posible que desees consultar su sitio de ayuda: <http://help.github.com/>.

La mejor (y más fácil) forma de contribuir al código es la siguiente:

1. Crear una cuenta de GitHub.
2. Crear un fork de OpenSesame <https://github.com/smathot/OpenSesame>.
3. Modificar tu fork.
4. Enviar una 'solicitud de pull', solicitando que tus cambios se combinen con el repositorio principal.

Cada versión principal de OpenSesame tiene su propia rama. Por ejemplo, la rama `ising` contiene el código para 3.0 *Interactive Ising*. La rama `master` contiene el código para la última versión estable.

## Desarrollar un complemento o extensión

Para el desarrollo de complementos o extensiones, consulta:

- %link:dev/plugin%
- %link:dev/extension%

## Traducir la interfaz de usuario

Para obtener instrucciones sobre cómo traducir la interfaz de usuario, consulta:

- %link:dev/translate%

## Directrices de estilo de codificación

El objetivo es mantener una base de código legible y consistente. Por lo tanto, ten en cuenta las siguientes pautas de estilo al contribuir con el código:

### Manejo de excepciones

Las excepciones deben manejarse a través de la clase `libopensesame.exceptions.osexception`. Por ejemplo:

~~~ .python
from libopensesame.exceptions import osexception
raise osexception(u'Ocurrió un error')
~~~

### Imprimir salida de depuración

La salida de depuración debe manejarse a través de `libopensesame.debug.msg()`, y se muestra solo cuando OpenSesame se inicia con el argumento de línea de comando `--debug`. Por ejemplo:

~~~ .python
from libopensesame import debug
debug.msg(u'Esto solo se mostrará en el modo de depuración')
~~~

### Sangría

La sangría debe basarse en tabulaciones. *Esta es la pauta de estilo más importante de todas*, porque la sangría mixta causa problemas y consume tiempo para corregir.

### Nombres, doc-strings y ajuste de línea

- Los nombres deben estar en minúsculas, con palabras separadas por guiones bajos.
- Cada función debe ir acompañada de un doc-string informativo, con el formato que se muestra a continuación. Si un doc-string es redundante, por ejemplo, porque una función anula otra función que tiene un doc-string, indique dónde se puede encontrar el doc-string completo.
- Por favor, no permitas que las líneas de código se extiendan más allá de 79 caracteres (donde una pestaña cuenta como 4 caracteres), con la excepción de las cadenas largas que resultan difíciles de dividir.

~~~ .python
def a_function(argument, keyword=None):

	"""
	desc:
		Esta es una cadena de documentos al estilo YAMLDoc, que permite una especificación completa
		de argumentos. Consultar también <https://github.com/smathot/python-yamldoc>.

	arguments:
		argument:   Este es un argumento.

	keywords:
		keyword:    Esta es una palabra clave.

	returns:
		Esta función devuelve algunos valores.
	"""

	pass

def a_simple_function():

	"""Este es un doc-string simple"""

	pass

~~~

### Escribir código compatible con Python 2 y 3

El código debe ser compatible con Python 2.7 y 3.4 y superior. Para facilitar la escritura de código compatible con Python 2 y 3, se incluyen algunos trucos en el módulo `py3compat`, que debe *importarse siempre* en tu script de la siguiente manera:

~~~ .python
from libopensesame.py3compat import *
~~~

Este módulo:

- Reasigna los tipos `str` y `unicode` de Python-2 a los tipos `bytes` y `str` de Python-3 (aproximadamente equivalentes). Por lo tanto, debes codificar con objetos `str` en la mayoría de los casos y objetos `bytes` en casos especiales.
- Agrega las siguientes funciones:
  - `safe_decode(s, enc='utf-8', errors='strict')` convierte cualquier objeto en un objeto `str`
  - `safe_encode(s, enc='utf-8', errors='strict')` convierte cualquier objeto en un objeto `bytes`
- Agrega una variable `py3`, que es `True` cuando se ejecuta en Python 3 y `False` cuando se ejecuta en Python 2.
- Agrega un objeto `basestr` cuando se ejecuta en Python 3.

### Unicode y cadenas

Asegúrate de que toda la funcionalidad sea compatible con Unicode. Para el código nuevo, usa *solamente* cadenas Unicode internamente.

~~~ .python
my_value = 'a string' # no preferido
my_value = u'a string' # preferido
~~~

Para más información, consulta:

- <http://docs.python.org/2/howto/unicode.html>

### Otro

Con la excepción de las pautas mostradas arriba, por favor siga el siguiente estándar:

- <http://www.python.org/dev/peps/pep-0008/#a-foolish-consistency-is-the-hobgoblin-of-little-minds>