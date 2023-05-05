<div class="ClassDoc YAMLDoc" markdown="1">

# instancia __var__

__Nuevo en 4.0.0__: A partir de OpenSesame 4.0, todas las variables experimentales también están
disponibles en el espacio de trabajo de Python. Esto significa que, por lo tanto,
no necesitas más el objeto `var`.

El objeto `var` proporciona acceso a las variables experimentales.
Las variables experimentales son las variables que viven en la GUI y están
configuradas comúnmente como variables independientes en el elemento LOOP, referenciadas
mediante la notación de llaves (`{my_variable}`), y registradas por
el ítem LOGGER.

Se crea automáticamente un objeto `var` cuando comienza el experimento.
Además de las funciones que se detallan a continuación, se admiten las siguientes semánticas:

__Ejemplo__:

~~~ .python
# Establecer una variable experimental
var.my_variable = u'my_value'
# Obtener una variable experimental
print(u'Sujeto nr = %d' % var.subject_nr)
# Borrar (deshacer) una variable experimental
del var.my_variable
# Verificar si existe una variable experimental
if
u'my_variable' in var:
    print(u'¡my_variable existe!')
# Recorrer todas
las variables experimentales
for var_name in var:
        print(u'variable encontrada:
%s' % var_name)
~~~

[TOC]

## clear(preserve=[])

*Nuevo en 3.1.2*

Limpia todas las variables experimentales.

__Parámetros__

- **preserve**: Una lista de nombres de variables que no deben borrarse.

__Ejemplo__

~~~ .python
var.clear()
~~~



## get(var, default=None, _eval=True, valid=None)

Obtiene una variable experimental.

__Parámetros__

- **var**: La variable a obtener.
- **default**: Un valor por defecto en caso de que la variable no exista o `None` para
sin valor por defecto.
- **_eval**: Determina si la variable devuelta debe ser evaluada para
referencias de variables.
- **valid**: Una lista de valores válidos, o `None` para permitir todos los valores.

__Ejemplo__

~~~ .python
print('my_variable = %s' % var.get(u'my_variable'))
# Equivalente a:
print('my_variable = %s' % var.my_variable)
# Pero si desea pasar argumentos de palabras clave, debe usar `get()`:
var.get(u'my_variable', default=u'a_default_value')
~~~



## has(var)

Verifica si existe una variable experimental.

__Parámetros__

- **var**: La variable a comprobar.

__Ejemplo__

~~~ .python
if var.has(u'my_variable'):
        print(u'¡my_variable ha sido definida!')
# Equivalente a:
if u'my_variable' in var:
        print(u'¡my_variable ha sido definida!')
~~~



## inspect(self)

Genera una descripción de todas las variables experimentales, tanto vivas
como hipotéticas.

__Devoluciones__

- Un diccionario donde los nombres de las variables son claves y los valores son diccionarios con
claves de fuente, valor y vida.


## items(self)

Devuelve una lista de tuplas (nombre_variable, valor). Vea `var.vars()`
para obtener información sobre la no exhaustividad de esta función.

__Devoluciones__

- Una lista de tuplas (nombre_variable, valor).

__Ejemplo__

~~~ .python
for varname, value in var.items():
        print(varname, value)
~~~



## set(var, val)

Establece una variable experimental.

__Parámetros__

- **var**: La variable a asignar.
- **val**: El valor a asignar.

__Ejemplo__

~~~ .python
var.set(u'my_variable', u'my_value')
# Equivalente a
var.my_variable = u'my_value'
~~~



## unset(var)

Elimina una variable.

__Parámetros__

- **var**: La variable a eliminar.

__Ejemplo__

~~~ .python
var.unset(u'my_variable')
# Equivalente a:
del var.my_variable
~~~



## vars(self)

Devuelve una lista de variables experimentales. Debido a que las variables experimentales
pueden almacenarse en varios lugares, esta lista puede no ser
exhaustiva. Es decir, `u'my_var' in var` puede devolver `True`, mientras
u'my_var' no está en la lista de variables devueltas por esta función.

__Devoluciones__

- Una lista de nombres de variables.

__Ejemplo__

~~~ .python
for varname in var.vars():
        print(varname)
~~~



</div>