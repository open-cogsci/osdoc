title: Caja SR
hash: 4071d0970094db9727787578d613e899ded69a490b5c9c3e902816836096ee9a
locale: es
language: Spanish

[TOC]

## Acerca del plugin srbox

La caja de respuestas serie (SR) es una caja de botones, diseñada específicamente para la recolección de respuestas en experimentos psicológicos. La versión original, desarrollada por Psychology Software Tools, tiene 5 botones, 5 luces y se conecta a la PC a través del puerto serie. También existen dispositivos compatibles con SR Box de otros fabricantes, que pueden diferir en el número de botones y luces y suelen utilizar una conexión USB, que emula un puerto serie.

El plugin SRBOX para OpenSesame te permite usar la caja de respuestas serie o un dispositivo compatible en tus experimentos con OpenSesame.

## Captura de pantalla

%--
figure:
  source: srbox.png
  id: FigSrbox
  caption: El plugin srbox en OpenSesame.
--%

## Establecer el nombre del dispositivo

De forma predeterminada, el plugin intenta detectar automáticamente tu SR Box. Si esto funciona, no tienes que cambiarlo. Si tu experimento se bloquea, OpenSesame ha elegido el puerto serie incorrecto y debes ingresar el nombre del dispositivo manualmente. En Windows, el dispositivo probablemente se llama algo así como

```text
COM4
```

En Linux, el dispositivo probablemente se llama algo así como

``` text
/dev/tty0
```

## Requisitos

Una caja de botones SR Box o compatible. No todas las cajas de botones son compatibles, consulta:

- %link:buttonbox%

## Usar la SR Box desde el código Python en línea

El objeto `srbox` *no* existe cuando el plugin está en modo dummy.

%-- include: include/api/srbox.md --%