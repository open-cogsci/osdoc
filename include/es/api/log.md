<div class="ClassDoc YAMLDoc" markdown="1">

# instancia __log__

El objeto `log` proporciona el registro de datos. Se crea automáticamente un objeto `log` al inicio del experimento.

__Ejemplo__

~~~ .python
# Escribe una línea de texto
log.write('Mi mensaje personalizado de registro')
# Escribe todas las variables
log.write_vars()
~~~

[TOC]

## close(self)

Cierra el registro actual.

__Ejemplo__

~~~ .python
log.close()
~~~



## open(path)

Abre el registro actual. Si un registro ya estaba abierto, se cierra
automáticamente y se vuelve a abrir.

__Parámetros__

- **path**: La ruta al archivo de registro actual. En la mayoría de los casos (a menos que) se utilice un
sistema de registro personalizado, esto será un nombre de archivo.

__Ejemplo__

~~~ .python
# Abrir un nuevo registro
log.open('/ruta/hacia/el/nuevo/archivo/registro.csv')
~~~



## write(msg, newline=True)

Escribe un mensaje en el registro.

__Parámetros__

- **msg**: Un mensaje de texto. Al usar Python 2, esto debe ser
`unicode` o una cadena `str` codificada en utf-8. Al usar Python 3, esto
debe ser `str` o una cadena `bytes` codificada en utf-8.
- **newline**: Indica si se debe escribir una nueva línea después del mensaje.

__Ejemplo__

~~~ .python
# Escribe una sola cadena de texto
log.write(f'tiempo = {clock.time()}')
~~~



## write_vars(var_list=None)

Escribe variables en el registro.

__Parámetros__

- **var_list**: Una lista de nombres de variables para escribir, o None para escribir todas las variables
que existen en el experimento.

__Ejemplo__

~~~ .python
# Escribe todas las variables en el archivo de registro
log.write_vars()
~~~



</div>
