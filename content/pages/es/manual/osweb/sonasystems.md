title: Sistemas Sona
hash: b16a73f1e8a3fb7fd7efb983a26825940c0de47ec814bf27280a22d31c398657
locale: es
language: Spanish

[TOC]

## Acerca de Sona Systems

Sona Systems es una herramienta en línea que muchas universidades utilizan para reclutar participantes, otorgar créditos de cursos a los estudiantes participantes, etc.

Ver también:

- <https://www.sona-systems.com/help/integration_test.aspx>

## Crear un estudio en JATOS

Primero, importa tu experimento en JATOS, como se describe arriba. Luego, ve al Administrador de Trabajadores y Lotes, activa el Trabajador Múltiple General, obtén una URL haciendo clic en Obtener enlace y cópiala.


## Crear un estudio en Sona Systems

A continuación, crea un estudio en Sona Systems. Inserta la URL del estudio JATOS en el campo etiquetado como "URL del estudio". Esto le dirá a Sona Systems cómo iniciar el experimento. Es importante añadir lo siguiente al final de la URL (esto transmitirá el ID del participante de Sona a tu experimento):

```bash
&SONA_ID=%SURVEY_CODE%
```

Sona Systems no utiliza una URL de redireccionamiento. Esto significa que Sona Systems no sabrá automáticamente si el participante completó o no el estudio.

## Registrar la ID de Sona en tu experimento

Cada participante de Sona se identifica mediante un ID único. Es importante registrar este ID en tu experimento, porque esto te permite saber qué participante de Sona corresponde a cada entrada en los resultados de JATOS. Puedes hacer esto agregando el siguiente script en la fase de preparación de un elemento `inline_javascript` al comienzo de tu experimento.

Al ejecutar el experimento a través de Sona, esto hará que la ID de Sona esté disponible como la variable experimental `sona_participant_id`. Cuando se ejecute el experimento de cualquier otra manera (por ejemplo, durante las pruebas), la variable `sona_participant_id` se configurará en -1.

```javascript
if (window.jatos && jatos.urlQueryParameters.SONA_ID) {
    console.log('La información de Sona está disponible')
    vars.sona_participant_id = jatos.urlQueryParameters.SONA_ID
} else {
    console.log('La información de Sona no está disponible (estableciendo el valor en -1)')
    vars.sona_participant_id = -1
}
console.log('sona_participant_id = ' + vars.sona_participant_id)
```

## Otorgar créditos automáticamente al completar el estudio

Sona Systems proporciona una URL de finalización (lado del cliente), que se debe llamar cuando se completa correctamente un estudio, para que Sona Systems pueda otorgar crédito al participante (ver %FigCompletionURL).

%--
figure:
 id: FigCompletionURL
 source: completion-url.png
 caption: La URL de finalización en la información del estudio de Sona Systems.
--%

La URL de finalización (lado del cliente) tiene tres argumentos en ella:

- `experiment_id` que identifica el estudio y es el mismo para todos los participantes
- `credit_token` que (aparentemente) cambia cuando se modifica la información del estudio, pero de lo contrario es el mismo para todos los participantes
- `survey_code` que corresponde a la ID de participante de Sona y, por lo tanto, es diferente para cada participante

Copia la URL de finalización y reemplaza las `XXX` por `[SONA_ID]`. Ve a las propiedades del estudio en JATOS e inserta la URL resultante en el campo de URL de redireccionamiento final.

%--
figure:
 id: FigEndRedirectURL
 source: end-redirect-url.png
 caption: La URL de redireccionamiento final en las propiedades del estudio JATOS.
--%