title: Acerca de JavaScript
hash: a7f9ce07f8ba8ef35658430e6e490db256a6c6c1681e7b791f85a4d8f288ae44
locale: es
language: Spanish

En OpenSesame puedes crear experimentos complejos usando solo la interfaz gráfica de usuario (GUI). Pero a veces te encontrarás con situaciones en las que la funcionalidad proporcionada por la GUI es insuficiente. En estos casos, puedes agregar código JavaScript a tu experimento.

JavaScript es para experimentos que se ejecutan en un navegador con OSWeb. Si necesitas ejecutar tu experimento en el escritorio, debes usar [Python](%url:manual/python/about%) en lugar de JavaScript.

__Nota de la versión:__ El soporte de escritorio para JavaScript se eliminó en OpeSesame 4.0. Esto se debe a que el soporte de JavaScript en el escritorio estaba incompleto y los usuarios lo percibieron como confuso sin agregar mucho beneficio.
{: .page-notification}

[TOC]


## Aprendiendo JavaScript

Hay muchos tutoriales de JavaScript disponibles en línea. Un buen recurso es Code Academy:

- <https://www.codecademy.com/learn/introduction-to-javascript>


## JavaScript en la GUI de OpenSesame


### Ítems Inline_javascript

Para usar código JavaScript debes agregar un ítem INLINE_JAVASCRIPT a tu experimento. Después de hacer esto verás algo como %FigInlineJavaScript.

%--
figure:
 id: FigInlineJavaScript
 source: inline-javascript.png
 caption: El ítem INLINE_JAVASCRIPT.
--%

Como puedes ver, el ítem INLINE_JAVASCRIPT consta de dos pestañas: una para la fase de Preparación y otra para la fase de Ejecución. La fase de Preparación se ejecuta primero, para permitir que los ítems se preparen para la fase de Ejecución, que es de tiempo crítico. Es una buena práctica construir objetos `Canvas` durante la fase de Preparación, para que puedan presentarse sin demora durante la fase de Ejecución. Pero esto es solo una convención; puedes ejecutar código JavaScript arbitrario durante ambas fases.

Para obtener más información sobre la estrategia de preparar-ejecutar, mira:

- %link:prepare-run%


### Imprimiendo output en la consola

Puedes imprimir en la consola con el comando `console.log()`:

```js
console.log('¡Esto aparecerá en la consola!')
```

Cuando se ejecuta en el escritorio, la salida aparecerá en la consola de OpenSesame (o: ventana de depuración). Cuando se ejecuta en un navegador, la salida aparecerá en la consola del navegador.


## Cosas a saber

### Funciones comunes

Muchas funciones comunes están directamente disponibles en un ítem INLINE_JAVASCRIPT. Por ejemplo:

```js
// `Canvas()` es una función de fábrica que devuelve un objeto `Canvas`
let fixdotCanvas = Canvas()
if (sometimes()) {  // A veces el fixdot es verde
    fixdotCanvas.fixdot({color: 'green'})
} else {  // A veces es rojo
    fixdotCanvas.fixdot({color: 'red'})
}
fixdotCanvas.show()
```

Para obtener una lista de funciones comunes, mira:

- %link:manual/javascript/common%


### El objeto `persistent`: preservar objetos a través de scripts

__Nota de la versión__ A partir de OSWeb 2.0, todo el código JavaScript se ejecuta en el mismo espacio de trabajo y los objetos se conservan, por lo tanto, a través de scripts. Esto significa que ya no necesitas el objeto `persistent`.
{:.page-notification}

Cada ítem INLINE_JAVASCRIPT se ejecuta en su propio espacio de trabajo. Esto significa, ¡y esto es diferente de los ítems de Python INLINE_SCRIPT! - que no puedes usar variables o funciones que has declarado en un script en otro script. Como solución alternativa, puedes adjuntar variables o funciones como propiedades al objeto `persistent`, que sirve como un contenedor de cosas que deseas conservar a través de scripts.

De esta manera puedes construir un `Canvas` en un INLINE_JAVASCRIPT...

```js
persistent.myCanvas = Canvas()
persistent.myCanvas.fixdot()
```

.. y mostrarlo en otro INLINE_JAVASCRIPT:

```js
persistent.myCanvas.show()
```


### El objeto `vars`: Acceso a variables experimentales

__Nota de la versión__ A partir de OSWeb 2.0, todas las variables experimentales están disponibles como globales. Esto significa que ya no necesitas el objeto `vars`.
{:.page-notification}

Puedes acceder a las variables experimentales a través del objeto `vars`:

```js
// OSWeb <= 1.4 (con objeto vars)
// Obtén una variable experimental
console.log('my_variable es: ' + vars.my_variable)
// Establece una variable experimental
vars.my_variable = 'mi_valor'

// OSWeb >= 2.0 (sin objeto vars)
// Obtén una variable experimental
console.log('my_variable es: ' + my_variable)
// Establece una variable experimental
var my_variable = 'mi_valor'
```


### El objeto `pool`: Acceso a la piscina de archivos

Se accede a 'archivos' desde la piscina de archivos a través del objeto `pool`. El uso más obvio de esto es para analizar archivos CSV, por ejemplo con condiciones experimentales, de la piscina de archivos utilizando la biblioteca `csv-parse` (descrita en más detalle a continuación).

```js
const conditions = csvParse(
    pool['attentional-capture-jobs.csv'].data,
    {columnas: true}
)
for (const trial of conditions) {
    console.log(trial.distractor)
}
```

También puedes reproducir archivos de sonido directamente desde la piscina de archivos. Suponiendo que hay un archivo llamado `bark.ogg` en la piscina de archivos, puedes reproducirlo de esta manera:

```js
pool['bark.ogg'].data.play()
```


### La clase `Canvas`: Presentando estímulos visuales

La clase `Canvas` se usa para presentar estímulos visuales. Por ejemplo, puedes mostrar un punto de fijación de la siguiente manera:

```js
let myCanvas = Canvas()
myCanvas.fixdot()
myCanvas.show()
```

Una descripción completa de la clase `Canvas` se puede encontrar aquí:

- %link:manual/javascript/canvas%

## Bibliotecas de JavaScript disponibles

Las siguientes bibliotecas de JavaScript están incluidas por defecto:

- [funciones aleatorias (`random-ext`)](%url:manual/javascript/random%)
- [Funciones de conversión de color (`color-convert`)](%url:manual/javascript/color-convert%)
- [Funciones CSV (`csv-parse`)](%url:manual/javascript/csv%)
- [Iteradores estilo Python (`pythonic`)](%url:manual/javascript/pythonic%)

También puedes incluir bibliotecas de JavaScript adicionales mediante las URLs a estas bibliotecas en el campo 'Bibliotecas de JavaScript externas' del panel de control de OSWeb.


## Depuración

Ver:

- %link:debugging%