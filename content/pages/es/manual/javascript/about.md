title: Acerca de JavaScript
hash: 073e796248136726c6b04b838715a867d5ef1958a34beae0785870553faa2e4c
locale: es
language: Spanish

En OpenSesame, puedes crear experimentos complejos utilizando únicamente la interfaz gráfica de usuario (GUI). Pero a veces te encontrarás con situaciones en las que la funcionalidad proporcionada por la GUI es insuficiente. En estos casos, puedes agregar código JavaScript a tu experimento.

JavaScript es para experimentos que se ejecutan en un navegador con OSWeb. Si necesitas ejecutar tu experimento en el escritorio, debes usar [Python](%url:manual/python/about%) en lugar de JavaScript.

__Nota de versión:__ El soporte de escritorio para JavaScript se eliminó en OpeSesame 4.0. Esto se debe a que el soporte de JavaScript en el escritorio estaba incompleto y era percibido por los usuarios como confuso sin aportar mucho beneficio.
{: .page-notification}

[TOC]


## Aprender JavaScript

Hay muchos tutoriales de JavaScript disponibles en línea. Un buen recurso es Code Academy:

- <https://www.codecademy.com/learn/introduction-to-javascript>


## JavaScript en la GUI de OpenSesame


### elementos Inline_javascript

Para usar código JavaScript, debes agregar un elemento INLINE_JAVASCRIPT a tu experimento. Después de hacer esto, verás algo como %FigInlineJavaScript.

%--
figure:
 id: FigInlineJavaScript
 source: inline-javascript.png
 caption: El elemento INLINE_JAVASCRIPT.
--%

Como puedes ver, el elemento INLINE_JAVASCRIPT consta de dos pestañas: una para la fase de preparación y otra para la fase de ejecución. La fase de preparación se ejecuta primero, para permitir que los elementos se preparen para la fase de ejecución crítica en tiempo. Es una buena práctica construir objetos `Canvas` durante la fase de preparación, para que puedan presentarse sin demora durante la fase de ejecución. Pero esto es solo una convención; puedes ejecutar código JavaScript arbitrario durante ambas fases.

Para obtener más información sobre la estrategia de preparación-ejecución, consulte:

- %link:prepare-run%


### Imprimir la salida en la consola

Puedes imprimir en la consola con el comando `console.log()`:

```js
console.log('¡Esto aparecerá en la consola!')
```

Al ejecutarse en el escritorio, la salida aparecerá en la consola de OpenSesame (o: ventana de depuración). Al ejecutarse en un navegador, la salida aparecerá en la consola del navegador.


## Cosas que debes saber

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

Para obtener una lista de funciones comunes, consulte:

- %link:manual/javascript/common%


### El objeto `persistent`: conservar objetos en varios scripts

__Nota de versión__ A partir de OSWeb 2.0, todo el código JavaScript se ejecuta en el mismo espacio de trabajo y, por lo tanto, los objetos se conservan en varios scripts. Esto significa que ya no necesitas el objeto `persistent`.
{:.page-notification}

Cada elemento INLINE_JAVASCRIPT se ejecuta en su propio espacio de trabajo. Esto significa, ¡y esto es diferente de los elementos INLINE_SCRIPT de Python! — que no puedes utilizar variables o funciones que hayas declarado en un script en otro script. Como solución alternativa, puedes adjuntar variables o funciones como propiedades al objeto `persistent`, que sirve como contenedor de cosas que deseas conservar en varios scripts.

De esta manera, puedes construir un `Canvas` en un INLINE_JAVASCRIPT ...

```js
persistent.myCanvas = Canvas()
persistent.myCanvas.fixdot()
```

.. y muéstralo en otro INLINE_JAVASCRIPT:

```js
persistent.myCanvas.show()
```


### El objeto `vars`: acceso a las variables experimentales

__Nota de versión__ A partir de OSWeb 2.0, todas las variables experimentales están disponibles como globales. Esto significa que ya no necesitas el objeto `vars`.
{:.page-notification}

Puedes acceder a las variables experimentales a través del objeto `vars`:

```js
// Obtener una variable experimental
console.log('mi_variable es: ' + vars.my_variable)
// Establecer una variable experimental
vars.my_variable = 'mi_valor'
```

### El objeto `pool`: acceso al grupo de archivos

Puedes acceder a los 'archivos' del grupo de archivos a través del objeto `pool`. El uso más obvio de esto es analizar archivos CSV, por ejemplo con condiciones experimentales, desde el grupo de archivos utilizando la biblioteca `csv-parse` (descrita con más detalle a continuación).

```js
const conditions = csvParse(
    pool['attentional-capture-jobs.csv'].data,
    {columns: true}
)
for (const trial of conditions) {
    console.log(trial.distractor)
}
```

También puedes reproducir archivos de sonido directamente desde el grupo de archivos. Suponiendo que haya un archivo llamado `bark.ogg` en el grupo de archivos, puedes reproducirlo de la siguiente manera:

```js
pool['bark.ogg'].data.play()
```


### La clase `Canvas`: presentando estímulos visuales

La clase `Canvas` se utiliza para presentar estímulos visuales. Por ejemplo, puedes mostrar un punto de fijación de la siguiente manera:

```js
let myCanvas = Canvas()
myCanvas.fixdot()
myCanvas.show()
```

Se puede encontrar una descripción completa de la clase `Canvas` aquí:

- %link:manual/javascript/canvas%

## Bibliotecas de JavaScript disponibles

Las siguientes bibliotecas de JavaScript están incluidas de forma predeterminada:

- [Funciones aleatorias (`random-ext`)](%url:manual/javascript/random%)
- [Funciones de conversión de colores (`color-convert`)](%url:manual/javascript/color-convert%)
- [Funciones CSV (`csv-parse`)](%url:manual/javascript/csv%)
- [Iteradores estilo Python (`pythonic`)](%url:manual/javascript/pythonic%)

Puedes incluir bibliotecas adicionales de JavaScript agregando las URLs a las bibliotecas en el campo 'Bibliotecas de JavaScript externas' del panel de control de OSWeb.

## Depuración

La mayoría de los navegadores modernos, especialmente Chrome y Firefox, cuentan con un depurador integrado potente. Puedes activar el depurador agregando una línea que simplemente indique `debugger` a tu script (%FigDebuggerInlineJavaScript).

%--
figure:
 id: FigDebuggerInlineJavaScript
 source: debugger-inline-javascript.png
 caption: Activando el depurador desde un elemento INLINE_JAVASCRIPT.
--%

Luego, inicia el experimento y muestra el depurador (o: Dev tools en Chrome, o: Web Developer Tools en Firefox) tan pronto como aparezca la pantalla de bienvenida de OSWeb. El depurador pausará el experimento cuando encuentre la declaración `debugger`. En este punto, puede usar la Consola para interactuar con el espacio de trabajo de JavaScript, o puede inspeccionar variables usando la herramienta Scope (%FigDebuggerChrome).

%--
figure:
 id: FigDebuggerChrome
 source: debugger-chrome.png
 caption: Inspeccionando el ámbito de las variables en Chrome.
--%

Ver también:

- %link:manual/osweb/osweb%