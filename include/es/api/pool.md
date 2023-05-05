<div class="ClassDoc YAMLDoc" markdown="1">

# instancia __pool__

El objeto `pool` proporciona acceso tipo dict al repositorio de archivos. Cuando
se verifica si un archivo está en el repositorio de archivos, se buscan
varias carpetas.
Para obtener más detalles, consulte `pool.folders()`.

Se crea un objeto `pool`
automáticamente cuando comienza el experimento.

Además de las funciones
listadas a continuación, se admiten las siguientes semánticas:

__Ejemplos__

Uso básico:

~~~ .python
# Obtén la ruta completa a un archivo en el repositorio de archivos
print(f'La ruta completa a img.png es {pool["img.png"]}')
# Comprueba si un archivo está en el repositorio de archivos
if 'img.png' in pool:
    print('img.png está en el repositorio de archivos')
# Elimina un archivo del repositorio de archivos
del pool['img.png']
# Recorre todos los archivos en el repositorio de archivos. Esto recupera las rutas completas.
for path in pool:
    print(path)
# Comprueba el número de archivos en el repositorio de archivos
print(f'Hay {len(pool)} archivos en el repositorio de archivos')
~~~

Obtén una imagen del repositorio de archivos y usa un `Canvas` para mostrarla.

~~~ .python
image_path = pool['img.png']
my_canvas = Canvas()
my_canvas.image(image_path)
my_canvas.show()
~~~

[TOC]

## add(path, new_name=None)

Copia un archivo al repositorio de archivos.

__Parámetros__

- **path**: La ruta completa al archivo en el disco.
- **new_name**: Un nuevo nombre para el archivo en el repositorio, o None para usar el nombre original
del archivo.

__Ejemplo__

~~~ .python
pool.add('/home/username/Pictures/my_ing.png')
~~~



## clean_up(self)

Elimina la carpeta del repositorio.




## fallback_folder(self)

La ruta completa a la carpeta del repositorio alternativo, que es la
subcarpeta `__pool__` de la carpeta del experimento actual, o
`None` si esta carpeta no existe. El repositorio alternativo
es útil en combinación con un sistema de control de versiones,
como git, porque te permite guardar el
experimento como un archivo de texto sin formato, incluso al tener archivos
en el repositorio de archivos.



__Devuelve__

- 

__Ejemplo__

~~~ .python
if pool.fallback_folder() is not None:
    print('¡Hay una carpeta de repositorio alternativo!')
~~~



## files(self)

Devuelve todos los archivos en el repositorio de archivos.

__Devuelve__

- Una lista de rutas completas.

__Ejemplo__

~~~ .python
for path in pool.files():
    print(path)
# Equivalente a:
for path in pool:
    print(path)
~~~



## folder(self)

Muestra la ruta completa a la carpeta del repositorio (principal). Esta suele ser una
carpeta temporal que se elimina cuando termina el experimento.

__Devuelve__

- La ruta completa a la carpeta principal del repositorio.

__Ejemplo__

~~~ .python
print(f'La carpeta del repositorio está aquí: {pool.folder()}')
~~~



## folders(include_fallback_folder=True, include_experiment_path=False)

Proporciona una lista de todas las carpetas que se buscan al recuperar la
ruta completa a un archivo. Estas son (en orden):

1. La carpeta del repositorio de archivos
en sí, como lo devuelve `pool.folder()`.
2. La carpeta del experimento actual (si existe)
3. La carpeta del repositorio alternativo, del que se devuelve en
`pool.fallback_folder()` (si existe)

__Parámetros__

- **include_fallback_folder**: Indica si la carpeta del repositorio alternativo debe incluirse si es que
existe.
- **include_experiment_path**: Indica si la carpeta del experimento debe incluirse si es que
existe.

__Devuelve__

- Una lista de todas las carpetas.

__Ejemplo__

~~~ .python
print('Las siguientes carpetas se buscan archivos:')
for folder in pool.folders():
    print(folder)
~~~



## in_folder(path)

Comprueba si la ruta está en la carpeta del repositorio. Esto es diferente de
la sintaxis `path en pool` ya que solo verifica la carpeta principal del repositorio,
y no la carpeta del repositorio alternativo ni la carpeta del experimento.

__Parámetros__

- **path**: Un nombre base de archivo para verificar.

__Devuelve__

- 

__Ejemplo__

~~~ .python
print(pool.in_folder('cue.png'))
~~~



## rename(old_path, new_path)

Cambia el nombre de un archivo en la carpeta del repositorio.

__Parámetros__

- **old_path**: El antiguo nombre del archivo.
- **new_path**: El nuevo nombre del archivo.

__Ejemplo__

~~~ .python
pool.rename('my_old_img.png', 'my_new_img.png')
~~~



## size(self)

Obtiene el tamaño combinado en bytes de todos los archivos en el repositorio de archivos.

__Devuelve__

- 

__Ejemplo__

~~~ .python
print(f'El tamaño del grupo de archivos es de {pool.size()} bytes')
~~~



</div>