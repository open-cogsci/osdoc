title: Registro y lectura de archivos de datos
hash: 6c081bb9571ecf270fcbd02104d88319bf6044245745b621d549cbc38c34e370
locale: es
language: Spanish

Siempre verifica tres veces si tus datos se han registrado correctamente antes de ejecutar tu experimento.
{: .page-notification}

[TOC]

## Usando el elemento LOGGER

OpenSesame no registrará tus datos automáticamente. En cambio, debes insertar un elemento LOGGER, típicamente al final de tu secuencia de pruebas.

%--
figure:
 id: FigLogger
 source: logger.png
 caption: |
  El elemento LOGGER.
--%

La forma más sencilla de utilizar LOGGER es dejando habilitada la opción "Registrar automáticamente todas las variables". De esa manera, todas las variables que OpenSesame conoce se escriben en el archivo de registro, excepto aquellas que están explícitamente excluidas (ver más abajo).

Puedes incluir explícitamente qué variables quieres registrar. La razón principal para hacerlo es cuando descubres que faltan algunas variables (porque OpenSesame no las detectó automáticamente) o si has desactivado la opción "Registrar automáticamente todas las variables",

También puedes excluir explícitamente ciertas variables del archivo de registro. La razón principal para hacerlo es mantener limpios los archivos de registro al excluir variables que generalmente no son útiles.

En general, debes crear solo un elemento LOGGER y reutilizar ese LOGGER en diferentes ubicaciones de tu experimento si es necesario (es decir, utilizar copias vinculadas del mismo elemento LOGGER). Si creas múltiples LOGGER (en lugar de usar un solo LOGGER varias veces), todos escribirán en el mismo archivo de registro y el resultado será un desorden.

## Usando Python inline script

Puedes escribir en el archivo de registro utilizando el objeto `log`:

~~~ .python
log.write('¡Esto se escribirá en el archivo de registro!')
~~~

Para obtener más información, consulte:

- %link:log%

Por lo general, no debes escribir directamente en el archivo de registro y usar un elemento LOGGER al mismo tiempo; hacerlo dará como resultado archivos de registro desordenados.

## Formato de los archivos de datos

Si has utilizado el elemento LOGGER estándar, los archivos de datos están en el siguiente formato (simplemente csv estándar):

- texto sin formato
- separados por comas
- entre comillas dobles (las comillas dobles literales se escapan con barras invertidas)
- finales de línea estilo Unix
- codificado en UTF-8
- nombres de columnas en la primera fila

## Leer y procesar archivos de datos

### En Python con pandas o DataMatrix

En Python, puedes usar [pandas](http://pandas.pydata.org/) para leer archivos csv.

```python
import pandas
df = pandas.read_csv('sujeto-1.csv')
print(df)
```

O [DataMatrix](https://datamatrix.cogsci.nl/):

```python
from datamatrix import io
dm = io.readtxt('sujeto-1.csv')
print(dm)
```

### En R

En R, puedes simplemente usar la función `read.csv()` para leer un solo archivo de datos.

~~~ .R
df = read.csv('sujeto-1.csv', encoding = 'UTF-8')
head(df)
~~~

Además, puedes utilizar la función `read_opensesame()` del paquete [readbulk](https://github.com/pascalkieslich/readbulk) para leer y combinar fácilmente varios archivos de datos en un gran marco de datos. El paquete está disponible en CRAN y se puede instalar a través de `install.packages('readbulk')`.

~~~ .R
# Leer y combinar todos los archivos de datos almacenados en la carpeta "raw_data"
library(readbulk)
df = read_opensesame('raw_data')
~~~

### En JASP

[JASP](http://jasp-stats.org/), un paquete estadístico de código abierto, abre archivos csv directamente.

### En LibreOffice Calc

Si abres un archivo csv en LibreOffice Calc, debes indicar el formato de datos exacto, como se indica en %FigLibreOffice. (La configuración predeterminada suele ser correcta).

%--
figure:
 source: libreoffice.png
 id: FigLibreOffice
--%

### En Microsoft Excel

En Microsoft Excel, debes utilizar el Asistente para importar texto.

### Combinar múltiples archivos de datos en un solo archivo grande

Para algunos propósitos, como el uso de tablas dinámicas, puede ser conveniente combinar todos los archivos de datos en un solo archivo grande. Con Python DataMatrix, puedes hacerlo con el siguiente script:

```python
import os
from datamatrix import DataMatrix, io, operations as ops

# Cambia esto a la carpeta que contiene los archivos .csv
SRC_FOLDER = 'student_data'
# Cambia esto a una lista de nombres de columnas que quieras mantener
COLUMNS_TO_KEEP = [
    'RT_search',
    'load',
    'memory_resp'
]


dm = DataMatrix()
for basename in os.listdir(SRC_FOLDER):
    path = os.path.join(SRC_FOLDER, basename)
    print('Leyendo {}'.format(path))
    dm <<= ops.keep_only(io.readtxt(path), *COLUMNS_TO_KEEP)
io.writetxt(dm, 'merged-data.csv')
```


## Registro en OSWeb

Cuando ejecutas un experimento en un navegador con OSWeb, el registro funciona de manera diferente a cuando ejecutas un experimento en el escritorio.

Específicamente, cuando inicias un experimento de OSWeb directamente desde OpenSesame, el archivo de registro se descarga al final del experimento. Este archivo de registro está en formato `.json`. Cuando inicias un experimento de OSWeb desde JATOS, no hay un archivo de registro como tal, pero todos los datos se envían a JATOS desde donde se pueden descargar.

Ver también:

- %link:manual/osweb/workflow%



[libreoffice]: http://www.libreoffice.org/
[openoffice]: http://www.openoffice.org/
[gnumeric]: http://projects.gnome.org/gnumeric/
[log-func]: /python/inline-script/#inline_script.log
[codecs]: http://docs.python.org/2/library/codecs.html
[ppa]: https://launchpad.net/~smathot/+archive/cogscinl/