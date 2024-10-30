title: Acerca de JavaScript
hash: 89b8cd7f6f738823b8fc04558cb7b3e118768d97f5e91a82f90905cbf9bdbe6e
locale: es
language: Spanish

En OpenSesame puedes crear experimentos complejos usando únicamente la interfaz gráfica de usuario (GUI). Pero a veces te encontrarás con situaciones en las que la funcionalidad proporcionada por la GUI es insuficiente. En estos casos puedes agregar código JavaScript a tu experimento.

JavaScript es para experimentos que se ejecutan en un navegador con OSWeb. Si necesitas ejecutar tu experimento en el escritorio, debes usar [Python](%url:manual/python/about%) en lugar de JavaScript.

__Nota sobre la versión:__ El soporte de JavaScript para escritorio fue eliminado en OpenSesame 4.0. Esto se debe a que el soporte de JavaScript en el escritorio era incompleto y fue percibido por los usuarios como confuso sin añadir mucho beneficio.
{: .page-notification}


## Aprendiendo JavaScript

Hay muchos tutoriales de JavaScript disponibles en línea. Un buen recurso es Code Academy:

- <https://www.codecademy.com/learn/introduction-to-javascript>


## JavaScript en la GUI de OpenSesame


### Elementos Inline_javascript

Para usar código JavaScript necesitas agregar un elemento INLINE_JAVASCRIPT a tu experimento. Después de hacer esto verás algo como %FigInlineJavaScript.

figure:
 id: FigInlineJavaScript
 source: inline-javascript.png
 caption: El elemento INLINE_JAVASCRIPT.
{: .notranslate}

Como puedes ver, el elemento INLINE_JAVASCRIPT consta de dos pestañas: una para la fase Prepare y otra para la fase Run. La fase Prepare se ejecuta primero, para permitir que los elementos se preparen para la fase Run que es crítica en tiempo. Es buena práctica construir objetos `Canvas` durante la fase Prepare, para que puedan ser presentados sin retraso durante la fase Run. Pero esto es solo una convención; puedes ejecutar código JavaScript arbitrario durante ambas fases.

Para más información sobre la estrategia prepare-run, consulta:

- %link:prepare-run%


### Imprimir salida en la consola

Puedes imprimir en la consola con el comando `console.log()`:

```js
console.log('¡Esto aparecerá en la consola!')
```

Cuando se ejecuta en el escritorio, la salida aparecerá en la consola de OpenSesame (o: ventana de depuración). Cuando se ejecuta en un navegador, la salida aparecerá en la consola del navegador.


## Cosas que saber

### Funciones comunes

Muchas funciones comunes están disponibles directamente en un elemento INLINE_JAVASCRIPT. Por ejemplo:

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

Para una lista de funciones comunes, consulta:

- %link:manual/javascript/common%


### Declarando variables (let y var)

Los elementos INLINE_JAVASCRIPT se ejecutan en modo no estricto (o: laxo). Esto significa que puedes asignar un valor a una variable que no fue declarada explícitamente. Cuando haces esto, la variable se declara implícitamente usando `var` si no se había declarado previamente.

```js
my_variable = 'mi valor'  // declarada implícitamente usando var
```

Las variables que son declaradas implícita o explícitamente usando `var` son globales, lo que principalmente significa que pueden ser registradas por un LOGGER. Las variables que se declaran usando `let` no son globales, lo que principalmente significa que no son registradas por un LOGGER.

```js
this_is_a_global_variable = 'mi valor'
var this_is_also_a_global_variable = 'mi valor'
let this_is_not_a_global_variable = 'mi valor'
```


### El objeto `persistent`: preservando objetos a través de los scripts

__Nota sobre la versión__ A partir de OSWeb 2.0, todo el código JavaScript se ejecuta en el mismo espacio de trabajo y por lo tanto los objetos se conservan a través de los scripts. Esto significa que ya no necesitas el objeto `persistent`.
{:.page-notification}

Cada elemento INLINE_JAVASCRIPT se ejecuta en su propio espacio de trabajo. Esto significa—¡y esto es diferente de los elementos INLINE_SCRIPT de Python!—que no puedes usar variables o funciones que hayas declarado en un script en otro. Como solución alternativa, puedes adjuntar variables o funciones como propiedades al objeto `persistent`, que sirve como contenedor de cosas que quieres conservar a través de los scripts.

De esta manera, puedes construir un `Canvas` en un INLINE_JAVASCRIPT ...

```js
persistent.myCanvas = Canvas()
persistent.myCanvas.fixdot()
```

... y mostrarlo en otro INLINE_JAVASCRIPT:

```js
persistent.myCanvas.show()
```


### El objeto `vars`: Acceso a las variables experimentales

__Nota de versión__ A partir de OSWeb 2.0, todas las variables experimentales están disponibles como globales. Esto significa que ya no necesitas el objeto `vars`.
{:.page-notification}

Puedes acceder a las variables experimentales a través del objeto `vars`:

```js
// OSWeb <= 1.4 (con objeto vars)
// Obtener una variable experimental
console.log('my_variable es: ' + vars.my_variable)
// Establecer una variable experimental
vars.my_variable = 'my_value'

// OSWeb >= 2.0 (sin objeto vars)
// Obtener una variable experimental
console.log('my_variable es: ' + my_variable)
// Establecer una variable experimental
my_variable = 'my_value'
```


### El objeto `pool`: Acceso al banco de archivos

Accedes a los 'archivos' del banco de archivos a través del objeto `pool`. El uso más obvio de esto es analizar archivos CSV, por ejemplo con condiciones experimentales, del banco de archivos utilizando la biblioteca `csv-parse` (descrita con más detalle a continuación).

```js
const conditions = csvParse(
    pool['attentional-capture-jobs.csv'].data,
    {columns: true}
)
for (const trial of conditions) {
    console.log(trial.distractor)
}
```

También puedes reproducir archivos de sonido directamente desde el banco de archivos. Suponiendo que hay un archivo llamado `bark.ogg` en el banco de archivos, puedes reproducirlo así:

```js
audioContext = new (window.AudioContext || window.webkitAudioContext)()
source = audioContext.createBufferSource()
source.buffer = pool['bark.ogg'].data
source.connect(audioContext.destination)
source.start(0)
```

Ten en cuenta que en versiones anteriores de OSWeb simplemente podrías usar `pool['bark.ogg'].data.play()`. Sin embargo, esto ya no funciona desde que OSWeb migró a Web Audio API, que es una forma más moderna y ampliamente soportada de reproducir audio.


### La clase `Canvas`: Presentación de estímulos visuales

La clase `Canvas` se utiliza para presentar estímulos visuales. Por ejemplo, puedes mostrar un punto de fijación de la siguiente manera:

```js
let myCanvas = Canvas()
myCanvas.fixdot()
myCanvas.show()
```

Una visión completa de la clase `Canvas` se puede encontrar aquí:

- %link:manual/javascript/canvas%

## Bibliotecas de JavaScript disponibles

Las siguientes bibliotecas de JavaScript están incluidas por defecto:

- [Funciones aleatorias (`random-ext`)](%url:manual/javascript/random%)
- [Funciones de conversión de colores (`color-convert`)](%url:manual/javascript/color-convert%)
- [Funciones CSV (`csv-parse`)](%url:manual/javascript/csv%)
- [Iteradores estilo Python (`pythonic`)](%url:manual/javascript/pythonic%)

Puedes incluir bibliotecas adicionales de JavaScript añadiendo URLs de las bibliotecas en el campo 'Bibliotecas de JavaScript externas' del panel de control de OSWeb.


## Depuración

Ver:

- %link:debugging%