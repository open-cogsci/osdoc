title: WebGazer.js
hash: 47ee55649881bcf2ff92c750daeac0bdea5feb3a8719e0e99c5309e49686ecc6
locale: es
language: Spanish

Requiere OSWeb v1.4.6.1
{:.page-notification}

[TOC]

## Acerca de WebGazer

WebGazer.js es una biblioteca de seguimiento ocular escrita en JavaScript. Puedes incluirla con OSWeb para realizar seguimiento ocular en experimentos en línea.

- <https://webgazer.cs.brown.edu/>

## Incluir WebGazer.js en el experimento

WebGazer.js no viene incluido por defecto en OSWeb. Sin embargo, puedes incluirlo como una biblioteca externa colocando un enlace a `webgazer.js` en Bibliotecas externas de JavaScript. Actualmente, un enlace funcional es:

```
https://webgazer.cs.brown.edu/webgazer.js
```

Ver también:

- %link:manual/osweb/osweb%

## Experimento de ejemplo

A continuación, puedes descargar un experimento de ejemplo que utiliza WebGazer.js. Primero se les pide a los participantes que hagan clic y miren un conjunto de puntos; esto hará que WebGazer.js realice automáticamente algo similar a un procedimiento de calibración. A continuación, el experimento muestra una pantalla sencilla para probar la precisión en la grabación de la posición de la mirada. En general, el seguimiento ocular de grano fino no es factible, pero se puede saber en qué cuadrante de la pantalla está mirando el participante. Para ejecutar este experimento, debes incluir WebGazer.js en el experimento, como se describió anteriormente.

- %static:attachments/webgazer.osexp%

También puedes iniciar el experimento directamente en el navegador:

- <https://jatos.mindprobe.eu/publix/BowSAFY2VWl>