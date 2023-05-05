title: Prolífico
hash: ae0240db997107f3570b2cbf0d4576f801d25a57fbdd0a043e7f8be1bb82d715
locale: es
language: Spanish

[TOC]


## Acerca de Prolific

[Prolific](https://prolific.co/) es una herramienta comercial para reclutar participantes para investigaciones. Para ejecutar experimentos OSWeb en Prolific, debes seguir los pasos explicados a continuación.

Ver también:

- <http://www.jatos.org/Use-Prolific.html>


## Crear un estudio en JATOS

Primero, importa tu experimento a JATOS, como se describe anteriormente. A continuación, ve al Administrador de trabajadores y grupos, activa el Trabajador múltiple general, obtén una URL haciendo clic en Obtener enlace y copiala (%FigJatosURL).


%--
figure:
 id: FigJatosURL
 source: jatos-url.png
 caption: Obtén una URL de estudio de JATOS.
--%



## Crear un estudio en Prolific

Luego, crea un estudio en Prolific. En Detalles del estudio (%FigProlific), inserta la URL del estudio JATOS en el campo etiquetado como "¿Cuál es la URL de tu estudio?". Esto le dirá a Prolific cómo iniciar el experimento. Importante, agrega lo siguiente al final de la URL (esto pasará información importante de Prolific a tu experimento):

{% raw %}
```bash
&PROLIFIC_PID={{%PROLIFIC_PID%}}&STUDY_ID={{%STUDY_ID%}}&SESSION_ID={{%SESSION_ID%}}
```
{% endraw %}

Cuando el experimento termine, Prolific necesita saberlo. Para este propósito, Prolific utiliza una URL de redireccionamiento final, que se encuentra en el campo etiquetado como "Para demostrar que los participantes han completado tu estudio...". Copia esta URL de redireccionamiento final. También marca la casilla etiquetada como "He configurado mi estudio para redirigir a esta url al final".

%--
figure:
 id: FigProlific
 source: prolific.png
 caption: Detalles del estudio en Prolific.
--%



## Establece una URL de redireccionamiento final en JATOS

Ahora regresa a JATOS y abre las Propiedades de tu estudio (%FigJatosProperties). Allí, pega la URL de redireccionamiento final que has copiado de Prolific en el campo etiquetado como "End Redirect URL". Esto le dirá a JATOS que el participante debe ser redirigido de vuelta a Prolific cuando el experimento haya terminado, de modo que Prolific sepa que el participante completó el experimento.

%--
figure:
 id: FigJatosProperties
 source: jatos-properties.png
 caption: Establecer la URL de redireccionamiento final en JATOS.
--%


## Registra la información de Prolific en tu experimento

Cada participante de Prolific es identificado por un ID único. Es importante registrar este ID en tu experimento, porque esto te permitirá saber qué participante de Prolific corresponde a qué entrada en los resultados de JATOS. Puedes hacer esto agregando el siguiente script en la fase de preparación de un ítem `inline_javascript` al comienzo de tu experimento.

Cuando se ejecuta el experimento a través de Prolific, esto hará que la ID de Prolific esté disponible como la variable experimental `prolific_participant_id`. Cuando se ejecute el experimento de cualquier otra manera (por ejemplo, durante pruebas), la variable `prolific_participant_id` se establecerá en -1. La misma lógica se aplica a la ID de estudio de Prolific (`prolific_study_id`) y la ID de sesión de Prolific (`prolific_session_id`).

```javascript
if (window.jatos && jatos.urlQueryParameters.PROLIFIC_PID) {
    console.log('La información de Prolific está disponible')
    vars.prolific_participant_id = jatos.urlQueryParameters.PROLIFIC_PID
    vars.prolific_study_id = jatos.urlQueryParameters.STUDY_ID
    vars.prolific_session_id = jatos.urlQueryParameters.SESSION_ID
} else {
    console.log('La información de Prolific no está disponible (estableciendo valores en -1)')
    vars.prolific_participant_id = -1
    vars.prolific_study_id = -1
    vars.prolific_session_id = -1
}
console.log('prolific_participant_id = ' + vars.prolific_participant_id)
console.log('prolific_study_id = ' + vars.prolific_study_id)
console.log('prolific_session_id = ' + vars.prolific_session_id)
```


## Prueba el estudio

Vuelve a la página de Detalles del Estudio en Prolific. En la parte inferior de la página, hay un botón de Vista Previa. Esto te permite probar el experimento actuando como un participante tú mismo. ¡No olvides revisar los resultados de JATOS para asegurarte de que el experimento haya finalizado correctamente y que toda la información necesaria (incluida la información de Prolific) se haya registrado!