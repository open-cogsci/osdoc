title: Sistemas Sona
hash: d944a35b3e0c80d34ad14fc5152e628c6249312a06e28b86e5e6da4470fa60a2
locale: es
language: Spanish

[TOC]


## Acerca de Sona Systems

Sona Systems es una herramienta en línea que muchas universidades utilizan para reclutar participantes, otorgar crédito de curso a los participantes estudiantes, etc.

Ver también:

- <https://www.sona-systems.com/help/integration_test.aspx>


## Crear un estudio en JATOS

Primero, importa tu experimento a JATOS, tal como se describió anteriormente. A continuación, ve al administrador de Worker & Batch, activa el trabajador múltiple general, obtén una URL haciendo clic en Obtener enlace, y cópiala.


## Crear un estudio en Sona Systems

Luego, crea un estudio en Sona Systems. Inserta la URL del estudio JATOS en el campo etiquetado como "URL del estudio". Esto le dirá a Sona Systems cómo iniciar el experimento. Importante, agrega lo siguiente al final de la URL (esto pasará la ID del participante de Sona a tu experimento):

```bash
&SONA_ID=%SURVEY_CODE% 
```

Sona Systems no utiliza una URL de redireccionamiento. Esto significa que Sona Systems no sabrá automáticamente si el participante terminó o no el estudio.


## Registrar la ID de Sona en tu experimento

Cada participante de Sona está identificado por una ID única. Es importante registrar esta ID en tu experimento, ya que te permite reconocer qué participante de Sona corresponde a qué entrada en los resultados de JATOS. Puedes hacerlo agregando el siguiente script en la fase de preparación de un artículo `inline_javascript` al comienzo de tu experimento.

Cuando se ejecuta el experimento a través de Sona, esto hará que la ID de Sona esté disponible como la variable experimental `sona_participant_id`. Cuando se ejecuta el experimento de cualquier otra manera (por ejemplo, durante las pruebas), la variable `sona_participant_id` se establecerá en -1. 


```javascript
if (window.jatos && jatos.urlQueryParameters.SONA_ID) {
    console.log('La información de Sona está disponible')
    var sona_participant_id = jatos.urlQueryParameters.SONA_ID
} else {
    console.log('La información de Sona no está disponible (estableciendo el valor en -1)')
    var sona_participant_id = -1
}
console.log('sona_participant_id = ' + sona_participant_id)
```


## Otorgar créditos automáticamente al completar el estudio

Sona Systems proporciona una URL de finalización (lado del cliente), que se debe llamar cuando un estudio se completa con éxito, para que Sona Systems pueda otorgar crédito al participante (ver %FigCompletionURL).

%--
figure:
 id: FigCompletionURL
 source: completion-url.png
 caption: La URL de finalización en la información del estudio de Sona Systems.
--%

La URL de finalización (lado del cliente) tiene tres argumentos en ella:

- `experiment_id` que identifica el estudio y es el mismo para todos los participantes
- `credit_token` que (aparentemente) cambia cuando cambias la información del estudio, pero por lo demás es el mismo para todos los participantes
- `survey_code` que corresponde a la ID del participante de Sona, y por lo tanto es diferente para cada participante

Copia la URL de finalización, y reemplaza los `XXX` por `[SONA_ID]`. Ve a las Propiedades del Estudio en JATOS, e inserta la URL resultante en el campo URL de Redirección Final.

%--
figure:
 id: FigEndRedirectURL
 source: end-redirect-url.png
 caption: La URL de redirección final en las propiedades del estudio JATOS.
--%