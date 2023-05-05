<div class="ClassDoc YAMLDoc" markdown="1">

# instancia __items__

El objeto `items` proporciona acceso tipo diccionario a los elementos. Es principalmente
útil para ejecutar elementos de forma programática.

Se crea automáticamente un objeto `items` cuando comienza el experimento.

Además de las funciones enumeradas a continuación, se admiten las siguientes semánticas:

__Ejemplo__

~~~ .python
# Preparar y ejecutar programáticamente un elemento sketchpad.
items.execute('my_sketchpad')
# Verificar si existe un elemento
if 'my_sketchpad' in items:
    print('my_sketchpad existe')
# Eliminar un elemento
del items['my_sketchpad']
# Recorrer todos los nombres de elementos
for item_name in items:
    print(item_name)
~~~

[TOC]

## execute(name)

Ejecuta las fases de ejecución y preparación de un elemento y actualiza el
pila de elementos.


__Parámetros__

- **name**: El nombre de un elemento.

__Ejemplo__

~~~ .python
items.execute('target_sketchpad')
~~~



## new(_type, name=None, script=None, allow_rename=True)

Crea un nuevo elemento.


__Parámetros__

- **_type**: El tipo de elemento.
- **name**: El nombre del elemento, o None para elegir un nombre único basado en el tipo de
elemento.
- **script**: Un script de definición, o None para comenzar con un elemento en blanco.
- **allow_rename**: Indica si OpenSesame puede usar un nombre diferente al que
se proporciona como `name` para evitar nombres duplicados, etc.

__Devuelve__

- El elemento recién generado.

__Ejemplo__

~~~ .python
items.new('sketchpad', name='my_sketchpad')
items['my_sketchpad'].prepare()
items['my_sketchpad'].run()
~~~



## prepare(name)

Ejecuta la fase de preparación de un elemento y actualiza la pila de elementos.


__Parámetros__

- **name**: El nombre de un elemento.

__Ejemplo__

~~~ .python
items.prepare('target_sketchpad')
items.run('target_sketchpad')
~~~



## run(name)

Ejecuta la fase de ejecución de un elemento y actualiza la pila de elementos.


__Parámetros__

- **name**: El nombre de un elemento.

__Ejemplo__

~~~ .python
-items.prepare('target_sketchpad')
items.run('target_sketchpad')
~~~



## valid_name(item_type, suggestion=None)

Genera un nombre único válido que se asemeje al nombre deseado.


__Parámetros__

- **item_type**: El tipo del elemento para sugerir un nombre.
- **suggestion**: El nombre deseado, o None para elegir un nombre basado en el tipo de elemento.

__Devuelve__

- Un nombre único.

__Ejemplo__

~~~ .python
valid_name = items.valid_name('sketchpad', 'an invalid name')
~~~



</div>